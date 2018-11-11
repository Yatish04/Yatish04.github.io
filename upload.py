import requests
import json
headers = {"Authorization": "Bearer ya29.GltRBuIZz0L_cmo6sUcHvoFYs9NEfV2PVPf8CCMUk1xdiqX6JV-tjJsBedBIFQqNfRmgq6xBqmXEyvzqDjlB92oFvuTMmAvSlErU-7yBgObtV_2QVvdTMJNkP4nj"
} #put ur access token after the word 'Bearer '
para = {
    "name": "model_2.h5", #file name to be uploaded
    "parents": ["1r1CDFiE0xlcGrjledoFbLqK5rudZ8erf"] # make a folder on drive in which you want to upload files; then open that folder; the last thing in present url will be folder id
}
files = {
    'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
    'file': ('application/h5',open("./model_2.h5", "rb")) # replace 'application/zip' by 'image/png' for png images; similarly 'image/jpeg' (also replace your file name)
}
r = requests.post(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=headers,
    files=files
)
print(r.text)
