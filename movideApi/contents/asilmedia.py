
from bs4 import BeautifulSoup
import requests


def asilmedia(q, p):

    # Data Json
    data = {
        "site":"asilmedia",
        "max-pages":"",
        "now-page":f"{p}",
        "urls":[]
    }

    url = f"http://asilmedia.org/index.php?story={q}&search_start={p}&do=search&subaction=search"
    r = requests.request('GET', url)

    soup = BeautifulSoup(r.text, 'lxml')
    
    kinolar_qutisi = soup.find(
        'div',
        {
            'id':'dle-content'
        }
    )
    
    for kino_card in kinolar_qutisi.find_all('a', {'href':True, 'class':'flx flx-column flx-column-reverse'}):
        data['urls'].append({
            "name":f"{kino_card.find('h2', {'class':'title is-6 txt-ellipsis mb-2'}).text}",
            "url":f"{kino_card['href']}"
        })

    try:
        pages_dom = kinolar_qutisi.find('div',{'class':'navigation fx-row fx-start'}).find_all('a')
        page_counter = 1
        for i in pages_dom:
            page_counter += 1

        max_page = str(page_counter)
        
        if max_page == p: # pagelarni tugashi
            data["max-pages"] = "stoped-page"
        elif p == '1': #pagelarni boshlanishi
            data["max-pages"] = "start-page"
        else: #yakka pagelar
            data["max-pages"] = max_page
    except:
        data["max-pages"] = 'yakka-page'


    return data