import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime
import logging
import pytz

class GNITSDataFetcher:
    def __init__(self):
        self.base_url = "https://www.gnits.ac.in"
        self.cache_dir = "data"
        self.cache_file = os.path.join(self.cache_dir, "gnits_data_cache.json")
        self.logger = logging.getLogger(__name__)
        
        # Create cache directory if it doesn't exist
        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)
        
        self.load_cache()

    def load_cache(self):
        try:
            with open(self.cache_file, 'r') as f:
                self.cache = json.load(f)
        except FileNotFoundError:
            self.cache = {
                'last_updated': None,
                'faq_data': {}
            }

    def fetch_placements(self):
        try:
            response = requests.get(f"{self.base_url}/placements")
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                # Update these selectors based on GNITS website structure
                stats = {
                    "highest_package": self._extract_text(soup, ".highest-package"),
                    "average_package": self._extract_text(soup, ".average-package"),
                    "placement_percentage": self._extract_text(soup, ".placement-percentage"),
                    "companies_visited": self._extract_list(soup, ".company-list")
                }
                return stats
        except Exception as e:
            self.logger.error(f"Error fetching placement data: {str(e)}")
        return None

    def fetch_news(self):
        try:
            response = requests.get(f"{self.base_url}/news")
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                news_items = soup.select(".news-item")
                return [item.text.strip() for item in news_items]
        except Exception as e:
            self.logger.error(f"Error fetching news: {str(e)}")
        return []

    def update_faq_data(self):
        """Update FAQ data cache"""
        try:
            # Update last_updated timestamp
            self.cache['last_updated'] = datetime.now(pytz.timezone('Asia/Kolkata')).isoformat()
            
            # Save to cache file
            with open(self.cache_file, 'w') as f:
                json.dump(self.cache, f, indent=4)
            
            self.logger.info("FAQ data updated successfully")
            return True
        except Exception as e:
            self.logger.error(f"Error updating FAQ data: {str(e)}")
            return False

    def log_chat_message(self, app, user_type, message, response):
        """Log chat messages to PostgreSQL database with enhanced logging"""
        try:
            from flask_app import db, ChatMessage
            
            # Validate input parameters
            if not all([user_type, message, response]):
                raise ValueError("Missing required parameters")

            # Create chat message
            chat_message = ChatMessage(
                user_type=user_type,
                message=message,
                response=response
            )

            # Save to database with context management
            with app.app_context():
                db.session.add(chat_message)
                db.session.commit()
                
                # Log successful insertion
                self.logger.info(
                    f"Chat message logged successfully:\n"
                    f"User Type: {user_type}\n"
                    f"Message: {message[:50]}...\n"
                    f"Response: {response[:50]}..."
                )
                
                # Return message ID for tracking
                return chat_message.id

        except ValueError as ve:
            self.logger.error(f"Validation error: {str(ve)}")
            return None
        except Exception as e:
            self.logger.error(f"Database error: {str(e)}")
            return None

    def get_response(self, query, user_type):
        """Get response for a given query"""
        # Add your response logic here
        return "I'm sorry, I don't have specific information about that query."

    def _extract_text(self, soup, selector):
        element = soup.select_one(selector)
        return element.text.strip() if element else ""

    def _extract_list(self, soup, selector):
        elements = soup.select(selector)
        return [el.text.strip() for el in elements]