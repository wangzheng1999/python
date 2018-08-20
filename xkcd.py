import requests,os,bs4
url='http://xkcd.com'
os.makedirs('xkcd',exist_ok=True)
while not url.endwith('#'):
  print('Done.')
