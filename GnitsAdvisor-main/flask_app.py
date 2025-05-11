from flask import Flask, render_template, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv
import os
import logging
from werkzeug.middleware.proxy_fix import ProxyFix
from services.data_fetcher import GNITSDataFetcher
from flask_apscheduler import APScheduler
from datetime import datetime
import pytz
import json

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__, static_url_path='/static')
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1)

# Security configurations
app.secret_key = os.getenv("SECRET_KEY", "gnits-chat-assistant-secret")
app.config["SESSION_COOKIE_SECURE"] = True
app.config["SESSION_COOKIE_HTTPONLY"] = True
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"

# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "postgresql://username:password@localhost:5432/gnits_db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Scheduler configuration
app.config['SCHEDULER_TIMEZONE'] = 'Asia/Kolkata'
scheduler = APScheduler()
scheduler.init_app(app)

# Initialize database
db = SQLAlchemy(app)

# Database Model
class ChatMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_message = db.Column(db.String(500), nullable=False)
    bot_response = db.Column(db.String(500), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.now(pytz.timezone('Asia/Kolkata')))

# Initialize CORS
CORS(app, resources={
    r"/*": {
        "origins": ["https://gnits.ac.in", "http://localhost:5000", "https://your-app-name.herokuapp.com"],
        "methods": ["GET", "POST"],
        "allow_headers": ["Content-Type"]
    }
})

# Initialize data fetcher
data_fetcher = GNITSDataFetcher()

# Your existing FAQ_RESPONSES dictionary here
FAQ_RESPONSES = {
    "student": {
        "admission": {
            "What are the eligibility criteria?": """
### B.Tech Admission Requirements
- Completed 10+2 with PCM subjects
- Qualify in TG-EAMCET examination
- Merit-based admission through counseling
- AICTE approved program
            """,
            "How to apply?": """
### Application Process
1. Qualify in TG-EAMCET
2. Attend counseling by TSCHE
3. Choose GNITS based on rank
4. Complete admission formalities
            """
        },
        "courses": {
            "What courses are offered?": """
### B.Tech Programs
- Computer Science and Engineering (CSE)
- Information Technology (IT)
- Electronics and Communication Engineering (ECE)
- Electrical and Electronics Engineering (EEE)
- Electronics and Telematics Engineering (ETM)
- CSE (AI & ML)
- CSE (Data Science)

### M.Tech Programs
- Computer Science and Engineering
- Computer Networks & Information Security
- Digital Electronics and Communication
- Power Electronics & Electric Drives
- Wireless & Mobile Communications
            """,
            "What is the fee structure?": """
### Fee Structure 2023-24
- Category A & B (JEE): ₹1,00,000/year
- Category B (NRI): USD 5,000/year
- Additional JNTUH fees applicable
            """
        }
    }
    # Add other categories similarly
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    data = request.json
    query = data.get('query', '').lower()
    user_type = data.get('user_type', 'general')
    
    response = "I'm sorry, I don't have specific information about that query."
    
    if user_type in FAQ_RESPONSES:
        for category in FAQ_RESPONSES[user_type]:
            for question, answer in FAQ_RESPONSES[user_type][category].items():
                if query.lower() in question.lower():
                    response = answer
                    break
    
    return jsonify({
        "content": response,
        "type": "markdown"
    })

@app.route('/data_status')
def data_status():
    try:
        with open(data_fetcher.cache_file) as f:
            cache = json.load(f)
        return jsonify({
            "status": "success",
            "last_updated": cache['last_updated']
        })
    except:
        return jsonify({
            "status": "error",
            "message": "Could not retrieve update status"
        })

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    response = "I'm sorry, I don't have specific information about that query."
    
    # Save chat message to database
    chat_message = ChatMessage(user_message=user_message, bot_response=response)
    db.session.add(chat_message)
    db.session.commit()
    
    return jsonify({
        "user_message": user_message,
        "bot_response": response
    })

# Schedule FAQ data update
@scheduler.task('interval', id='update_faq', hours=24, timezone='Asia/Kolkata')
def update_faq_data():
    with app.app_context():
        data_fetcher.update_faq_data()

if __name__ == '__main__':
    try:
        # Initialize database
        with app.app_context():
            db.create_all()
        
        # Initial data fetch
        data_fetcher.update_faq_data()
        
        # Server configuration
        port = int(os.environ.get("PORT", 8080))  # Changed to use environment variable
        host = '0.0.0.0'  # Allow external connections
        
        # Print access URLs
        print("\n=== GNITS FAQ Assistant Server ===")
        print(f"Local access: http://localhost:{port}")
        print(f"Network access: http://10.10.8.52:{port}")
        print("Press CTRL+C to quit\n")
        
        # Start scheduler
        scheduler.start()
        
        # Run the server
        app.run(
            host=host,
            port=port,
            debug=True,
            threaded=True,
            use_reloader=True
        )
    except Exception as e:
        print(f"\nError starting server: {str(e)}")