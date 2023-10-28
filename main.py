
import requests
import os
from openai import OpenAI

# Définissez les variables d'environnement
API_KEY = os.getenv("META_CLOUD_API_KEY")
API_SECRET = os.getenv("META_CLOUD_API_SECRET")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Créez un objet OpenAI
openai = OpenAI(api_key=OPENAI_API_KEY)

# Créez un objet API Meta Cloud
meta_cloud = MetaCloud(api_key=API_KEY, api_secret=API_SECRET)

# Définissez une fonction pour traiter les messages entrants
def handle_message(message):
    # Obtenez le texte du message
    text = message.text

    # Créez une réponse avec l'API OpenAI
    response = openai.generate("text", prompt=text)

    # Envoyez la réponse au client
    meta_cloud.send_message(message.from_number, response)

# Démarrez le bot
while True:
    # Attendez un nouveau message
    message = meta_cloud.receive_message()

    # Traitez le message
    handle_message(message)
