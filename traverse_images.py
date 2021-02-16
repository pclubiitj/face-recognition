from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


# Get a client_secrets.json from Google Cloud console
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)


# Add Photography club's drive as a shortcut to your google drive
fileList = drive.ListFile({
    'q': "'127DYBOd4M98t6KNCJeZ9Y6WJB7B5wb_3' in parents and trashed=false"
    }).GetList()

for file in fileList:
    print('Title: %s, ID: %s' % (file['title'], file['id']))
