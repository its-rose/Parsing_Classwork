import requests
from bs4 import BeautifulSoup as BS

url = 'https://www.tenders.kg/'
# /html/body/div[4]/div[3]/div[1]/table/tbody/tr[2]/td[2]/strong[1]/font/span/a

def get_html():
    response = requests.get(url)
    return response.text

# https://www.tenders.kg/Announcements_list.php?goto=1
# https://www.tenders.kg/Announcements_list.php?goto=105
all_pages = []
pagination = 'Announcements_list.php?goto='
def get_all_pages():
    for page in range(0, 105):
        page += 1
        page_url = f'{url}{pagination}{page}'
        all_pages.append(page_url)
        with open('all_pages.txt', 'w') as file:
            for i in all_pages:
                file.write(f'{i}\n')
get_all_pages()

all_tenders = []
html = get_html()
soup = BS(html, 'html.parser')

def get_all_tenders():
    for page in range(0, 105):
                    page += 1

                    try:
                        span = soup.find('tbody').find_all('span')
                        for tender in span:
                            a = f'{url}{pagination}{page}{a}'
                            a = tender.find('a').get('href')
                            all_tenders.append(a)
                            print(a)
                    except Exception as ex:
                        pass
                        with open('all_tenders.txt', 'w') as file:
                            for tender in all_tenders:
                                file.write(f'{tender}\n')

get_all_tenders()
