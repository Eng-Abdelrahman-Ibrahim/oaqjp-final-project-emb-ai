'''
Executing this command initiates the emotion detection function
using IBM Watson NLP library
'''
# Import the requests library to handle HTTP requests
import requests

# Define a function name emotion_detector that takes text_to_analyze as an argument to analyze it
def emotion_detector(text_to_analyze):
    '''
    This function defines url, headers, and myobj input
    from IBM Watson library and use these inputs to generate
    response based on the text_to_analyze argument
    '''

    # URL of the emotion detection service
    url = (
        'https://sn-watson-emotion.labs.skills.network/v1/'
        'watson.runtime.nlp.v1/NlpService/EmotionPredict'
    )

    # Defining the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Create a dectionary with the text that will be analyzed
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Send a POST request to the API with the text and headers
    response =  requests.post(url, json = myobj, headers=header, timeout=5)

    # Returns the text value of response
    return response.text
