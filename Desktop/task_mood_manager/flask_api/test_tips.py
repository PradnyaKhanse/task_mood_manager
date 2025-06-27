import requests

resp = requests.post(
    "http://127.0.0.1:5001/api/tips",
    json={"mood": "happy"}
)
print(resp.status_code, resp.json())
