import requests

def download_no_watermark(video_url):
    # Eine häufig genutzte öffentliche API
    api_url = f"https://www.tikwm.com/api/?url={video_url}"
    
    response = requests.get(api_url).json()
    video_data_url = response['data']['play'] # URL zum Video ohne Wasserzeichen
    title = response['data']['title'][:20]    # Titel kürzen für Dateinamen

    # Download der eigentlichen Datei
    video_bytes = requests.get(video_data_url).content
    
    with open(f"{title}.mp4", "wb") as f:
        f.write(video_bytes)
    print(f"Video '{title}' erfolgreich heruntergeladen!")

link = input("TikTok Link: ")
download_no_watermark(link)