import requests
from bs4 import BeautifulSoup
import fake_useragent 
from yakytia24.yk_func import check_title


def yakytia24():
    user = fake_useragent.UserAgent().random 
    header = {'user-agent': user}
    url = 'https://yk24.ru/category/main/'
    response = requests.get(url, headers=header).text
    soup = BeautifulSoup (response, 'lxml')

    last_news = soup.find_all('div', class_ = 'archive-item')[0]
    news_link = last_news.find('a').get('href') 
    if check_title(news_link):
        return 'Error:101 Старая новость с сайта yakytia24'
    else:
        return news_page(news_link)
    
def news_page(url):
    try: 
        user = fake_useragent.UserAgent().random 
        header = {'user-agent': user}
        response = requests.get(url, headers=header).text
        soup = BeautifulSoup (response, 'lxml')

        title = soup.find('h1', class_ = 'article__title').text

        text_block = soup.find('div', class_='article__content')
        full_text_derty  = text_block.find_all('p')
        full_text_list = []
        for text_p in full_text_derty:  #в цикле соеденяем все полученные p
            full_text_list.append(text_p.text)

        full_text = '\n  '.join(full_text_list) #из списка переводим в строку

        # скачивание картинки
        try:
            image_block = soup.find('div', class_='article__thumbnail')
            image_link = image_block.findAll('img')
            for image in image_link:
                src = image.get("src")
                if src:
                    image_info = load_image(src)
        except:
            image_info = 'None'

        return title, full_text, image_info
    except Exception as ex:
            print(ex)
            return f'Error:102 - Упс, что-то пошло не так на второй стадии на сайте yakytia24 - {ex}'

def load_image(link):
    try:
        url = f'{link}'
        response = requests.get(url)
        
        with open ('content/yakytia24_image.jpg', 'wb') as file:
            file.write(response.content)
            return 'have'
    
    except Exception as ex:
        print(ex)
        return 'None'

