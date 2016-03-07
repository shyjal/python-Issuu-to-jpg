from urllib.request import urlopen
from os import path
from os import makedirs
from bs4 import BeautifulSoup
import urllib.request
import re
import json
import sys


configid = '0/33964045'

if(len(sys.argv) > 0):
	configid=str(sys.argv[0])
	
issuuSoup = BeautifulSoup(urlopen("http://e.issuu.com/embed/"+configid+".json?v=1.0.0").read())

jsonData=json.loads(str(issuuSoup))

issuuDocumentId = jsonData['id']

print("issuu doc id :"+issuuDocumentId)

index = 1

while (1==1):
	imageUrl = "http://image.issuu.com/"+str(issuuDocumentId)+"/jpg/page_"+str(index)+".jpg"
	print("Downloading"+imageUrl)
	try:
		urllib.request.urlretrieve(imageUrl, '{}.jpg'.format(index))
	except urllib.error.HTTPError:
		break
	index=index+1
