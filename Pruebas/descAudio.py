import yt_dlp

def descargar_audio(url,name):
    name = name
    try:
        ydl_opts = {
            'format': 'bestaudio',
            'outtmpl': f'./{name}.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',
                'preferredquality': '192',
            }],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

    except Exception as e:
        print(f"Ocurrió un error al descargar el audio: {e}")


if __name__ == "__main__":
    url = input('Ingrese URL: ')
    name = input('Ingrese nombre: ')
    descargar_audio(url,name)