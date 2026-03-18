URL="https://www.youtube.com/@ApnaCollegeOfficial"
Protocol=URL[: URL.find(':')]
dot1=URL.find('.')
dot2=URL.find('.',dot1+1)
Domain=URL[dot1+1: dot2]
Page=URL[URL.find ('A',dot2):]
print('Domain:',Domain)
print('Protocol:',Protocol)
print('Page:',Page)