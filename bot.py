import telebot 
from handler import main
from time import sleep
from some_functions import now_time

from dotenv import load_dotenv
import os 

load_dotenv()

bot = telebot.TeleBot (os.getenv('BOT_TOKEN')) 
chanel_id = '@test_chanel_023'
# chanel_id = '-1812773259'


@bot.message_handler(commands=['start'])
def start(message):
    print('works') 
    chat_bot_id = message.chat.id
    
    bot.send_message(chat_id=chat_bot_id, text= f'бот успешно запущен \n{now_time()}')

    while True:
        dt_time = now_time()

        bot.send_message(chat_id=chat_bot_id, text = f'===================================================\nБот начинает выполнение работы \n {dt_time}\n ===================================================')

        all_info_dict = main()
        sakha_day_text = all_info_dict['sakha_day']['text']
        if 'Error' in sakha_day_text:
            print(sakha_day_text)
            bot.send_message(chat_id=chat_bot_id, text=sakha_day_text)
        else:
            sakha_day_image = all_info_dict['sakha_day']['image']
            if sakha_day_image == 'have':
                photo = open('content/sakha_day_image.jpg', 'rb')
                bot.send_photo(chat_id=chanel_id, photo=photo)
                bot.send_message(chat_id=chanel_id, text=sakha_day_text)
            else:
                bot.send_message(chat_id=chanel_id, text = sakha_day_text )
            bot.send_message(chat_id=chat_bot_id, text = f'Новость с сайта sakha_day успешно выложенна \n {dt_time}')


        sakha_press_text = all_info_dict['sakha_press']['text']
        if 'Error' in sakha_press_text:
            print(sakha_press_text)
            bot.send_message(chat_id=chat_bot_id, text=sakha_press_text)
        else:
            sakha_press_image = all_info_dict['sakha_press']['image']
            if sakha_press_image == 'have':
                photo = open('content/sakha_press_image.jpg', 'rb')
                bot.send_photo(chat_id=chanel_id, photo=photo)
                bot.send_message(chat_id=chanel_id, text=sakha_press_text)
            else:
                bot.send_message(chat_id=chanel_id, text = sakha_press_text )
            bot.send_message(chat_id=chat_bot_id, text = f'Новость с сайта sakha_press успешно выложенна \n {dt_time}')
        
        sakha_news_text = all_info_dict['sakha_news']['text']
        if 'Error' in sakha_news_text:
            print(sakha_news_text)
            bot.send_message(chat_id=chat_bot_id, text=sakha_news_text)
        else:
            sakha_news_image = all_info_dict['sakha_news']['image']
            if sakha_news_image == 'have':
                photo = open('content/sakha_news_image.jpg', 'rb')
                bot.send_photo(chat_id=chanel_id, photo=photo)
                bot.send_message(chat_id=chanel_id, text=sakha_news_text)
            else:
                bot.send_message(chat_id=chanel_id, text = sakha_news_text )
            bot.send_message(chat_id=chat_bot_id, text = f'Новость с сайта sakha_news успешно выложенна \n {dt_time}')

        yakytia_text = all_info_dict['yakytia']['text']
        if 'Error' in yakytia_text:
            print(yakytia_text)
            bot.send_message(chat_id=chat_bot_id, text=yakytia_text)
        else:
            yakytia_image = all_info_dict['yakytia']['image']
            if yakytia_image == 'have':
                photo = open('content/yakytia24_image.jpg', 'rb')
                bot.send_photo(chat_id=chanel_id, photo=photo)
                bot.send_message(chat_id=chanel_id, text=yakytia_text)
            else:
                bot.send_message(chat_id=chanel_id, text = yakytia_text )
            bot.send_message(chat_id=chat_bot_id, text = f'Новость с сайта yakytia24 успешно выложенна \n {dt_time}')

        bot.send_message(chat_id=chat_bot_id, text = f'===================================================\nБот закончил выполнение работы \n {dt_time}\n ===================================================')

        sleep(1800)





if __name__ == '__main__':
    bot.infinity_polling()