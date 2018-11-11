import requests
import json
headers = {"Authorization": "Bearer ya29.GltRBgYfFGk9tN8rj4dwrBU-XUKfPaxT8AaYFy9ejFoOpOrfM6j8MZc5TgSSaQNZeUTZwVuqPTPBSJu2RbRj-xEyEccfAcwiqEp1eLevnpnc71QScCVh15wTohhu"
} #put ur access token after the word 'Bearer '
para = {
    "name": "models19.zip", #file name to be uploaded
    "parents": ["1r1CDFiE0xlcGrjledoFbLqK5rudZ8erf"] # make a folder on drive in which you want to upload files; then open that folder; the last thing in present url will be folder id
}
files = {
    'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
    'file': ('application/zip',open("./models19.zip", "rb")) # replace 'application/zip' by 'image/png' for png images; similarly 'image/jpeg' (also replace your file name)
}
r = requests.post(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=headers,
    files=files
)
print(r.text)
