from googleapiclient.http import MediaFileUpload
from Google import Create_Service

CLIENT_SECRET_FILE = 'client-secret.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

# Upload a file
file_metadata = {
    'name': 'drink.png',
    'parents': ['1HhaxcPXMO4nWAU0gynSwhxsSPz3287KQ']
}

media_content = MediaFileUpload(r'C:\Users\rjakkula\Downloads\coffee.png', mimetype='image/png')

file = service.files().create(
    body=file_metadata,
    media_body=media_content
).execute()

print(file)