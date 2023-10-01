import requests
from bs4 import BeautifulSoup
import fake_useragent 
from sch_pres.pres_func import check_title
 


def sakha_press():
    try:
        user = fake_useragent.UserAgent().random 
        header = {'user-agent': user}
        url = 'https://sakhapress.ru/'
        response = requests.get(url, headers=header).text
        soup = BeautifulSoup (response, 'lxml')

        news_card = soup.find_all('div', class_ = 'posts')
        card = news_card[0]
        link_block = card.find('div', class_ = 'title')
        news_link = link_block.find('a', class_ = 'link').get('href') #сылка на новость 
        if check_title(news_link):
            return 'Error:23 - Старая новость с сайта sakha_press'
        else:
            return news_page(news_link)
    except Exception as ex:
        print(ex)
        return 'Error:21 - Упс, что-то пошло не так на первой стадии на сайте sakha_press'
    

def news_page(url):
    try:
        user = fake_useragent.UserAgent().random 
        header = {'user-agent': user}
        response = requests.get(url, headers=header).text
        soup = BeautifulSoup (response, 'lxml')
        title = soup.find('h1').text

        text_block = soup.find('div', class_='text')
        full_text_derty  = text_block.find_all('p')
        full_text_list = []
        for text_p in full_text_derty:  #в цикле соеденяем все полученные p
            full_text_list.append(text_p.text)
        full_text = '\n'.join(full_text_list) #из списка переводим в строку

        # скачивание картинки
        try:
            image_block = soup.find('p', class_='aligncenter')
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
        return 'Error:22 - Упс, что-то пошло не так на второй стадии на сайте sakha_press'

def load_image(link):
    try:
        url = f'https://sakhapress.ru/{link}'
        response = requests.get(url)
        
        with open ('content/sakha_press_image.jpg', 'wb') as file:
            file.write(response.content)
            return 'have'
    
    except Exception as ex:
        print(ex)
        return f'None'