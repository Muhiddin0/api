import requests
from bs4 import BeautifulSoup

def asilemdiaDow(q):
    
    # web scrap
    url = f'http://asilmedia.org/{q}'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')

    # API Json
    
    online_watch = soup.find(
        'button',
            {
            'class':"button button100 txt-uppercase mb-2",
            "data-src":"#onlayn1"
            }
        )
    
    if online_watch == None:
        return {
            "content":'game'
        }
        
    APIjson = {
        'content':'movie',
        "img": "http://asilmedia.org/",
        'yili': "",
        'davlati': "",
        'nomi':f"{soup.find('h1', class_='title is-4 mb-2').text}",
        'data':[]
    }
    
    # img
    try:
        APIjson['img'] += soup.find('img', class_='img-fit lazyload')['data-src']
    except TypeError:
        APIjson['img'] += soup.find('img', class_='img-fit lazyload')['data-src']
    except:
        APIjson['img'] += "/templates/playfilmo/dleimages/no_image.jpg"


    # yili
    try:
        APIjson['yili'] = soup.find_all('span', class_='fullmeta-seclabel')[0].text
    except:
        APIjson['yili'] = "Nomalum"

    # davlati
    try:
        APIjson['davlati'] = soup.find_all('span', class_='fullmeta-seclabel')[1].text
    except:
        APIjson['davlati'] = "Nomalum"

    # download link box WEB ELEMENT
    link_box = soup.find(
        'div',
        {
            'class':'downlist-inner flx flx-column'
        }
    )
    
    
    a_tags = link_box.find_all('a', href=True)
    # bug download fixwd
    if len(a_tags) == 1:
        video_src_atr = soup.find('iframe')['src']
        APIjson['data'].append({
            "url":video_src_atr,
            "title":APIjson['nomi']
        })
        return APIjson

    # download data make
    for link_a in a_tags:

        url_movie = link_a['href']
        while url_movie[0] == ' ':
            url_movie = url_movie[1:]

        title_movie = link_a.text
        APIjson['data'].append(
            {
                "url":url_movie,
                "title":title_movie
            }
        )
    APIjson['data'] = APIjson['data'][1:]
    return APIjson
