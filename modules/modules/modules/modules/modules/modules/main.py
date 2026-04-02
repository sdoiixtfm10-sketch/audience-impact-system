from flask import Flask, jsonify, request
from modules.audience_sensor import AudienceSensor
from modules.sentiment_analyzer import SentimentAnalyzer
from modules.performance_tracker import PerformanceTracker
from modules.data_aggregator import DataAggregator
from modules.reporting import ReportGenerator
from config import Config
import json

app = Flask(__name__)

# Initialize components
sensor = AudienceSensor()
sentiment = SentimentAnalyzer()
performance = PerformanceTracker()
aggregator = DataAggregator()

@app.route('/api/health', methods=['GET'])
def health():
    """Health check"""
    return jsonify({'status': 'healthy', 'service': 'Audience Impact System'})

@app.route('/api/audience/snapshot', methods=['GET'])
def get_snapshot():
    """Get current audience snapshot"""
    snapshot = sensor.capture_snapshot()
    return jsonify(snapshot)

@app.route('/api/audience/batch', methods=['POST'])
def collect_batch():
    """Collect batch of audience readings"""
    data = request.get_json() or {}
    count = data.get('count', 10)
    
    batch = sensor.collect_batch(count)
    aggregator.add_sensor_data(batch)
    
    return jsonify({
        'status': 'success',
        'readings_collected': len(batch),
        'data': batch
    })

@app.route('/api/sentiment/analyze', methods=['POST'])
def analyze_sentiment():
    """Analyze sentiment from texts"""
    data = request.get_json() or {}
    texts = data.get('texts', [])
    
    if not texts:
        return jsonify({'error': 'No texts provided'}), 400
    
    result = sentiment.batch_analyze(texts)
    aggregator.add_sentiment_data(result)
    
    return jsonify(result)

@app.route('/api/performance/event', methods=['POST'])
def record_event():
    """Record a match event with crowd context"""
    data = request.get_json() or {}
    
    event = performance.record_event(
        event_type=data.get('event_type', 'unknown'),
        crowd_energy=data.get('crowd_energy', 50),
        team_a_score=data.get('team_a_score', 0),
        team_b_score=data.get('team_b_score', 0)
    )
    
    aggregator.add_performance_data(event)
    return jsonify(event)

@app.route('/api/data/summary', methods=['GET'])
def get_summary():
    """Get aggregated data summary"""
    summary = aggregator.get_summary()
    return jsonify(summary)

@app.route('/api/report/match', methods=['POST'])
def generate_match_report():
    """Generate comprehensive match report"""
    data = request.get_json() or {}
    match_id = data.get('match_id', 'match_001')
    
    report_data = {
        'summary': aggregator.get_summary()
    }
    
    report = ReportGenerator.generate_match_report(match_id, report_data)
    formatted = ReportGenerator.format_for_display(report)
    
    return jsonify({
        'report': report,
        'formatted': formatted
    })

@app.route('/api/data/export', methods=['POST'])
def export_data():
    """Export collected data"""
    data = request.get_json() or {}
    format_type = data.get('format', 'json')
    filename = data.get('filename', 'audience_data')
    
    if format_type == 'csv':
        result = aggregator.export_to_csv(f"{filename}.csv")
    else:
        result = aggregator.export_to_json(f"{filename}.json")
    
    return jsonify({'status': 'success', 'message': result})

if __name__ == '__main__':
    print("""
    ╔═══════════════════════════════════════════════════════╗
    ║   CROWD IMPACT ANALYTICS SYSTEM                       ║
    ║   Real-time Audience Data Collection & Analysis       ║
    ╚═══════════════════════════════════════════════════════╝
    """)
    
    app.run(
        host=Config.API_HOST,
        port=Config.API_PORT,
        debug=True
    )
