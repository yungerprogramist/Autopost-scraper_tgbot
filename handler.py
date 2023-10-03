from sch_day.sakhaday import sakha_day
from sch_pres.sakhapress import sakha_press
from sch_news.sakhanews import sakha_news
from yakytia24.yk24 import yakytia24

from some_functions import create_dict 


def main():
    content_dict ={
        'sakha_day' : {'text' : ''},
        'sakha_press' : {'text' : ''},
        'sakha_news' : {'text' : ''},
        'yakytia' : {'text' : ''},
    }

    #https://sakhaday.ru/
    sakha_d = sakha_day()
    if 'Error' in sakha_d :
        print(sakha_d)
        content_dict['sakha_day']['text']=  sakha_d
    else:
        sakha_day_info = create_dict(sakha_d)
        content_dict['sakha_day'] = sakha_day_info



    # https://sakhapress.ru/
    sakha_pr = sakha_press()
    if 'Error' in sakha_pr:
        print(sakha_pr)
        content_dict['sakha_press']['text']=  sakha_pr
    else:
        sakha_press_info = create_dict(sakha_pr)
        content_dict['sakha_press'] = sakha_press_info

    # https://1sn.ru/
    sakha_n = sakha_news()
    if 'Error' in sakha_n:
        print(sakha_n)
        content_dict['sakha_news']['text']= sakha_n
    else:
        sakha_news_info = create_dict(sakha_n)
        content_dict['sakha_news'] = sakha_news_info

    # https://yk24.ru/category/main/
    yakytia = yakytia24()
    if 'Error' in yakytia :
        print(yakytia)
        content_dict['yakytia']['text']=  yakytia
    else:
        yakytia_info = create_dict(yakytia)
        content_dict['yakytia'] = yakytia_info

    return content_dict
        
    
