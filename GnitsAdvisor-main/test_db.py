from flask_app import app, db, ChatMessage
from services.data_fetcher import GNITSDataFetcher
from datetime import datetime
import sys

def print_success(message):
    print(f"\033[92m✓\033[0m {message}")

def print_error(message):
    print(f"\033[91m❌\033[0m {message}")

def test_database_connection():
    try:
        with app.app_context():
            print("\n=== Testing PostgreSQL Database Connection ===")
            
            # Test 1: Create message
            chat_message = ChatMessage(
                user_type="test",
                message="Database test message",
                response="Database connection successful",
                timestamp=datetime.utcnow()
            )
            db.session.add(chat_message)
            db.session.commit()
            print_success(f"Test 1: Message created with ID: {chat_message.id}")
            
            # Test 2: Read message
            result = db.session.get(ChatMessage, chat_message.id)
            assert result.message == "Database test message"
            print_success("Test 2: Message retrieved successfully")
            
            # Test 3: Query all messages
            all_messages = db.session.query(ChatMessage).all()
            print_success(f"Test 3: Found {len(all_messages)} total messages")
            
            # Test 4: Query by user type
            test_messages = db.session.query(ChatMessage)\
                .filter_by(user_type="test")\
                .all()
            print_success(f"Test 4: Found {len(test_messages)} test messages")
            
            # Test 5: Recent messages
            recent = db.session.query(ChatMessage)\
                .order_by(ChatMessage.timestamp.desc())\
                .limit(3)\
                .all()
            print_success(f"Test 5: Recent messages check successful")
            
            # Test 6: Message update
            if recent and len(recent) > 0:
                test_msg = recent[0]
                old_response = test_msg.response
                test_msg.response = "Updated response"
                db.session.commit()
                updated_msg = db.session.get(ChatMessage, test_msg.id)
                assert updated_msg.response == "Updated response"
                # Restore original response
                test_msg.response = old_response
                db.session.commit()
                print_success("Test 6: Message update successful")

            # Test 7: Database connection stability
            connection = db.engine.connect()
            connection.close()
            print_success("Test 7: Database connection stability verified")

            print("\nDatabase Summary:")
            print(f"Total messages: {len(all_messages)}")
            print(f"Test messages: {len(test_messages)}")
            print(f"Most recent message ID: {recent[0].id}")
            print(f"Database URL: {app.config['SQLALCHEMY_DATABASE_URI'].split('@')[1]}")
            
            return True
            
    except Exception as e:
        print_error(f"Database test failed: {str(e)}")
        return False

if __name__ == "__main__":
    success = test_database_connection()
    print(f"\nOverall test {'succeeded' if success else 'failed'}")