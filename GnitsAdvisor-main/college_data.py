"""
Module to store and manage college data for GNITS
"""

import json
import os
from web_scraper import get_website_text_content

# URLs to scrape
GNITS_URLS = {
    "home": "https://www.gnits.ac.in/",
    "about": "https://www.gnits.ac.in/?page_id=35",
    "departments": "https://www.gnits.ac.in/?page_id=39",
    "admissions": "https://www.gnits.ac.in/?page_id=52",
    "placements": "https://www.gnits.ac.in/?page_id=45",
    "facilities": "https://www.gnits.ac.in/?page_id=47",
    "contact": "https://www.gnits.ac.in/?page_id=14"
}

# Path to cache file
CACHE_FILE = "gnits_data_cache.json"

# College image URLs - Using actual GNITS college images
COLLEGE_IMAGES = [
    "https://www.gnits.ac.in/wp-content/themes/education-hub/images/slider1.jpg",
    "https://www.gnits.ac.in/wp-content/themes/education-hub/images/slider2.jpg",
    "https://www.gnits.ac.in/wp-content/themes/education-hub/images/slider3.jpg",
    "https://www.gnits.ac.in/wp-content/themes/education-hub/images/gallery/1.jpg",
    "https://www.gnits.ac.in/wp-content/themes/education-hub/images/gallery/2.jpg",
    "https://www.gnits.ac.in/wp-content/themes/education-hub/images/gallery/3.jpg",
    "https://www.gnits.ac.in/wp-content/themes/education-hub/images/gallery/4.jpg",
    "https://www.gnits.ac.in/wp-content/themes/education-hub/images/gallery/5.jpg"
]

# Campus images (subset of college images)
CAMPUS_IMAGES = [
    "https://www.gnits.ac.in/wp-content/themes/education-hub/images/slider1.jpg",
    "https://www.gnits.ac.in/wp-content/themes/education-hub/images/gallery/1.jpg",
    "https://www.gnits.ac.in/wp-content/themes/education-hub/images/gallery/3.jpg",
    "https://www.gnits.ac.in/wp-content/themes/education-hub/images/gallery/5.jpg"
]

# College basic info
COLLEGE_INFO = {
    "name": "G. Narayanamma Institute of Technology and Science",
    "short_name": "GNITS",
    "established": "1997",
    "type": "Women's Engineering College",
    "affiliation": "Jawaharlal Nehru Technological University, Hyderabad",
    "location": "Shaikpet, Hyderabad, Telangana, India",
    "website": "https://www.gnits.ac.in/",
    "courses": {
        "btech": [
            "Computer Science and Engineering",
            "Computer Science & Engineering (Artificial Intelligence & Machine Learning)",
            "Computer Science & Engineering (Data Science)",
            "Computer Science and Technology",
            "Information Technology",
            "Electronics and Communication Engineering",
            "Electrical and Electronics Engineering",
            "Electronics and Telematics Engineering"
        ],
        "mtech": [
            "Computer Science and Engineering (CSE)",
            "Computer Networks & Information Security (IT)",
            "Digital Electronics and Comm. System (ECE)",
            "Power Electronics & Electric Drives (EEE)",
            "Wireless & Mobile Communications (ETE)"
        ]
    },
    "departments": [
        "Computer Science and Engineering",
        "Information Technology",
        "Electronics and Communication Engineering",
        "Electrical and Electronics Engineering",
        "Electronics and Telematics Engineering",
        "Artificial Intelligence and Data Science"
    ],
    "hostel": {
        "description": "Our hostels are designed to be more than just a place to stay—they are a vibrant community that fosters learning, friendship, and well-being. Managed by the esteemed G. Pulla Reddy Charities Trust, our hostels are an extension of GNITS's commitment to empowering women through education.",
        "facilities": "Each hostel is thoughtfully equipped with all the modern amenities you need to thrive during your time here. From cozy, well-furnished rooms to nutritious meals prepared with care, our facilities ensure that you can focus on your studies and extracurricular activities without any worries.",
        "capacity": "218 rooms with a strength of 1037 students"
    },
    "sports": {
        "outdoor": [
            "Volley Ball",
            "Basket Ball",
            "Throw Ball",
            "Hand Ball",
            "KhoKho",
            "Kabaddi"
        ],
        "indoor": [
            "Indoor Gym",
            "Carroms",
            "Table Tennis",
            "Badminton",
            "Chess"
        ]
    },
    "clubs": {
        "cultural": [
            "Soaring Beyond Boundaries - Samskruthi",
            "Where Words Become Worlds - Litereria Clava",
            "Your Passion, Our Platform - Artista",
            "Symphony to Your Soul - Suswara"
        ],
        "community": [
            "NSS",
            "Rotaract Club",
            "Street Cause",
            "Abhaya",
            "Aarambh"
        ]
    },
    "placements": {
        "highest_package": "51.03 LPA",
        "placement_percentage": "~69.58%",
        "average_salary": "8.64 LPA",
        "top_recruiters": [
            "Microsoft: A global leader in software, services, and solutions",
            "Adobe: Renowned for its multimedia and creativity software products",
            "Amazon: A multinational technology company focusing on e-commerce, cloud computing, and artificial intelligence",
            "Visa: A world leader in digital payments",
            "Deloitte: One of the 'Big Four' accounting organizations, offering audit, consulting, tax, and advisory services",
            "TCS (Tata Consultancy Services): A leading global IT services, consulting, and business solutions organization",
            "Accenture: A multinational professional services company specializing in IT services and consulting",
            "Bank of America: One of the world's largest financial institutions"
        ]
    }
}

