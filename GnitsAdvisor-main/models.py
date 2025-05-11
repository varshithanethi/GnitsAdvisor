"""
Database models for the GNITS College Chat Assistant
"""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ChatUser(db.Model):
    """Store user information and preferences"""
    __tablename__ = 'chat_users'
    
    id = db.Column(db.Integer, primary_key=True)
    user_type = db.Column(db.String(20), nullable=False, default='general')  # student, faculty, parent, general
    session_id = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_active_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationship
    chat_messages = db.relationship('ChatMessage', backref='user', lazy=True, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<ChatUser {self.id}, type={self.user_type}>'


class ChatMessage(db.Model):
    """Store chat messages history"""
    __tablename__ = 'chat_messages'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('chat_users.id'), nullable=False)
    message_type = db.Column(db.String(10), nullable=False)  # 'user' or 'bot'
    content = db.Column(db.Text, nullable=False)
    topic = db.Column(db.String(50), nullable=True)  # The topic/category of the message
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<ChatMessage {self.id}, type={self.message_type}, topic={self.topic}>'


class FAQ(db.Model):
    """Store frequently asked questions and answers"""
    __tablename__ = 'faqs'
    
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(255), nullable=False)
    answer = db.Column(db.Text, nullable=False)
    user_type = db.Column(db.String(20), nullable=False, default='general')  # student, faculty, parent, general
    category = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<FAQ {self.id}, for={self.user_type}, category={self.category}>'


class CollegeResource(db.Model):
    """Store college resources like images, documents, etc."""
    __tablename__ = 'resources'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    resource_type = db.Column(db.String(20), nullable=False)  # image, document, link, etc.
    url = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<CollegeResource {self.id}, type={self.resource_type}, name={self.name}>'