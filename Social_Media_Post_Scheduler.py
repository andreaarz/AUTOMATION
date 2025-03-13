#Código Python para programar y publicar en Twitter

import tweepy
import time
from datetime import datetime

# Configura tus credenciales de la API de Twitter
API_KEY = 'tu_api_key'
API_SECRET_KEY = 'tu_api_secret_key'
ACCESS_TOKEN = 'tu_access_token'
ACCESS_TOKEN_SECRET = 'tu_access_token_secret'

# Autenticación con la API de Twitter
auth = tweepy.OAuth1UserHandler(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET_KEY,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

# Crear el objeto API
api = tweepy.API(auth)

# Lista de publicaciones programadas
posts = [
    {"content": "Good morning! Here's your daily tip: Stay productive! #Motivation", "time": "2025-03-13 09:00:00"},
    {"content": "Check out our latest blog post on tech trends! #Technology #Blog", "time": "2025-03-13 12:00:00"},
    {"content": "Happy Friday! Let's wrap up the week with a big smile! #FridayVibes #PositiveEnergy", "time": "2025-03-13 17:00:00"}
]

# Función para programar publicaciones
def schedule_posts():
    for post in posts:
        # Convertir el tiempo programado de la publicación en un objeto datetime
        post_time = datetime.strptime(post['time'], "%Y-%m-%d %H:%M:%S")
        current_time = datetime.now()

        # Si la hora de publicación es en el futuro, esperar hasta esa hora
        if post_time > current_time:
            # Calcular el tiempo restante para la publicación
            wait_time = (post_time - current_time).total_seconds()
            print(f"Waiting for {wait_time} seconds to post: '{post['content']}'")

            # Esperar hasta la hora de la publicación
            time.sleep(wait_time)

            # Publicar en Twitter
            try:
                api.update_status(post['content'])
                print(f"Successfully posted: {post['content']}")
            except tweepy.TweepError as e:
                print(f"Error posting tweet: {e}")
        else:
            print(f"Skipped post because the scheduled time is in the past: '{post['content']}'")

# Ejecutar la programación de publicaciones
if __name__ == "__main__":
    schedule_posts()


""" Explicacion:
Autenticación con la API de Twitter:

Usamos tweepy.OAuth1UserHandler para autenticar la conexión con Twitter usando las credenciales obtenidas en el portal de desarrolladores de Twitter (API Key, Access Token, etc.).
Se crea un objeto api que nos permite interactuar con la API de Twitter.
Lista de publicaciones programadas:

La variable posts contiene las publicaciones programadas, donde cada publicación tiene un contenido y una hora programada (time).
El formato de fecha y hora debe ser YYYY-MM-DD HH:MM:SS.
Función schedule_posts:

Recorre la lista de publicaciones, verifica si la hora programada es en el futuro y calcula el tiempo de espera para publicar el contenido.
Usa time.sleep() para esperar hasta el momento exacto de la publicación.
Cuando llega el momento de publicar, se usa api.update_status() para publicar el contenido en Twitter.
Publicación en Twitter:

Si la hora de la publicación está en el futuro, el script esperará y luego publicará el contenido en Twitter.
Si la hora de la publicación ya ha pasado, se omite esa publicación.
Manejo de errores:

En caso de que ocurra algún error (por ejemplo, si las credenciales son incorrectas o si hay un problema con la conexión a la API), se captura el error usando try/except y se muestra un mensaje de error.
"""
