import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj, headers=header)
    formatted_response = json.loads(response.text)
    emotions_list = ['anger', 'disgust', 'fear', 'joy', 'sadness']
    if response.status_code == 200:
        output_dict = {k: formatted_response['emotionPredictions'][0]['emotion'][k] for k in emotions_list}
        output_dict['dominant_emotion'] = max(output_dict, key=output_dict.get)
    elif response.status_code == 400:
        output_dict = {k: None for k in emotions_list}
        output_dict['dominant_emotion'] = None

    return output_dict