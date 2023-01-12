import requests

print(requests.__version__)
response = requests.get("https://raw.githubusercontent.com/Javinvora/404Lab1/master/lab1.py");
print(response.text)
