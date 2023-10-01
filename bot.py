import telebot 
from handler import main
from time import sleep

from dotenv import load_dotenv
import os 

load_dotenv()

bot = telebot.TeleBot (os.getenv('BOT_TOKEN')) 
chanel_id = '@test_chanel_023'


@bot.message_handler(commands=['start'])
def start(message):
    print('works') 
    while True:
        all_info_dict = main()

        sakha_day_text = all_info_dict['sakha_day']['text']
        if 'Error' in sakha_day_text:
            print(sakha_day_text)
        else:
            sakha_day_image = all_info_dict['sakha_day']['image']
            if sakha_day_image == 'have':
                photo = open('content/sakha_day_image.jpg', 'rb')
                bot.send_photo(chat_id=chanel_id, photo=photo)
                bot.send_message(chat_id=chanel_id, text=sakha_day_text)
            else:
                bot.send_message(chat_id=chanel_id, text = sakha_day_text )

        sakha_press_text = all_info_dict['sakha_press']['text']
        if 'Error' in sakha_press_text:
            print(sakha_day_text)
        else:
            sakha_press_image = all_info_dict['sakha_press']['image']
            if sakha_press_image == 'have':
                photo = open('content/sakha_press_image.jpg', 'rb')
                bot.send_photo(chat_id=chanel_id, photo=photo)
                bot.send_message(chat_id=chanel_id, text=sakha_press_text)
            else:
                bot.send_message(chat_id=chanel_id, text = sakha_press_text )
        
        sakha_news_text = all_info_dict['sakha_news']['text']
        if 'Error' in sakha_news_text:
            print(sakha_day_text)
        else:
            sakha_news_image = all_info_dict['sakha_news']['image']
            if sakha_news_image == 'have':
                photo = open('content/sakha_news_image.jpg', 'rb')
                bot.send_photo(chat_id=chanel_id, photo=photo)
                bot.send_message(chat_id=chanel_id, text=sakha_news_text)
            else:
                bot.send_message(chat_id=chanel_id, text = sakha_news_text )


        sleep(1800)



if __name__ == '__main__':
    bot.infinity_polling()