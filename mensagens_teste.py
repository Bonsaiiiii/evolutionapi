import requests
import time

def enviar_mensagem(number, text, tipo = 0):
    if tipo == 0:
        url = "http://localhost:8080/message/sendText/torb"
        payload = {
            "number": number,
            "text": text
        }
    elif tipo == 1: 
        url = "http://localhost:8080/message/sendMedia/torb"
        payload = {
            "number": number,
            "mediatype": "image",
            "mimetype": "image/png",
            "caption": "Codora",
            "media": "https://upload.wikimedia.org/wikipedia/commons/d/d8/Taoniscus.jpg",
            "fileName": "Codorna.png"
        }

    headers = {
        "Content-Type": "application/json",
        "apikey": "E9C67FFF60A3-42DC-BF86-4445A4455376",
        "User-Agent": "PostmanRuntime/7.44.1",
        "Accept": "*/*"
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        return response.status_code, response.text
    except requests.RequestException as e:
        return 500, str(e)

while True:
    status, response = enviar_mensagem("5547997691399", "quebraram minha torre", 1)
    print(f"Status: {status}, Response: {response}")
    
    time.sleep(0)

#5548999509969