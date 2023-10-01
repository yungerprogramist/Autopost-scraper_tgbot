from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import requests

from sch_news.news_func import check_title

from chromedriver_py import binary_path

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--log-level=3')
options.add_argument("--headless") #скрытие браузера 


 


def sakha_news():
    try:
        svc = Service(executable_path=binary_path)
        driver = webdriver.Chrome(service=svc, options=options) 

        driver.get(url='https://1sn.ru/')
        driver.implicitly_wait(5)

        head_news_block = driver.find_elements(By.CLASS_NAME, 'col-md-9')[0]
        link = head_news_block.find_element(By.TAG_NAME, 'a').get_attribute('href')
        if check_title(link):
            return 'Error:33 Старая новость с сайта sakha_news'
        else:
            return news_page(link)
    except Exception as ex:
        print(ex)
        return 'Error:31 - Упс, что-то пошло не так на первой стадии на сайте sakha_news'
    finally:
        driver.close()
        driver.quit()


def news_page(url):
    try:
        svc = Service(executable_path=binary_path)
        driver = webdriver.Chrome(service=svc, options=options) 
        driver.get(url=url)
        driver.implicitly_wait(3)

        full_news = driver.find_element(By.ID, 'article')
        title = full_news.find_element(By.TAG_NAME, 'h1').text
        
        full_text_block = full_news.find_element(By.CLASS_NAME, 'detail_text')
        full_text_derty = full_text_block.find_elements(By.TAG_NAME, 'p')
        full_text_list = []
        for text_p in full_text_derty:  #в цикле соеденяем все полученные p
            full_text_list.append(text_p.text)
        full_text = '\n'.join(full_text_list) #из списка переводим в строку

        # скачивание картинки
        image_block = full_text_block.find_elements(By.TAG_NAME, 'p')[1]
        try:
            img_link = image_block.find_element(By.TAG_NAME, "img").get_attribute("src")
            if img_link:
                image_info = load_image(img_link)
        except:
            image_info = 'None'
        

        return title, full_text, image_info

    except Exception as ex:
        print(ex)
        return 'Error:32 - Упс, что-то пошло не так на второй стадии на сайте sakha_news'
    
def load_image(url):
    try:
        url = f'{url}'
        response = requests.get(url)
        
        with open ('content/sakha_news_image.jpg', 'wb') as file:
            file.write(response.content)

            return 'have'
    
    except Exception as ex:
        print(ex)
        return f'None'
    