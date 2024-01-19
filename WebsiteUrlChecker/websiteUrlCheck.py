import re

urlChecker = re.compile(r'https?://[^\s<>"]+|www\.[^\s<>"]+')

test = 'Check out this website: https://www.example.com or http://example.org for more information.'

urls = urlChecker.findall(test)

print(urls)
