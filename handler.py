from sch_day.sakhaday import sakha_day
from sch_pres.sakhapress import sakha_press
from sch_news.sakhanews import sakha_news



def main():
    content_dict ={
        'sakha_day' : {'text': '', 'image' : ''},
        'sakha_press' : {'text': '', 'image' : ''},
        'sakha_news' : {'text': '', 'image' : ''},
    }

    #https://sakhaday.ru/
    sakha_d = sakha_day()
    if 'Error' in sakha_d :
        print(sakha_d)
        content_dict['sakha_day']['text']=  sakha_d
    else:
        sakha_day_title = sakha_d[0]
        sakha_day_text = sakha_d[1]
        post_text = f'*{sakha_day_title}* \n\n {sakha_day_text}'
        if len(post_text) < 4095:
            content_dict['sakha_day']['text']=post_text

            image = sakha_d[2]
            content_dict['sakha_day']['image'] = image
                
        else:
            print('Error41 - большой текст с сайта sakha_day')
            content_dict['sakha_day']['text']='Error41 - большой текст с сайта sakha_day'


    # https://sakhapress.ru/
    sakha_pr = sakha_press()
    if 'Error' in sakha_pr:
        print(sakha_pr)
        content_dict['sakha_press']['text']=  sakha_pr
    else:
        sakha_press_title = sakha_pr[0]
        sakha_press_text = sakha_pr[1]
        post_text = f'*{sakha_press_title}* \n\n {sakha_press_text}'
        if len(post_text) < 4095:
            content_dict['sakha_press']['text']=post_text

            image = sakha_pr[2]
            content_dict['sakha_press']['image'] = image
        else:
            print('Error42 - большой текст с сайта sakha_press')
            content_dict['sakha_press']['text']= 'Error42 - большой текст с сайта sakha_press'

        
        
    # https://1sn.ru/
    sakha_n = sakha_news()
    if 'Error' in sakha_n:
        print(sakha_n)
        content_dict['sakha_news']['text']= sakha_n
    else:
        sakha_news_title = sakha_n[0]
        sakha_news_text = sakha_n[1]
        post_text = f'{sakha_news_title} \n\n {sakha_news_text}'
        if len(post_text) < 4095:
            content_dict['sakha_news']['text']=post_text

            image = sakha_n[2]
            content_dict['sakha_news']['image'] = image
        else:
            print('Error43 - большой текст с сайта sakha_news')
            content_dict['sakha_news']['text']='Error43 - большой текст с сайта sakha_news'

    return content_dict
        
    
