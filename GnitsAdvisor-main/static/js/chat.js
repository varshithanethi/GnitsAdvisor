const faqData = {
    student: {
        "Admission": [
            "How to apply for admission?",
            "What are the entrance exams accepted?",
            "What is the admission process?",
            "What are the documents required?"
        ],
        "Academics": [
            "What courses are offered?",
            "What is the fee structure?",
            "What is the academic calendar?",
            "How are classes conducted?"
        ],
        "Campus Life": [
            "Tell me about hostel facilities",
            "What are the sports facilities?",
            "What about the library?",
            "Are there any clubs or societies?"
        ]
    },
    parent: {
        "Admissions & Fees": {
            "What is the fee structure?": `### Fee Structure
- Category A & B (JEE) seats: ₹1,00,000 per annum + JNTUH fees
- Category B (NRI) seats: USD 5,000 per annum + JNTUH fees
- M.Tech programs: ₹1,00,000 per annum + JNTUH fees`,
            "What is the admission process?": `### Admission Process
- Through TG-EAMCET counseling
- Candidates must qualify in entrance exam
- Counseling conducted by TSCHE
- Merit-based seat allocation`,
            "Are scholarships available?": `### Available Scholarships
- State-level scholarships for SC/ST students
- BC/EBC scholarships
- Minority Welfare scholarships
- Merit-based scholarships`
        },
        "Hostel & Facilities": {
            "What are the hostel facilities?": `### Hostel Facilities
- AC and Non-AC rooms available
- Each room furnished with:
  - Cot, table, chair
  - Bookshelf, cupboard
- 1,037 students capacity across 218 rooms`,
            "What is the food policy?": `### Hostel Food Policy
- Only vegetarian food served
- Outside food not allowed
- Mess operates during breaks
- No private cooking in rooms`,
            "What are visitor rules?": `### Visitor Rules
- Visitors allowed only on holidays
- Morning hours: 10:00 AM to 1:00 PM
- Evening hours: 4:00 PM to 6:30 PM
- Must register at security`,
            "What about student outings?": `### Outing Policy
- Twice monthly permitted
- Maximum 3 days per visit
- Need warden permission on holidays
- HOD permission on working days
- Return by 6:30 PM`
        },
        "Academic Information": {
            "How to track performance?": `### Student Tracking
- Regular progress reports
- SMS alerts for attendance
- Parent-teacher meetings
- Online portal access
- Direct faculty communication`,
            "What programs are offered?": `### B.Tech Programs
- CSE (Regular & AI/ML/DS)
- ECE
- EEE
- IT
- ETM`,
            "What is the faculty qualification?": `### Faculty Profile
- Highly experienced professors
- Many with Ph.D. degrees
- Active in research
- Industry experience`
        },
        "Safety & Security": {
            "What safety measures exist?": `### Campus Safety
- 24/7 security personnel
- CCTV surveillance
- Biometric access
- Women's safety cell
- Anti-ragging committee`,
            "Is medical facility available?": `### Health Services
- On-campus health center
- Basic medical facilities
- First aid services
- Emergency response system`
        },
        "Campus Facilities": {
            "What infrastructure is available?": `### Campus Infrastructure
- 12.5 acre campus
- Modern laboratories
- Digital library
- Sports facilities
- Wi-Fi enabled campus
- Transportation service`,
            "What about transportation?": `### Transport Facilities
- College bus service
- Multiple routes in Hyderabad
- Professional drivers
- GPS tracking system`
        },
        "Placements": {
            "What is the placement record?": `### Placement Statistics 2024
- Highest Package: ₹51.03 LPA
- Average Package: ₹8.64 LPA
- Placement Rate: 69.58%
- 550 students placed`,
            "Which companies recruit?": `### Recruiting Companies
#### IT Giants
- Microsoft, Google, JP Morgan
- Infosys, TCS, Accenture
- Capgemini, Cognizant

#### Core Companies
- L&T, Carrier, Siemens
- Ashok Leyland

#### Other Notable Companies
- Amazon, Adobe, Flipkart
- EY India, PWC, Micron`
        }
    },
    faculty: {
        "Academic Resources": [
            "What research facilities are available?",
            "What are the lab facilities?",
            "How to access library resources?",
            "What software tools are provided?"
        ],
        "Administration": [
            "How to submit internal marks?",
            "What are the leave policies?",
            "How to organize events?",
            "Contact department heads"
        ]
    },
    visitor: {
        "General Info": [
            "Where is GNITS located?",
            "How to reach the campus?",
            "What are visiting hours?",
            "Whom to contact for queries?"
        ],
        "About GNITS": [
            "Tell me about GNITS",
            "What are the achievements?",
            "Industry collaborations",
            "Placement records"
        ]
    }
};