def get_or_create_college_data():
    """
    Load college data from cache if available, otherwise scrape from website
    """
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, 'r') as f:
                data = json.load(f)
                return data
        except Exception as e:
            print(f"Error loading cache: {e}")
    
    # Scrape data if cache not available
    data = {
        "basic_info": COLLEGE_INFO,
        "college_images": COLLEGE_IMAGES,
        "campus_images": CAMPUS_IMAGES
    }
    
    # Scrape content from the website
    scraped_data = {}
    for key, url in GNITS_URLS.items():
        try:
            content = get_website_text_content(url)
            scraped_data[key] = content
        except Exception as e:
            print(f"Error scraping {key} from {url}: {e}")
            scraped_data[key] = f"Information temporarily unavailable. Please visit {url} for details."
    
    data["scraped"] = scraped_data
    
    # Save to cache
    try:
        with open(CACHE_FILE, 'w') as f:
            json.dump(data, f)
    except Exception as e:
        print(f"Error saving cache: {e}")
    
    return data

# User-specific options based on user type
USER_TYPE_OPTIONS = {
    "student": [
        {"id": "about", "text": "About GNITS"},
        {"id": "courses", "text": "Academic Programs"},
        {"id": "hostel", "text": "Student Hostel"},
        {"id": "facilities", "text": "Campus Facilities"},
        {"id": "campus_life", "text": "Campus Life"},
        {"id": "sports", "text": "Sports & Recreation"},
        {"id": "clubs", "text": "Student Clubs"},
        {"id": "placements", "text": "Placements & Internships"},
        {"id": "scholarships", "text": "Scholarships & Financial Aid"},
        {"id": "exam_schedule", "text": "Exam Schedule"},
        {"id": "contact", "text": "Contact Information"}
    ],
    "faculty": [
        {"id": "about", "text": "About GNITS"},
        {"id": "departments", "text": "Departments & Research"},
        {"id": "facilities", "text": "Campus Facilities"},
        {"id": "research_grants", "text": "Research Grants"},
        {"id": "faculty_development", "text": "Faculty Development Programs"},
        {"id": "achievements", "text": "College Achievements"},
        {"id": "academic_calendar", "text": "Academic Calendar"},
        {"id": "contact", "text": "Contact Information"}
    ],
    "parent": [
        {"id": "about", "text": "About GNITS"},
        {"id": "admissions", "text": "Admissions Process"},
        {"id": "fees", "text": "Fees Structure"},
        {"id": "hostel", "text": "Student Hostel"},
        {"id": "facilities", "text": "Campus Facilities & Safety"},
        {"id": "placements", "text": "Placement Records"},
        {"id": "campus_life", "text": "Campus Life"},
        {"id": "scholarships", "text": "Scholarships & Financial Aid"},
        {"id": "parent_portal", "text": "Parent Portal Information"},
        {"id": "contact", "text": "Contact Information"}
    ],
    "general": [
        {"id": "about", "text": "About GNITS"},
        {"id": "courses", "text": "Academic Programs"},
        {"id": "admissions", "text": "Admissions"},
        {"id": "facilities", "text": "Campus Facilities"},
        {"id": "hostel", "text": "Student Hostel"},
        {"id": "sports", "text": "Sports & Recreation"},
        {"id": "clubs", "text": "Student Clubs"},
        {"id": "placements", "text": "Placements"},
        {"id": "campus_life", "text": "Campus Life"},
        {"id": "achievements", "text": "Achievements"},
        {"id": "contact", "text": "Contact Information"}
    ]
}

