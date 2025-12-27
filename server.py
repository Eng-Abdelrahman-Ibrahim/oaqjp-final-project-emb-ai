'''
This file is contains the web server routes and redirects to run
the web app emotion_detection on localhost, port 5000
'''

# Importing necessary libraries from flask
from flask import Flask, render_template, request

# Import emotion_detector function from the created package
from EmotionDetection.emotion_detection import emotion_detector

# Initialize the flask app
app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    ''' This function returns the rendering of the
        main page
    '''
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_detect():
    ''' This function receives the text from the HTML interface
        and returns the result of the emotion_detector function
    '''

    # Step1: Retreive the text to analyze from the request argument
    text_to_analyze = request.args.get("textToAnalyze")

    # Step2: Use the variable in emotion_detector function
    response = emotion_detector(text_to_analyze)

    # Returns Invalid text message if no text is given as input
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!."

    # Step3: Splits the dictionary into 2 parts, scores and dominant emotion
    scores = response.copy()
    dominant = scores.pop('dominant_emotion')

    # Return the final output string
    return (
        f"For the given statement, the system response is{scores}. " 
        f"The dominant emotion is {dominant}."
    )

# Run the web server when the script is executed directly
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=5000)
    