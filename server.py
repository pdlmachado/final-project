"""This module implements the server of the Emotion Detection App"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_detector():
    """ Router for the emotion_detector function"""    
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    a = response['anger']
    d = response['disgust']
    f = response['fear']
    j = response['joy']
    s = response['sadness']
    d_e = response['dominant_emotion']
    if d_e is None:
        return "Invalid text! Please try again!"
    cab = "For the given statement, the system response is "
    emotions = f"'anger': {a}, 'disgust': {d}, 'fear': {f},'joy': {j} and 'sadness': {s}."
    dominant_emotion = f"The dominant emotions is {d_e}."
    return cab + emotions + dominant_emotion

@app.route("/")
def render_index_page():
    """ Render app """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
