import os
import shutil
import urllib.request
import bs4
import requests
from mimetypes import guess_extension

# global dump

def get_dwonload(name, id):
    name=name.replace(' ', '-')
    response = requests.get("http://apkpure.com/{}/{}".format(name,id))
    soup = bs4.BeautifulSoup(response.text)
    # links=[a.attrs.get('href') for a in soup.select('a.ga') if 'com.imangi.templerun2' in a.attrs.get('href')]
    # links=[a.attrs.get('href') for a in soup.select('a.ga') if id in a.attrs.get('href')]
    links=[a.attrs.get('href') for a in soup.select('a.ga') if 'fn=%s'%name[:name.find('-')] in a.attrs.get('href') ][0]
    # print(links)
    # links=[a.attrs.get('href') for a in soup.select('a.ga')]
    # print(links)
    return name,links

def download_file(url):
    # url = "'http://download.apkpure.com/apk3/M00/00/06/wGOTMFXAqeyAR8qQAuUuCCkwzAQ165.apk?fn=%D7%91%D7%A0%D7%A7%20%D7%94%D7%A4%D7%95%D7%A2%D7%9C%D7%99%D7%9D%20%D7%A0%D7%99%D7%94%D7%95%D7%9C%20%D7%94%D7%97%D7%A9%D7%91%D7%95%D7%9F_v26.2_apkpure.com.apk&k=89f4d7bfc86fc8464c1d88cbca93cd8255fbe14f&p=com.ideomobile.hapoalim'http://download.apkpure.com/apk3/M00/00/06/wGOTMFXAqeyAR8qQAuUuCCkwzAQ165.apk?fn=%D7%91%D7%A0%D7%A7%20%D7%94%D7%A4%D7%95%D7%A2%D7%9C%D7%99%D7%9D%20%D7%A0%D7%99%D7%94%D7%95%D7%9C%20%D7%94%D7%97%D7%A9%D7%91%D7%95%D7%9F_v26.2_apkpure.com.apk&k=89f4d7bfc86fc8464c1d88cbca93cd8255fbe14f&p=com.ideomobile.hapoalim"
    return urllib.request.urlopen(url)
    # print(source.info()['Content-Type'])
    # extension = guess_extension(source.info()['Content-Type'])
    # print(extension)
    #
    # return source
    # file = requests.get(url, stream=True)
    # print(type(file))
    # return file.raw


def save_file(name,file):
    print(name)
    print(file)
    with open('{}.apk'.format(name),'wb') as f:
        f.write(file.read())
# def save_file(name,dump):
#     print(dump)
#     print(type(dump))
#     location = os.path.abspath("")
#     with open("{}.apk".format(name), 'wb') as location:
#         shutil.copyfileobj(dump, location)
#     del dump



def download_file_all(name, id):
    url=get_dwonload(name,id)
    # print(url[1])
    # save_file(url[0],download_file(url[1]))
    # return url[1]
    return download_file(url[1])
    # print(url[0])
    # print(url[1])
    # save_file(url[0],file)


if __name__ == '__main__':

    # url = get_dwonload('waze-social-gps-maps-traffic', 'com.waze')
    url = get_dwonload('Clouds & Sheep 2', 'com.hg.cloudsandsheep2free')
    print(url)
    a='Clouds & Sheep 2'
    b=a[:a.find(' ')]
    # print(b)

# file = download_file(url)
#     save_file(url[0],download_file(url[1]))
#     save_file(url[0],download_file(url[1]))
