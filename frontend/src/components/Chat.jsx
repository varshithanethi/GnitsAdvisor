import React, { useState, useEffect } from 'react';

const Chat = () => {
    const [message, setMessage] = useState('');
    const [userType, setUserType] = useState('');
    const [chatHistory, setChatHistory] = useState([]);
    const [buttons, setButtons] = useState([]);

    const sendMessage = async (e) => {
        e.preventDefault();
        if (!message.trim() || !userType) return;

        try {
            // Add user message to chat
            setChatHistory(prev => [...prev, { type: 'user', content: message }]);

            // Send to Node.js backend
            const response = await fetch('http://localhost:3001/api/chat-gpt', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    message,
                    user_type: userType
                })
            });

            const data = await response.json();

            // Add bot response to chat
            setChatHistory(prev => [...prev, { 
                type: 'bot', 
                content: data.response 
            }]);

            // Update buttons if provided
            if (data.buttons) {
                setButtons(data.buttons);
            }

            // Clear input
            setMessage('');

        } catch (error) {
            console.error('Error:', error);
            setChatHistory(prev => [...prev, { 
                type: 'bot', 
                content: 'Sorry, I encountered an error. Please try again.' 
            }]);
        }
    };

    const selectUserType = (type) => {
        setUserType(type);
        // Fetch buttons for user type
        fetch(`http://localhost:3001/api/button-info/${type}`)
            .then(res => res.json())
            .then(data => {
                if (data.status === 'success') {
                    setButtons(data.buttons);
                }
            })
            .catch(err => console.error('Error loading buttons:', err));
    };

    const handleButtonClick = (url) => {
        window.open(url, '_blank');
    };

    return (
        <div className="chat-container">
            {!userType ? (
                <div className="user-type-selection">
                    <button onClick={() => selectUserType('student')}>Student 👨‍🎓</button>
                    <button onClick={() => selectUserType('parent')}>Parent 👨‍👩‍👧‍👦</button>
                    <button onClick={() => selectUserType('faculty')}>Faculty 👨‍🏫</button>
                </div>
            ) : (
                <>
                    <div className="chat-history">
                        {chatHistory.map((msg, idx) => (
                            <div key={idx} className={`message ${msg.type}`}>
                                {msg.content}
                            </div>
                        ))}
                    </div>

                    <div className="quick-actions">
                        {buttons.map(button => (
                            <button 
                                key={button.id}
                                onClick={() => handleButtonClick(button.url)}
                                className="action-button"
                            >
                                {button.text}
                            </button>
                        ))}
                    </div>

                    <form onSubmit={sendMessage} className="chat-input">
                        <input
                            type="text"
                            value={message}
                            onChange={(e) => setMessage(e.target.value)}
                            placeholder="Type your message..."
                        />
                        <button type="submit">Send</button>
                    </form>
                </>
            )}
        </div>
    );
};

export default Chat;