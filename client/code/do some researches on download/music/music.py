import requests

response = requests.get('http://om5.alicdn.com/886/670338886/2100341606/1776107646_1463801047464.mp3?auth_key=67a7247f95ac5e2d6a98d9cb91f88ae9-1493607600-0-null')
with open('1.mp3', 'wb') as f:
    f.write(response.content)