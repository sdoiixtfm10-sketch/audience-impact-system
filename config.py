import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configuration for the audience impact system"""
    
    # API Settings
    API_HOST = os.getenv('API_HOST', '0.0.0.0')
    API_PORT = int(os.getenv('API_PORT', 5000))
    
    # Data Collection
    SENSOR_UPDATE_INTERVAL = 1  # seconds
    BUFFER_SIZE = 1000  # data points per minute
    
    # Thresholds
    ENERGY_THRESHOLD = 70  # 0-100 scale
    SENTIMENT_THRESHOLD = 0.5  # -1 to 1 scale
    
    # Storage
    DATA_DIR = 'data/matches/'
    LOG_FILE = 'logs/system.log'
