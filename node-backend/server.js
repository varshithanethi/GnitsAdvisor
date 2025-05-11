const express = require('express');
const { Pool } = require('pg');
const cors = require('cors');
const OpenAI = require('openai');
require('dotenv').config();

const app = express();

// Middleware
app.use(cors());
app.use(express.json());

// Initialize OpenAI with API key
const openai = new OpenAI({
    apiKey: process.env.OPENAI_API_KEY
});

// Add document URLs after OpenAI initialization
const ACADEMIC_LINKS = {
    midExams: 'https://gnits.ac.in/wp-content/uploads/2025/02/MID-EXAM-TT-SECOND-AND-THIRD-YEAR.pdf',
    semExams: 'https://gnits.ac.in/wp-content/uploads/2025/04/B.TECH-MTECH-EXAM-NOTIFICATION-JULY-2025.pdf',
    academicCalendar: 'https://gnits.ac.in/wp-content/uploads/2025/04/ACADEMIC-CALENDAR-2025-2026.pdf',
    revisedExams: 'https://gnits.ac.in/wp-content/uploads/2025/04/REVISED-B.TECH-2-2-AND-3-2-EXAM-TIME-TABLES-MAY-2025.pdf',
    resultsPortal: 'http://43.225.26.107/'
};

// Add button configurations
const BUTTON_INFO = {
    student: [
        { id: 'mid-exams', text: 'Mid Exam Schedule 📅', url: ACADEMIC_LINKS.midExams },
        { id: 'sem-exams', text: 'Semester Exams 📚', url: ACADEMIC_LINKS.semExams },
        { id: 'revised-schedule', text: 'Revised Schedule 🔄', url: ACADEMIC_LINKS.revisedExams },
        { id: 'academic-calendar', text: 'Academic Calendar 📆', url: ACADEMIC_LINKS.academicCalendar },
        { id: 'results', text: 'Check Results 📊', url: ACADEMIC_LINKS.resultsPortal }
    ],
    parent: [
        { id: 'results', text: 'Student Results 📊', url: ACADEMIC_LINKS.resultsPortal },
        { id: 'academic-calendar', text: 'Academic Calendar 📆', url: ACADEMIC_LINKS.academicCalendar },
        { id: 'exam-schedule', text: 'Exam Schedules 📅', url: ACADEMIC_LINKS.semExams }
    ],
    faculty: [
        { id: 'exam-schedule', text: 'Exam Schedule 📅', url: ACADEMIC_LINKS.semExams },
        { id: 'revised-schedule', text: 'Revised Schedule 🔄', url: ACADEMIC_LINKS.revisedExams },
        { id: 'results-portal', text: 'Results Portal 📊', url: ACADEMIC_LINKS.resultsPortal }
    ]
};

// PostgreSQL connection
const pool = new Pool({
    user: process.env.PG_USER,
    password: process.env.PG_PASSWORD,
    host: process.env.PG_HOST,
    database: process.env.PG_DATABASE,
    port: process.env.PG_PORT
});

// Health check route
app.get('/api/health', (req, res) => {
    res.json({ status: 'healthy', timestamp: new Date() });
});

// Route to get button info
app.get('/api/button-info/:userType', (req, res) => {
    const { userType } = req.params;
    const buttons = BUTTON_INFO[userType] || [];
    res.json({ status: 'success', buttons });
});

// GPT-powered chat endpoint
app.post('/api/chat-gpt', async (req, res) => {
    try {
        const { message, user_type } = req.body;

        // Enhanced system prompt with academic information
        const systemPrompt = `You are GNITS Assistant, a helpful chatbot for G. Narayanamma Institute of Technology & Science.
            You're speaking with a ${user_type}. 
            
            Available resources:
            - Mid Exam Schedule for Second and Third Year
            - B.Tech and M.Tech Exam Notifications
            - Academic Calendar 2025-2026
            - Revised Exam Schedules
            - Results Portal
            
            Provide accurate, relevant information about GNITS.
            Use formal language and be concise.
            For exam schedules and results, direct users to use the appropriate buttons.`;

        const completion = await openai.chat.completions.create({
            model: "gpt-3.5-turbo",
            messages: [
                { role: "system", content: systemPrompt },
                { role: "user", content: message }
            ],
            temperature: 0.7,
            max_tokens: 500
        });

        const gptResponse = completion.choices[0].message.content;

        // Store conversation in PostgreSQL
        await pool.query(
            'INSERT INTO chat_messages (user_type, message, response, timestamp) VALUES ($1, $2, $3, CURRENT_TIMESTAMP)',
            [user_type, message, gptResponse]
        );

        // Add button info to response
        const buttons = BUTTON_INFO[user_type] || [];
        res.json({
            status: 'success',
            response: gptResponse,
            buttons: buttons,
            timestamp: new Date()
        });

    } catch (error) {
        console.error('Error:', error);
        res.status(500).json({
            status: 'error',
            message: 'Failed to process chat request',
            error: error.message
        });
    }
});

// Start server
const PORT = process.env.NODE_PORT || 3001;
app.listen(PORT, () => {
    console.log(`Node.js server running on port ${PORT}`);
    console.log('GPT integration active');
    console.log('PostgreSQL connection configured');
});