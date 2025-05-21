"""
Watson NLP API Flask server to analyze emotion in user text
"""
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_analysis():
    """
    Analyze text input for emotions and return results
    """
    text_to_analyse = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyse)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'sadness': {response['sadness']}, "
        f"'dominant_emotion': {response['dominant_emotion']}. "
    )

    return response_text

@app.route("/")
def index():
    """
    Serve the HTML page for the emotion detection app
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
    