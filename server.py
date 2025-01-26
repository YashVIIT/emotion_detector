"""Server module for deploying the Emotion Detection application."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    """
    Render the home page.

    Returns:
        str: Rendered HTML template for the home page.
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def detect_emotion():
    """
    Handle the emotion detection request.

    Extracts the text to analyze from the query parameters,
    calls the emotion_detector function, and returns the formatted response.

    Returns:
        str: Formatted response or error message.
    """
    text_to_analyze = request.args.get('textToAnalyze', '').strip()

    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    formatted_result = (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, "
        f"'joy': {result['joy']}, and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return formatted_result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