# Function to get options based on user type
def get_user_type_options(user_type):
    """Return options specific to the user type"""
    return USER_TYPE_OPTIONS.get(user_type, USER_TYPE_OPTIONS["general"])

# Function to generate responses based on user query
def get_college_response(query_type, user_type="general"):
    """
    Generate a response based on the query type and user type.
    """
    data = get_or_create_college_data()
    scraped = data.get("scraped", {})
    
    # Common responses for all user types
    common_responses = {
        "about": {
            "title": "About GNITS",
            "content": scrape_summary(scraped.get("about", ""), 
                       "G. Narayanamma Institute of Technology and Science (GNITS), established in 1997, is one of the most prestigious institutions "
                       "dedicated to empowering women in engineering and technology. Located in Hyderabad, Telangana, GNITS is affiliated with "
                       "Jawaharlal Nehru Technological University, Hyderabad (JNTUH), and is approved by the All India Council for Technical Education (AICTE). "
                       "The mission of GNITS is to provide a transformative educational experience, equipping women with the knowledge, skills, and values "
                       "necessary to excel in engineering. GNITS envisions itself as a center of excellence, fostering technical education, research, innovation, "
                       "and leadership among women."),
            "image": data["college_images"][0]
        },
        "courses": {
            "title": "Academic Programs",
            "content": format_list("Courses Offered at GNITS:", data["basic_info"]["courses"]) + "\n\n" + 
                       format_list("Departments:", data["basic_info"]["departments"]),
            "image": data["college_images"][1]
        },
        "admissions": {
            "title": "Admissions",
            "content": scrape_summary(scraped.get("admissions", ""), 
                       "Admissions to GNITS are based on state-level entrance examinations. "
                       "For B.Tech programs, admissions are through the TS EAMCET counseling. "
                       "For M.Tech programs, GATE scores and state-level PGECET are considered. "
                       "MBA admissions are through ICET. The institute also has lateral entry options "
                       "for diploma holders entering B.Tech programs directly in the second year."),
            "image": data["college_images"][2]
        },
        "facilities": {
            "title": "Campus Facilities",
            "content": scrape_summary(scraped.get("facilities", ""), 
                       "GNITS offers modern facilities including well-equipped laboratories, digital classrooms, "
                       "central library with extensive collection of books and journals, computer centers, "
                       "sports facilities, gymnasium, auditorium, seminar halls, canteen, medical center, "
                       "transportation services, and separate hostels for outstation students."),
            "image": data["campus_images"][1]
        },
        "placements": {
            "title": "Placements",
            "content": f"GNITS has an impressive placement record with many top companies visiting the campus for recruitment.\n\n"
                       f"• Highest Package: {data['basic_info']['placements']['highest_package']}\n"
                       f"• Placement Percentage: {data['basic_info']['placements']['placement_percentage']}\n"
                       f"• Average Salary: {data['basic_info']['placements']['average_salary']}\n\n"
                       f"Top Recruiters:\n" +
                       "\n".join([f"• {company}" for company in data['basic_info']['placements']['top_recruiters'][:5]]) +
                       "\n\nThe Training and Placement Cell provides pre-placement training to help students prepare for campus interviews.",
            "image": data["college_images"][3]
        },
        "hostel": {
            "title": "Student Hostel",
            "content": f"Your Home Away from Home\n\n"
                       f"{data['basic_info']['hostel']['description']}\n\n"
                       f"{data['basic_info']['hostel']['facilities']}\n\n"
                       f"Capacity: {data['basic_info']['hostel']['capacity']}",
            "image": data["campus_images"][1]
        },
        "sports": {
            "title": "Sports & Recreation",
            "content": "GNITS offers excellent sports facilities to encourage students to maintain physical fitness and develop team spirit.\n\n"
                       "Outdoor Sports:\n" +
                       "\n".join([f"• {sport}" for sport in data['basic_info']['sports']['outdoor']]) +
                       "\n\nIndoor Sports:\n" +
                       "\n".join([f"• {sport}" for sport in data['basic_info']['sports']['indoor']]) +
                       "\n\nThe Department of Physical Education organizes various inter-college and intra-college sports events throughout the academic year.",
            "image": data["campus_images"][3]
        },
        "clubs": {
            "title": "Student Clubs",
            "content": "GNITS has a vibrant ecosystem of student clubs that provide opportunities for personal growth and skill development.\n\n"
                       "Cultural Clubs:\n" +
                       "\n".join([f"• {club}" for club in data['basic_info']['clubs']['cultural']]) +
                       "\n\nCommunity Service Clubs:\n" +
                       "\n".join([f"• {club}" for club in data['basic_info']['clubs']['community']]) +
                       "\n\nThese clubs regularly organize events, workshops, and community service activities to enrich campus life.",
            "image": data["campus_images"][2]
        },
        "campus_life": {
            "title": "Campus Life",
            "content": "Life at GNITS is vibrant and full of energy, offering students a dynamic and supportive environment. "
                       "The campus is equipped with state-of-the-art infrastructure that fosters both academic excellence and personal growth. "
                       "Active student communities promote a wide range of co-curricular and recreational activities. "
                       "National-level events and festivals on campus provide opportunities for students to pursue their ambitions, "
                       "enhance their skills, and explore new interests.",
            "image": data["campus_images"][2]
        },
        "contact": {
            "title": "Contact Information",
            "content": scrape_summary(scraped.get("contact", ""), 
                       "G. Narayanamma Institute of Technology and Science (For Women)\n"
                       "Shaikpet, Hyderabad - 500104, Telangana, India\n"
                       "Phone: +91-40-23565648, 23567780\n"
                       "Email: principal@gnits.ac.in, info@gnits.ac.in\n"
                       "Website: www.gnits.ac.in"),
            "image": data["college_images"][4]
        },
        "achievements": {
            "title": "Achievements",
            "content": "GNITS has been recognized for its academic excellence and contributions to technical education. "
                       "The institute received 'A' grade accreditation from NAAC and most of its eligible programs are "
                       "accredited by NBA. Students have consistently excelled in academics and extracurricular activities, "
                       "winning awards at national and international competitions. The college has also been ranked among "
                       "the top engineering colleges in India by various ranking agencies.",
            "image": data["college_images"][5]
        }
    }
    
    # User-specific responses
    student_responses = {
        "scholarships": {
            "title": "Scholarships & Financial Aid",
            "content": "GNITS offers various scholarships and financial aid options for deserving students:\n\n"
                       "• Merit Scholarships: For students with excellent academic performance\n"
                       "• Government Scholarships: SC/ST/BC/EBC scholarships from state and central governments\n"
                       "• Fee Waivers: For economically disadvantaged but academically bright students\n"
                       "• Corporate Scholarships: Sponsored by various companies and industry partners\n\n"
                       "Students can apply for these scholarships through the college administration office with "
                       "the required documentation. The scholarship committee reviews applications and awards based on eligibility.",
            "image": data["college_images"][6]
        },
        "exam_schedule": {
            "title": "Exam Schedule",
            "content": "The current semester examination schedule is now available.\n\n"
                       "Mid-semester examinations will be held from the 2nd to 7th of next month. End-semester examinations "
                       "are scheduled to begin on the 10th of the month after next.\n\n"
                       "All students are advised to check the detailed schedule posted on the department notice boards "
                       "and on the college website student portal. For any exam-related queries, please contact "
                       "the examination section at exams@gnits.ac.in.",
            "image": data["college_images"][7]
        }
    }
    
    faculty_responses = {
        "departments": {
            "title": "Departments & Research",
            "content": format_list("Academic Departments:", data["basic_info"]["departments"]) + "\n\n"
                       "Each department at GNITS is engaged in cutting-edge research in their respective fields. "
                       "The college encourages interdisciplinary research collaborations and provides "
                       "research infrastructure including specialized laboratories and computing facilities. "
                       "Faculty members regularly publish research papers in reputed journals and present at international conferences.",
            "image": data["college_images"][1]
        },
        "research_grants": {
            "title": "Research Grants",
            "content": "GNITS faculty have secured numerous research grants from organizations like DST, AICTE, UGC, and industry partners. "
                       "The Research & Development cell facilitates grant applications and project management. "
                       "Currently active research areas include AI & Machine Learning, IoT, Renewable Energy, Structural Engineering, "
                       "Communication Systems, and Data Analytics.\n\n"
                       "For assistance with research grant applications, please contact the R&D cell at rnd@gnits.ac.in.",
            "image": data["college_images"][3]
        },
        "faculty_development": {
            "title": "Faculty Development Programs",
            "content": "GNITS regularly organizes Faculty Development Programs (FDPs) to enhance teaching methodologies "
                       "and research capabilities. Upcoming FDPs include:\n\n"
                       "• Workshop on Outcome-Based Education (June 15-16)\n"
                       "• Research Methodology and Paper Writing (July 10-14)\n"
                       "• AI & Machine Learning Applications (August 5-10)\n\n"
                       "Faculty members can register for these programs through the college portal. "
                       "For external FDPs, applications for financial support can be submitted to the Principal's office.",
            "image": data["college_images"][4]
        },
        "academic_calendar": {
            "title": "Academic Calendar",
            "content": "The academic calendar for the current year is as follows:\n\n"
                       "• Odd Semester: July to December\n"
                       "• Even Semester: January to May\n"
                       "• Mid-semester breaks: First week of October & First week of March\n"
                       "• Semester end exams: First two weeks of December & Last two weeks of May\n\n"
                       "Faculty members are requested to plan their academic activities and leave accordingly. "
                       "The detailed calendar is available on the faculty portal.",
            "image": data["college_images"][2]
        }
    }
    
    parent_responses = {
        "fees": {
            "title": "Fees Structure",
            "content": "The fee structure for various programs at GNITS is as follows:\n\n"
                       "• B.Tech: Rs. 1,20,000 per annum\n"
                       "• M.Tech: Rs. 95,000 per annum\n"
                       "• MBA: Rs. 85,000 per annum\n\n"
                       "Additional charges include:\n"
                       "• One-time admission fee: Rs. 5,000\n"
                       "• Library deposit (refundable): Rs. 3,000\n"
                       "• Hostel fees (if applicable): Rs. 75,000 per annum\n\n"
                       "Fees can be paid online through the college portal or via DD in favor of 'GNITS' payable at Hyderabad.",
            "image": data["college_images"][4]
        },
        "parent_portal": {
            "title": "Parent Portal Information",
            "content": "GNITS provides a dedicated parent portal to keep parents informed about their ward's academic progress.\n\n"
                       "Through the portal, parents can access:\n"
                       "• Attendance records\n"
                       "• Examination results\n"
                       "• Fee payment details\n"
                       "• Important notices and circulars\n\n"
                       "Login credentials for the parent portal are shared during the admission process. "
                       "For login issues, please contact the IT support team at itsupport@gnits.ac.in or call 040-23565648 ext. 123.",
            "image": data["college_images"][5]
        }
    }
    
    # Combine responses based on user type
    all_responses = common_responses.copy()
    if user_type == "student":
        all_responses.update(student_responses)
    elif user_type == "faculty":
        all_responses.update(faculty_responses)
    elif user_type == "parent":
        all_responses.update(parent_responses)
    
    return all_responses.get(query_type, {"title": "GNITS", "content": "Welcome to GNITS Chat Assistant! Please select a topic to learn more about our college.", "image": data["college_images"][0]})

def scrape_summary(scraped_text, fallback_text):
    """Return the scraped text if it's substantial, otherwise return the fallback"""
    if scraped_text and len(scraped_text) > 100:  # Check if scraped text is meaningful
        return clean_scraped_text(scraped_text)
    return fallback_text

def clean_scraped_text(text):
    """Clean and format the scraped text to be more readable"""
    if not text:
        return ""
    
    # Get first 1500 characters to avoid too lengthy responses
    text = text[:1500]
    
    # Basic cleaning
    text = text.replace('\n\n', '\n').strip()
    
    return text

def format_list(title, items):
    """Format a list of items with a title"""
    if not items:
        return title + " No information available"
    
    if isinstance(items, list):
        result = title + "\n"
        for item in items:
            result += f"• {item}\n"
        return result
    elif isinstance(items, dict):
        # Handle nested dictionaries like courses with btech and mtech
        result = title + "\n"
        for key, values in items.items():
            key_title = key.upper() if len(key) <= 5 else key.title()
            result += f"\n{key_title} Programs:\n"
            for item in values:
                result += f"• {item}\n"
        return result
    return title + "\n" + str(items)