const userTypeQueries = {
    student: [
        "What courses are offered?",
        "What is the fee structure?",
        "How to apply for admission?",
        "Tell me about placements",
        "What are the hostel facilities?",
        "What about transportation?",
        "Tell me about library facilities",
        "What are the sports facilities?"
    ],
    parent: [
        "What are the safety measures?",
        "What is the fee structure?",
        "How to track student performance?",
        "What about hostel facilities?",
        "Tell me about transportation",
        "When are parent-teacher meetings?",
        "What is the attendance policy?",
        "How to contact faculty?"
    ],
    faculty: [
        "What research facilities are available?",
        "What development programs are offered?",
        "How to access academic resources?",
        "What are the lab facilities?",
        "Tell me about faculty benefits",
        "How to organize events?",
        "What about leave policies?",
        "Research collaboration opportunities"
    ],
    visitor: [
        "Where is GNITS located?",
        "How to reach the campus?",
        "What courses are offered?",
        "Tell me about placements",
        "What are the achievements?",
        "Admission process",
        "Contact information",
        "Campus facilities"
    ]
};

let currentUserType = '';

function selectUserType(type) {
    currentUserType = type;
    document.getElementById('userTypeSelection').classList.add('d-none');
    
    displayUserQueries(type);
}

function backToUserTypes() {
    document.getElementById('userTypeSelection').classList.remove('d-none');
    document.getElementById('faqCategories').classList.add('d-none');
    currentUserType = '';
}

function displayFAQCategories(userType) {
    const faqButtons = document.getElementById('faqButtons');
    faqButtons.innerHTML = '';
    
    Object.entries(faqData[userType]).forEach(([category, questions]) => {
        const categoryDiv = document.createElement('div');
        categoryDiv.className = 'card mb-3';
        
        categoryDiv.innerHTML = `
            <div class="card-header bg-light">
                <h6 class="mb-0">${category}</h6>
            </div>
            <div class="card-body">
                <div class="d-grid gap-2">
                    ${questions.map(q => 
                        `<button class="btn btn-outline-secondary text-start" onclick="askQuestion('${q}')">
                            <i class="fas fa-question-circle me-2"></i>${q}
                        </button>`
                    ).join('')}
                </div>
            </div>
        `;
        
        faqButtons.appendChild(categoryDiv);
    });
}

