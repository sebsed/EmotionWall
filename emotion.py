import boto3
import pandas as pd

# Obtener credenciales de usuario
credential = pd.read_csv('RaspiRekognition_accessKeys.csv')

access_key_id = credential['Access key ID'][0]
secret_access_key = credential['Secret access key'][0]

rekognition = boto3.client('rekognition',aws_access_key_id=access_key_id,
             aws_secret_access_key=secret_access_key,
             region_name="us-west-2")

# Analizar emoción con AWS rekognition
def getEmotion(response_content):
    rekognition_response = rekognition.detect_faces(Image={'Bytes':response_content}, Attributes=['ALL'])

    for item in rekognition_response.get('FaceDetails'):
        face_emotion_confidence = 0
        face_emotion = None
        for emotion in item.get('Emotions'):
            if emotion.get('Confidence') >= face_emotion_confidence:
                face_emotion_confidence = emotion['Confidence']
                face_emotion = emotion.get('Type')
    
    return transEmotion(face_emotion)

# Mensajes a desplegar en pantalla
def transEmotion(detected_emotion):
    return{
        'HAPPY': '¡Qué bueno verte feliz!',
        'SAD': '¿Por qué estás triste?',
        'ANGRY': '¡No te enojes!',
        'CONFUSED': '¿Te confundiste?',
        'DISGUSTED': '¿Te doy asco?',
        'SURPRISED': '¡ME SORPRENDO!',
        'CALM': 'Un gusto verte en calma',
        'FEAR': '¡No tengas miedo!',
        'UNKNOWN': 'No puedo detectarte :('
    }[detected_emotion]