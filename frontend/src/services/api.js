const API_URL = 'http://localhost:8080';

export const getFAQResponse = async (query, userType) => {
    try {
        const response = await fetch(`${API_URL}/get_response`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ query, user_type: userType })
        });
        
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        
        return await response.json();
    } catch (error) {
        console.error('API Error:', error);
        throw error;
    }
};

export const getDataStatus = async () => {
    try {
        const response = await fetch(`${API_URL}/data_status`);
        return await response.json();
    } catch (error) {
        console.error('Status Check Error:', error);
        throw error;
    }
};