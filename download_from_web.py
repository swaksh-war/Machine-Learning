import requests

url = r'https://i.insider.com/5cbf50dfd1a2f8074406a8b2?width=1136&format=jpeg'

r = requests.get(url)

with open("image.jpg",'wb') as i:
    i.write(r.content)