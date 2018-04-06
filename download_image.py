# /usr/lib64/env python3.6
# -*- coding: utf-8 -*-
import bs4
import requests
URL = 'https://picjumbo.com/?s='


def run():
    busqueda = input('Write a category of image, like night, people, sports, etc: ')
    url = '{}{}'.format(URL, busqueda)
    web = requests.get(url)
    soup = bs4.BeautifulSoup(web.content, 'html.parser')
    src = soup.find_all('img', {'class': 'image'})
    for link in src:
        tmp = link.get('src')
        lin = 'https:{}'.format(tmp) if 'https' not in tmp else tmp
        lin = ''.join(lin.split('?')[0])
        # print(lin)
        image_name = lin.split('/')[-1]
        # print(image_name)
        print('Downloading image {}'.format(image_name))
        urllib.request.urlretrieve('{}'.format(lin), image_name)
    
    
if __name__ == '__main__':
    print('Bienvenidos sean!')
    run()
