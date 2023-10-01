import requests
from bs4 import BeautifulSoup
import fake_useragent 
from sch_day.day_func import check_title



def sakha_day():
    try:
        user = fake_useragent.UserAgent().random 
        header = {'user-agent': user}
        url = 'https://sakhaday.ru/'
        response = requests.get(url, headers=header).text
        soup = BeautifulSoup (response, 'lxml')

        news_card = soup.find_all('div', class_ = 'news_item')
        card = news_card[0]
        news_link = card.find('a', class_ = 'link').get('href') #сылка на новость 
        if check_title(news_link):
            return 'Error:13 Старая новость с сайта sakha_day'
        else:
            return news_page(news_link)
    except Exception as ex:
        print(ex)
        return 'Error:11 - Упс, что-то пошло не так на первой стадии на сайте sakha_day'

 



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
            image_block = soup.find('div', class_='image_container')
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
        return 'Error:12 - Упс, что-то пошло не так на второй стадии на сайте sakha_day'
    

def load_image(link):
    try:
        url = f'https://sakhaday.ru/{link}'
        response = requests.get(url)
        
        with open ('content/sakha_day_image.jpg', 'wb') as file:
            file.write(response.content)
            return 'have'
    
    except Exception as ex:
        print(ex)
        return 'None'
        # return f'Error:13 Упс, что то пошло не так на стадии скачивания картинки на sakha_day'
    

    