from typing import Dict
import json

class ReportGenerator:
    """Generates reports for coaches and analysts"""
    
    @staticmethod
    def generate_match_report(match_id: str, aggregated_data: Dict) -> Dict:
        """Generate comprehensive match report"""
        return {
            'match_id': match_id,
            'report_type': 'audience_impact_analysis',
            'data_summary': aggregated_data.get('summary', {}),
            'key_insights': ReportGenerator._extract_insights(aggregated_data),
            'recommendations': ReportGenerator._generate_recommendations(aggregated_data)
        }
    
    @staticmethod
    def _extract_insights(data: Dict) -> list:
        """Extract key insights from data"""
        insights = []
        
        summary = data.get('summary', {})
        avg_energy = summary.get('average_crowd_energy', 0)
        
        if avg_energy > 75:
            insights.append("Crowd provided exceptional energy throughout the match")
        elif avg_energy > 60:
            insights.append("Crowd maintained good energy levels")
        else:
            insights.append("Crowd energy was lower than optimal")
        
        return insights
    
    @staticmethod
    def _generate_recommendations(data: Dict) -> list:
        """Generate actionable recommendations for coaches"""
        recommendations = []
        
        summary = data.get('summary', {})
        avg_energy = summary.get('average_crowd_energy', 0)
        
        if avg_energy < 60:
            recommendations.append("Engage crowd with more attacking plays")
            recommendations.append("Consider momentum-building substitutions")
        
        if avg_energy > 80:
            recommendations.append("Leverage high crowd energy for attacking")
            recommendations.append("Maintain possession to sustain momentum")
        
        return recommendations
    
    @staticmethod
    def format_for_display(report: Dict) -> str:
        """Format report for display"""
        output = f"""
╔════════════════════════════════════════════════════════╗
║        CROWD IMPACT ANALYSIS REPORT                    ║
╠════════════════════════════════════════════════════════╣
║ Match ID: {report.get('match_id', 'N/A')}
║ Type: {report.get('report_type', 'N/A')}
╠════════════════════════════════════════════════════════╣
║ KEY INSIGHTS:
"""
        for insight in report.get('key_insights', []):
            output += f"║  • {insight}\n"
        
        output += "║\n║ RECOMMENDATIONS:\n"
        for rec in report.get('recommendations', []):
            output += f"║  • {rec}\n"
        
        output += "╚════════════════════════════════════════════════════════╝\n"
        
        return output
