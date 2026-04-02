from typing import Dict, List
from datetime import datetime

class PerformanceTracker:
    """Correlates crowd metrics with team performance"""
    
    def __init__(self):
        self.performance_data = []
    
    def record_event(self, event_type: str, crowd_energy: float, 
                     team_a_score: int, team_b_score: int) -> Dict:
        """
        Record correlation between crowd state and game event
        event_type: 'goal', 'foul', 'injury', 'substitution'
        """
        return {
            'timestamp': datetime.now().isoformat(),
            'event_type': event_type,
            'crowd_energy': crowd_energy,
            'team_a_score': team_a_score,
            'team_b_score': team_b_score,
            'energy_momentum': self._calculate_momentum(crowd_energy)
        }
    
    def _calculate_momentum(self, energy: float) -> str:
        """Classify crowd momentum"""
        if energy >= 80:
            return 'high_momentum'
        elif energy >= 60:
            return 'building_momentum'
        else:
            return 'low_momentum'
    
    def analyze_performance_impact(self, crowd_metrics: List[Dict], 
                                   match_events: List[Dict]) -> Dict:
        """
        Analyze how crowd energy correlates with performance
        Returns correlation coefficient and insights
        """
        if not crowd_metrics or not match_events:
            return {'error': 'Insufficient data'}
        
        # Calculate correlation
        energy_values = [m['crowd_energy'] for m in crowd_metrics]
        avg_energy = sum(energy_values) / len(energy_values)
        
        # Count positive events during high-energy periods
        high_energy_events = [e for e in match_events 
                            if e.get('crowd_energy', 0) > 75]
        
        return {
            'average_crowd_energy': round(avg_energy, 2),
            'peak_energy': round(max(energy_values), 2),
            'high_energy_events': len(high_energy_events),
            'impact_score': round(len(high_energy_events) / max(len(match_events), 1) * 100, 2)
        }
