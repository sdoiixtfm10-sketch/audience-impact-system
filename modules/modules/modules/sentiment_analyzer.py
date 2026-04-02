from textblob import TextBlob
from typing import Dict, List, Tuple

class SentimentAnalyzer:
    """Analyzes crowd sentiment from social media & comments"""
    
    def __init__(self):
        self.sentiments = []
    
    def analyze_text(self, text: str) -> Dict:
        """
        Analyze sentiment of crowd comments
        Returns polarity (-1 to 1) and subjectivity (0 to 1)
        """
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity
        
        return {
            'text': text[:100],
            'polarity': round(polarity, 3),
            'subjectivity': round(subjectivity, 3),
            'sentiment': self._classify_sentiment(polarity)
        }
    
    def _classify_sentiment(self, polarity: float) -> str:
        """Classify sentiment as positive, neutral, or negative"""
        if polarity > 0.1:
            return 'positive'
        elif polarity < -0.1:
            return 'negative'
        else:
            return 'neutral'
    
    def batch_analyze(self, texts: List[str]) -> Dict:
        """Analyze multiple texts and return aggregate sentiment"""
        results = [self.analyze_text(text) for text in texts]
        
        avg_polarity = sum(r['polarity'] for r in results) / len(results) if results else 0
        sentiment_counts = {}
        for r in results:
            s = r['sentiment']
            sentiment_counts[s] = sentiment_counts.get(s, 0) + 1
        
        return {
            'total_analyzed': len(results),
            'average_polarity': round(avg_polarity, 3),
            'sentiment_distribution': sentiment_counts,
            'details': results
        }
