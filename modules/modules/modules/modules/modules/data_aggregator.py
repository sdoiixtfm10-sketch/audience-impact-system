import json
import pandas as pd
from typing import Dict, List
from datetime import datetime

class DataAggregator:
    """Aggregates and processes all audience data"""
    
    def __init__(self):
        self.all_data = {
            'sensors': [],
            'sentiment': [],
            'performance': []
        }
    
    def add_sensor_data(self, data: List[Dict]):
        """Add sensor readings"""
        self.all_data['sensors'].extend(data)
    
    def add_sentiment_data(self, data: Dict):
        """Add sentiment analysis"""
        self.all_data['sentiment'].append(data)
    
    def add_performance_data(self, data: Dict):
        """Add performance correlations"""
        self.all_data['performance'].append(data)
    
    def get_summary(self) -> Dict:
        """Get high-level summary of all data"""
        sensor_count = len(self.all_data['sensors'])
        
        if sensor_count > 0:
            energies = [s['crowd_energy'] for s in self.all_data['sensors']]
            avg_energy = sum(energies) / len(energies)
        else:
            avg_energy = 0
        
        return {
            'timestamp': datetime.now().isoformat(),
            'total_sensor_readings': sensor_count,
            'average_crowd_energy': round(avg_energy, 2),
            'sentiment_analyses': len(self.all_data['sentiment']),
            'performance_correlations': len(self.all_data['performance'])
        }
    
    def export_to_csv(self, filename: str):
        """Export all data to CSV for analysis"""
        if self.all_data['sensors']:
            df = pd.DataFrame(self.all_data['sensors'])
            df.to_csv(filename, index=False)
            return f"Data exported to {filename}"
        return "No sensor data to export"
    
    def export_to_json(self, filename: str):
        """Export all data to JSON"""
        with open(filename, 'w') as f:
            json.dump(self.all_data, f, indent=2)
        return f"Data exported to {filename}"
