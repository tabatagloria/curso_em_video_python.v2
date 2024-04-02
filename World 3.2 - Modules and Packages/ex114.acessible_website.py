# Create a Python code that tests if the website is accessible from the computer being used

import requests
import urllib

try:
    url = urllib.request.urlopen('https://www.google.com')
except urllib.error.URLError:
    print('Error! I can`t acessed this website')
else:
    print('I successfully accessed this website.')

    