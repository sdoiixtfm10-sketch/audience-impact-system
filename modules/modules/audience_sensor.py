import time
import json
import random
from datetime import datetime
from typing import Dict, List

class AudienceSensor:
    """Collects real-time crowd metrics"""
    
    def __init__(self):
        self.data_points = []
        self.start_time = datetime.now()
    
    def get_crowd_energy(self) -> float:
        """
        Measure crowd energy (0-100)
        Sources: noise level, chants, movement patterns
        """
        # In production, this integrates with actual sensors
        # For demo: simulates energy spikes during key moments
        energy = random.uniform(50, 95)
        return round(energy, 2)
    
    def get_crowd_size(self) -> int:
        """Get estimated crowd attendance"""
        return random.randint(15000, 80000)
    
    def get_noise_level(self) -> float:
        """Measure ambient noise in decibels"""
        return round(random.uniform(70, 110), 2)
    
    def get_movement_intensity(self) -> float:
        """Measure crowd movement/activity (0-100)"""
        return round(random.uniform(30, 100), 2)
    
    def capture_snapshot(self) -> Dict:
        """Capture complete audience state"""
        return {
            'timestamp': datetime.now().isoformat(),
            'crowd_energy': self.get_crowd_energy(),
            'crowd_size': self.get_crowd_size(),
            'noise_level': self.get_noise_level(),
            'movement_intensity': self.get_movement_intensity(),
            'elapsed_seconds': (datetime.now() - self.start_time).total_seconds()
        }
    
    def collect_batch(self, count: int = 10) -> List[Dict]:
        """Collect multiple snapshots"""
        batch = [self.capture_snapshot() for _ in range(count)]
        self.data_points.extend(batch)
        return batch
