import requests

def download_file_from_google_drive(id, destination):
    def get_confirm_token(response):
        for key, value in response.cookies.items():
            if key.startswith('download_warning'):
                return value

        return None

    def save_response_content(response, destination):
        CHUNK_SIZE = 32768

        with open(destination, "wb") as f:
            for chunk in response.iter_content(CHUNK_SIZE):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)

    URL = "https://drive.google.com/file/d/1Gh9Sfrgh0lveBTreEvsXv1ebzTS6WlCO/"
    #"https://drive.google.com/drive/folders/1XzBAKxKom4TAr-Or91dh2rXywnjbWijo?usp=sharing"#
#1W8rRheWttuAtmOZYjbbRzHdJW_bLg7ET
    session = requests.Session()
    #view?usp=sharing

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)    
#https://drive.google.com/file/d/0B7EVK8r0v71pOXBhSUdJWU1MYUk/view?usp=sharing

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python google_drive.py drive_file_id destination_file_path")
    else:
        # TAKE ID FROM SHAREABLE LINK
        file_id = sys.argv[1]
        # DESTINATION FILE ON YOUR DISK
        destination = sys.argv[2]
        download_file_from_google_drive(file_id, destination)