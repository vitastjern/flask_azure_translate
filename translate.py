import os, requests, uuid, json

# Don't forget to set AZ_KEY1_TRANSLATE, AZ_REGION and AZ_ENDPOINT as environment 
# variables with your Cognitive Services values before running this app!
# See app.py about the environment variables.
# This way I will not store my keys etc in github...
subscription_key = os.getenv('AZ_KEY1_TRANSLATE')
location = os.getenv('AZ_REGION')
endpoint = os.getenv('AZ_ENDPOINT')

# Our Flask route will supply two arguments: text_input and language_output.
# When the translate text button is pressed in our Flask app, the Ajax request
# will grab these values from our web app, and use them in the request.
# See main.js for Ajax calls.
def get_translation(text_input, language_output):
    base_url = endpoint
    path = '/translate?api-version=3.0'
    params = '&to=' + language_output
    constructed_url = base_url + path + params

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = [{
        'text' : text_input
    }]
    response = requests.post(constructed_url, headers=headers, json=body)
    return response.json()