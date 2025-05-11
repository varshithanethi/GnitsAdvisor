import React, { useState } from 'react';
import { getFAQResponse } from '../services/api';
import '../styles/Chatbot.css';

const Chatbot = () => {
    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState('');
    const [userType, setUserType] = useState('student');
    const [isLoading, setIsLoading] = useState(false);

    const handleSend = async () => {
        if (!input.trim()) return;

        try {
            setIsLoading(true);
            setMessages(prev => [...prev, { type: 'user', content: input }]);

            const response = await getFAQResponse(input, userType);
            setMessages(prev => [...prev, {
                type: 'bot',
                content: response.content
            }]);
            setInput('');
        } catch (error) {
            setMessages(prev => [...prev, {
                type: 'bot',
                content: 'Sorry, I encountered an error. Please try again.'
            }]);
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <div className="chatbot-container">
            <div className="chatbot-header">
                <h2>GNITS Assistant</h2>
                <select 
                    value={userType} 
                    onChange={(e) => setUserType(e.target.value)}
                    className="user-type-select"
                >
                    <option value="student">Student</option>
                    <option value="faculty">Faculty</option>
                    <option value="parent">Parent</option>
                    <option value="guest">Guest</option>
                </select>
            </div>
            
            <div className="chat-messages">
                {messages.map((msg, idx) => (
                    <div key={idx} className={`message ${msg.type}`}>
                        {msg.content}
                    </div>
                ))}
                {isLoading && <div className="message bot loading">Typing...</div>}
            </div>
            
            <div className="chat-input">
                <input
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    onKeyPress={(e) => e.key === 'Enter' && handleSend()}
                    placeholder="Type your question..."
                    disabled={isLoading}
                />
                <button onClick={handleSend} disabled={isLoading}>Send</button>
            </div>
        </div>
    );
};

export default Chatbot;