function addUserMessage(message) {
    const chatMessages = document.getElementById('chatMessages');
    const messageDiv = document.createElement('div');
    messageDiv.className = 'message user-message';
    messageDiv.innerHTML = `
        <div class="user-icon">
            <i class="fas fa-user"></i>
        </div>
        <div class="message-content">
            ${message}
        </div>
    `;
    chatMessages.appendChild(messageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

function addBotMessage(message) {
    const chatMessages = document.getElementById('chatMessages');
    const messageDiv = document.createElement('div');
    messageDiv.className = 'message bot-message';
    
    // Show typing indicator
    const typingDiv = document.createElement('div');
    typingDiv.className = 'message bot-message';
    typingDiv.innerHTML = `
        <div class="message-icon bot-icon"></div>
        <div class="message-content typing-indicator">
            <span class="typing-dot"></span>
            <span class="typing-dot"></span>
            <span class="typing-dot"></span>
        </div>
    `;
    chatMessages.appendChild(typingDiv);
    
    // Remove typing indicator and show message after delay
    setTimeout(() => {
        chatMessages.removeChild(typingDiv);
        messageDiv.innerHTML = `
            <div class="message-icon bot-icon"></div>
            <div class="message-content">
                ${marked.parse(message)}
            </div>
        `;
        chatMessages.appendChild(messageDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }, 1500);
}

// Add clear chat function
function clearChat() {
    const chatMessages = document.getElementById('chatMessages');
    chatMessages.innerHTML = '';
    addBotMessage("Welcome to GNITS FAQ Assistant! Please select your category to get started.");
}

// Update FAQ database
const faqDatabase = {
    student: {
        "Admissions": {
            "What are the eligibility criteria?": "Candidates must have completed their 10+2 education with Mathematics, Physics, and Chemistry as core subjects and must qualify in the TG-EAMCET examination conducted by the Government of Telangana.",
            "How to apply for B.Tech courses?": "Apply through the TG-EAMCET counselling process. After qualifying, attend the counselling session conducted by the Convener for engineering college admissions and choose GNITS based on the availability of seats in the desired branch.",
            "What is the admission process for lateral entry?": "Candidates with a Diploma in Engineering/Technology must qualify in the ECET examination and can apply for lateral entry into the B.Tech program."
        },
        "Courses & Fees": {
            "What B.Tech Courses are offered?": `GNITS offers B.Tech programs in:
- Computer Science and Engineering (CSE)
- Electronics and Communication Engineering (ECE)
- Electrical and Electronics Engineering (EEE)
- Information Technology (IT)
- Electronics and Telematics Engineering (ETM)
- CSE (AI & ML)
- CSE (Data Science)`,
            "What is the fee structure?": "For Category-A and Category-B (JEE) seats, the tuition fee is ₹1,00,000 per annum, plus other JNTUH fees. For Category-B (NRI) seats, the fee is USD 5,000 per annum, plus other JNTUH fees.",
            "What M.Tech Courses are offered?": `GNITS offers M.Tech programs in:
- Computer Science and Engineering (CSE)
- Computer Networks & Information Security (IT)
- Digital Electronics and Comm. System (ECE)
- Power Electronics & Electric Drives (EEE)
- Wireless & Mobile Communications (ETE)`
        },
        "Facilities": {
            "What are the hostel facilities?": "GNITS provides both AC and non-AC rooms in its hostels, equipped with necessary amenities. Each room is furnished with cot, table, chair, bookshelf, and cupboard.",
            "What sports facilities are available?": `Sports facilities include:
Outdoor Sports: Volleyball, Basketball, Throw Ball, Hand Ball, Kho Kho, Kabaddi
Indoor Sports: Indoor Gym, Carroms, Table Tennis, Badminton, Chess`,
            "Is Wi-Fi available on campus?": "Yes, GNITS provides Wi-Fi facility across the campus including hostel premises."
        },
        "Placements": {
            "What is the placement record?": `Placement Statistics:
- Highest Package: ₹51.03 LPA
- Average Package: ₹8.64 LPA
- Placement Percentage: 69.58%`,
            "Which companies recruit from GNITS?": `Top recruiting companies include:
- IT Sector: Microsoft, Deloitte, ServiceNow, Accenture, Capgemini, Cognizant
- Core Sector: L&T, Carrier, Siemens
- Others: Amazon, JPMorgan Chase, Adobe, Flipkart, EY India`

        },
       
            
            "Academic Curriculum": {
                "How to access the curriculum?": `### Accessing Academic Curriculum
    1. Visit https://gnits.ac.in
    2. Hover over Academics menu
    3. Click on Syllabus (UG & PG)
    4. Select your program and department
    
    Available sections under Academics:
    - Admissions
    - Bachelors Programs
    - Auxiliary Departments
    - Syllabus (UG & PG)
    - Masters Programs
    - Academic Timetables
    - Extended Learning
    - Academic Calendar
    - Staff Directory`,
                "What is the B.Tech duration?": "The B.Tech program at GNITS is a 4-year course divided into 8 semesters.",
                "Is the program AICTE approved?": "Yes, the B.Tech program at GNITS is approved by the All India Council for Technical Education (AICTE)."
            },
            "Campus Life": {
                "What clubs are available?": `### Student Clubs at GNITS
    #### Cultural Clubs
    - Samskruthi (Soaring Beyond Boundaries)
    - Litereria Clava (Where Words Become Worlds)
    - Artista (Your Passion, Our Platform)
    - Suswara (Symphony to Your Soul)
    
    #### Community Service Clubs
    - NSS
    - Rotaract Club
    - Street Cause
    - Abhaya
    - Aarambh`,
                "Tell me about library facilities": "GNITS has a well-equipped library with over 34,000 books, including handbooks and reference materials, and subscribes to various technical magazines.",
                "Is transportation available?": "Yes, GNITS provides college bus services covering various routes in Hyderabad for student commuting."
            }
        
    },
    parent: {
        "Admissions & Fees": {
            "What is the fee structure?": `### Fee Structure
- Category A & B (JEE) seats: ₹1,00,000 per annum + JNTUH fees
- Category B (NRI) seats: USD 5,000 per annum + JNTUH fees
- M.Tech programs: ₹1,00,000 per annum + JNTUH fees`,
            "What is the admission process?": `### Admission Process
- Through TG-EAMCET counseling
- Candidates must qualify in entrance exam
- Counseling conducted by TSCHE
- Merit-based seat allocation`,
            "Are scholarships available?": `### Available Scholarships
- State-level scholarships for SC/ST students
- BC/EBC scholarships
- Minority Welfare scholarships
- Merit-based scholarships`
        },
        "Hostel & Facilities": {
            "What are the hostel facilities?": `### Hostel Facilities
- AC and Non-AC rooms available
- Each room furnished with:
  - Cot, table, chair
  - Bookshelf, cupboard
- 1,037 students capacity across 218 rooms`,
            "What is the food policy?": `### Hostel Food Policy
- Only vegetarian food served
- Outside food not allowed
- Mess operates during breaks
- No private cooking in rooms`,
            "What are visitor rules?": `### Visitor Rules
- Visitors allowed only on holidays
- Morning hours: 10:00 AM to 1:00 PM
- Evening hours: 4:00 PM to 6:30 PM
- Must register at security`,
            "What about student outings?": `### Outing Policy
- Twice monthly permitted
- Maximum 3 days per visit
- Need warden permission on holidays
- HOD permission on working days
- Return by 6:30 PM`
        },
        "Academic Information": {
            "How to track performance?": `### Student Tracking
- Regular progress reports
- SMS alerts for attendance
- Parent-teacher meetings
- Online portal access
- Direct faculty communication`,
            "What programs are offered?": `### B.Tech Programs
- CSE (Regular & AI/ML/DS)
- ECE
- EEE
- IT
- ETM`,
            "What is the faculty qualification?": `### Faculty Profile
- Highly experienced professors
- Many with Ph.D. degrees
- Active in research
- Industry experience`
        },
        "Safety & Security": {
            "What safety measures exist?": `### Campus Safety
- 24/7 security personnel
- CCTV surveillance
- Biometric access
- Women's safety cell
- Anti-ragging committee`,
            "Is medical facility available?": `### Health Services
- On-campus health center
- Basic medical facilities
- First aid services
- Emergency response system`
        },
        "Campus Facilities": {
            "What infrastructure is available?": `### Campus Infrastructure
- 12.5 acre campus
- Modern laboratories
- Digital library
- Sports facilities
- Wi-Fi enabled campus
- Transportation service`,
            "What about transportation?": `### Transport Facilities
- College bus service
- Multiple routes in Hyderabad
- Professional drivers
- GPS tracking system`
        },
        "Placements": {
            "What is the placement record?": `### Placement Statistics 2024
- Highest Package: ₹51.03 LPA
- Average Package: ₹8.64 LPA
- Placement Rate: 69.58%
- 550 students placed`,
            "Which companies recruit?": `### Recruiting Companies
#### IT Giants
- Microsoft, Google, JP Morgan
- Infosys, TCS, Accenture
- Capgemini, Cognizant

#### Core Companies
- L&T, Carrier, Siemens
- Ashok Leyland

#### Other Notable Companies
- Amazon, Adobe, Flipkart
- EY India, PWC, Micron`
        }
    },
    faculty: {
        "Academic Policies": {
            "Who frames academic policies?": "The Academic Council is solely responsible for all academic matters, such as framing academic policy, approval of courses, regulations, and syllabus.",
            "Are faculty involved in decision-making?": "Yes, Faculty members are actively involved in the Academic Council.",
            "What is the role of HOD?": "The HOD is responsible for overseeing the department's academic and administrative functions, including curriculum planning, faculty coordination, and student performance monitoring.",
            "How is curriculum designed?": "The curriculum is designed by the Academic Council and periodically reviewed to align with industry standards.",
            "Are faculty involved in syllabus revision?": "Yes, faculty members participate in syllabus revision committees to ensure the curriculum remains relevant and comprehensive."
        },
        "Development & Research": {
            "What opportunities exist for development?": "GNITS organizes Faculty Development Programs (FDPs) and Short-Term Training Programs (STTPs) to enhance teaching skills and subject knowledge.",
            "Is research support available?": "Yes, GNITS encourages research by providing facilities and support for faculty to engage in research projects and publications.",
            "Can faculty guide Ph.D. students?": "Yes, faculty members with necessary qualifications and experience can guide Ph.D. students in their research endeavors.",
            "Are there collaboration opportunities?": "Yes, GNITS collaborates with various institutions and organizations to promote research and development activities."
        },
        "Teaching Resources": {
            "What teaching resources are available?": "GNITS provides access to digital classrooms, e-resources, and modern teaching aids to facilitate effective teaching.",
            "How is student performance monitored?": "Faculty members assess student performance through regular tests, assignments, and feedback mechanisms.",
            "Are there remedial classes?": "Yes, GNITS offers remedial classes to help students who need additional support in their studies.",
            "How is feedback collected?": "Feedback is collected through surveys, direct interactions, and online platforms to assess teaching effectiveness."
        },
        "Administrative Support": {
            "What administrative support is available?": "GNITS provides administrative support through various departments to assist faculty in their academic duties.",
            "Are there facilities for workshops?": "Yes, GNITS has well-equipped seminar halls and conference rooms to host workshops and seminars.",
            "Is there a faculty lounge?": "Yes, GNITS provides a faculty lounge for relaxation and informal discussions.",
            "How is workload determined?": "Faculty workload is determined based on courses assigned, student strength, and departmental requirements."
        }
    },
    visitor: {
        "About GNITS": {
            "What is GNITS?": "G. Narayanamma Institute of Technology and Science (GNITS) is an autonomous engineering college for women, located in Shaikpet, Hyderabad.",
            "Is it affiliated with any university?": "Yes, GNITS is affiliated with Jawaharlal Nehru Technological University Hyderabad (JNTUH).",
            "What is the history of GNITS?": "GNITS was established in 1997 by Sri G. Pulla Reddy to promote technical education among women.",
            "What accreditations does GNITS have?": "GNITS is accredited by NBA, NAAC (A+ grade), and is ISO 9001:2015 certified."
        },
        "Programs & Admissions": {
            "What undergraduate programs are offered?": `GNITS offers B.Tech in:
- Computer Science and Engineering
- Information Technology
- CSE (AI & ML)
- CSE (Data Science)
- Electronics and Communication
- Electrical and Electronics
- Electronics and Telematics`,
            "What postgraduate programs are offered?": `M.Tech programs in:
- Computer Science and Engineering
- Computer Networks & Information Security
- Digital Electronics and Communication
- Power Electronics & Electrical Drives
- Wireless & Mobile Communications`,
            "What is the admission process?": "Admissions are through TG-EAMCET for B.Tech and GATE/TS-PGECET for M.Tech programs."
        },
        "Campus & Facilities": {
            "Where is GNITS located?": "GNITS is located at Shaikpet, Hyderabad – 500104, Telangana.",
            "What is the campus size?": "GNITS campus spans 12.5 acres with a constructed area of 4,01,100 sq. ft.",
            "What facilities are available?": `Campus includes:
- Modern laboratories
- Digital library
- Sports facilities
- Hostel accommodation
- Transportation
- Wi-Fi enabled campus
- Health center`,
            "How to contact GNITS?": `Contact Information:
- Phone: +91-040-29565856
- Email: Principal@gnits.ac.in
- Website: https://gnits.ac.in`
        }
    }
};

function displayUserQueries(type) {
    const queryContainer = document.createElement('div');
    queryContainer.className = 'query-container';
    
    const backButton = document.createElement('button');
    backButton.className = 'back-btn';
    backButton.innerHTML = '<i class="fas fa-arrow-left"></i> Back';
    backButton.onclick = backToUserTypes;
    
    const queries = document.createElement('div');
    queries.className = 'query-buttons';
    
    // Generate buttons for each category
    Object.entries(faqDatabase[type]).forEach(([category, questions]) => {
        const categoryDiv = document.createElement('div');
        categoryDiv.className = 'category-section';
        categoryDiv.innerHTML = `
            <h5 class="category-title">${category}</h5>
            <div class="category-buttons">
                ${Object.keys(questions).map(q => `
                    <button class="query-btn" onclick="askQuestion('${q}')">
                        <i class="fas fa-question-circle"></i>
                        ${q}
                    </button>
                `).join('')}
            </div>
        `;
        queries.appendChild(categoryDiv);
    });
    
    queryContainer.appendChild(backButton);
    queryContainer.appendChild(queries);
    
    const chatMessages = document.getElementById('chatMessages');
    chatMessages.innerHTML = '';
    chatMessages.appendChild(queryContainer);
    
    addBotMessage("Please select your question or type your query.");
}

function askQuestion(question) {
    addUserMessage(question);
    
    let answer = "I'm sorry, I don't have specific information about that query.";
    
    if (currentUserType && faqDatabase[currentUserType]) {
        Object.values(faqDatabase[currentUserType]).forEach(category => {
            if (category[question]) {
                answer = category[question];
            }
        });
    }
    
    addBotMessage(answer);
}

function sendMessage() {
    const input = document.getElementById('userInput');
    const question = input.value.trim();
    
    if (question) {
        addUserMessage(question);
        const answer = processUserQuery(question);
        addBotMessage(answer);
        input.value = '';
    }
}

function processUserQuery(query) {
    query = query.toLowerCase().trim();

    // Keywords mapping for common queries
    const keywordMap = {
        'academic': {
            keywords: ['academic', 'syllabus', 'curriculum', 'semester', 'subjects', 'study material', 'course structure'],
            response: faqDatabase.student["Academic Curriculum"]["How to access the curriculum?"]
        },
        'placement': {
            keywords: ['placement', 'job', 'package', 'salary', 'company', 'recruit'],
            response: faqDatabase.student.Placements["What is the placement record?"]
        },
        'library': {
            keywords: ['library', 'book', 'reading', 'study material'],
            response: faqDatabase.student["Campus Life"]["Tell me about library facilities"]
        },
        'course': {
            keywords: ['course', 'branch', 'program', 'btech', 'mtech'],
            response: faqDatabase.student["Courses & Fees"]["What B.Tech Courses are offered?"]
        },
        'fee': {
            keywords: ['fee', 'cost', 'payment', 'charges'],
            response: faqDatabase.student["Courses & Fees"]["What is the fee structure?"]
        },
        'hostel': {
            keywords: ['hostel', 'accommodation', 'room', 'stay'],
            response: faqDatabase.parent["Hostel & Facilities"]["What are the hostel facilities?"]
        }
    };

    // Check for keyword matches
    for (const [category, info] of Object.entries(keywordMap)) {
        if (info.keywords.some(keyword => query.includes(keyword))) {
            return info.response;
        }
    }

    // If no direct match, search through all FAQ responses
    for (const userType in faqDatabase) {
        for (const category in faqDatabase[userType]) {
            for (const [question, answer] of Object.entries(faqDatabase[userType][category])) {
                if (question.toLowerCase().includes(query) || 
                    answer.toLowerCase().includes(query)) {
                    return answer;
                }
            }
        }
    }

    // If query contains college-related terms but no specific answer
    const collegeKeywords = ['gnits', 'college', 'university', 'institute', 'narayanamma'];
    if (collegeKeywords.some(keyword => query.includes(keyword))) {
        return `### I apologize!
I don't have specific information about that aspect of GNITS. You can:
1. Check the options above for related topics
2. Visit our [college website](https://gnits.ac.in) for detailed information
3. Try rephrasing your question`;
    }

    // Default response for unrelated queries
    return `### I'm here to help!
I can provide information about:
- Admissions and eligibility
- Courses and programs
- Fee structure
- Placements
- Campus facilities
- Hostel accommodation

Please try asking about these topics or select from the options above.`;
}

// Handle Enter key in input
document.getElementById('userInput').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

// Initialize chatbot with welcome message
window.onload = function() {
    addBotMessage("Welcome to GNITS FAQ Assistant! Please select your category to get started.");
};
