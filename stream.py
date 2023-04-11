import threading
import os
import requests
import time
streamkey = "live_210990436_amVnCWsic3Vt8eHJhShxUlUAgv4RyI"
resolution = "1280x720"
command = str("ffmpeg -f v4l2 -framerate 30 -video_size " + resolution + " -input_format mjpeg -i /dev/video1 -pix_fmt yuv420p -c:v libx264 -preset veryfast -b:v 2500k -maxrate 3000k -bufsize 6000k -threads 0 -f flv rtmp://live.twitch.tv/app/"+ streamkey)

auth ="https://id.twitch.tv/oauth2/authorize?response_type=code&client_id=nb6e6hevkw46dvxsbkbs5mu5qk6mw8&redirect_uri=https://localhost&scope=channel:manage:broadcast&force_verify=true"

TWITCH_CLIENT_ID = "nb6e6hevkw46dvxsbkbs5mu5qk6mw8"
TWITCH_ACCESS_TOKEN = "19ci7f6fdqddhvga01vxlmucvryuex"
TWITCH_CHANNEL_ID = "21099043"
TWITCH_CLIENT_SECRET = "pptx2y5eiwlf2ojk8fyinzvtydfrqi"

def getAccessToken():
    url = "https://id.twitch.tv/oauth2/token"
    data = {
        "client_id": TWITCH_CLIENT_ID,
        "client_secret": TWITCH_CLIENT_SECRET,
        "grant_type": "client_credentials",
        "scope": "channel:manage:broadcast",
    }
    response = requests.post(url, data=data)
    response.raise_for_status()
    print(response.json()['access_token'])
    return (response.json()["access_token"])

def setAccessToken():
    global TWITCH_ACCESS_TOKEN
    TWITCH_ACCESS_TOKEN = getAccessToken()
    print(TWITCH_ACCESS_TOKEN)


def startStream():
    thread = threading.Thread(target=os.system, args=(command,))
    thread.start()

def stopStream():
    os.system("pkill ffmpeg")

def getUser():
    url="https://api.twitch.tv/helix/users?login=lonelybiscuit07"
    headers = {
        "Client-ID": TWITCH_CLIENT_ID,
        "Authorization": f"Bearer {TWITCH_ACCESS_TOKEN}",
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()["data"][0]
    print(data)
    return data["id"]

def set_goal(amount):
    goal = f"Help me reach my goal of ${amount}!"
    headers = {
        "Client-ID": TWITCH_CLIENT_ID,
        "Authorization": "Bearer " + TWITCH_ACCESS_TOKEN,
        "Content-Type": "application/json",
    }
    data = {"title": goal}
    url = f"https://api.twitch.tv/helix/channels?broadcaster_id={TWITCH_CHANNEL_ID}"
    response = requests.patch(url, headers=headers, json=data)
    response.raise_for_status()

def get_goal():
    headers = {
        "Client-ID": TWITCH_CLIENT_ID,
        "Authorization": f"Bearer {TWITCH_ACCESS_TOKEN}",
    }
    url = f"https://api.twitch.tv/helix/channels?broadcaster_id={TWITCH_CHANNEL_ID}"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()["data"]
    print(response.json()['data'])
    return data

if __name__ == "__main__":
    getUser()
    getAccessToken()
    setAccessToken()
    get_goal()
    set_goal(10)
