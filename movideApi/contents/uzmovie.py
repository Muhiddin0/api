import requests
from bs4 import BeautifulSoup


def test():
    return

def uzmovie(q, p):

    # Data Json 
    data = {
        "site":"uzmovie",
        "max-pages": "",
        "now-page":f"{p}",
        "urls":[]
    }
    
    test()

    
    # STEP 1
        # Qidiruv natijalariga ko"ra Kinolarni olish 
    
    # sayitni qirqib olish
    url = f"http://uzmovi.com/search/page/{p}?q={q}"
    r = requests.request("GET", url)
    soup = BeautifulSoup(r.text, "lxml")

    
    
    
    # kinolarni qutisi
    kinolar_qutisi = soup.find(
        "div",
        {
            "class":"col-md-9 col-xs-12"
        }
    )
        
    # maximal pagelarni aniqlash
    try:
        pages_dom = kinolar_qutisi.find("div", {"class":"pages-numbers"})
        page_counter = 0
        for i in pages_dom.children:
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



    # content urlarini olish
    for kino_qutisi in kinolar_qutisi.find_all("a", href=True, title=True):
        if kino_qutisi["href"] == "http://uzmovi.com/":
            continue
        
        data["urls"].append(
            {
                "name":f"{kino_qutisi['title']}",
                "url":f"{kino_qutisi['href']}"
            }
        )

    
    return data