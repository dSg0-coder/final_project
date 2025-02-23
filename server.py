"""
This module provides the server side of the application Emotion Detector.

Functions:
- render_index_page(): Return index.html rendered.
- sent_analyzer(): Return emotions score with the dominant emotion.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """Return index.html rendered."""
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_analyzer():
    """Return emotions score with the dominant emotion."""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    return f"For the giver statement, the system response is \
        'anger': {response['anger']}, 'disgust': {response['disgust']}, \
        'fear': {response['fear']}, 'joy': {response['joy']} and \
        'sadness': { response['sadness']}. The dominant emotion \
        is {response['dominant_emotion']}."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
