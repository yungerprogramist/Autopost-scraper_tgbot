import datetime

def create_dict(post_list):
    post_dict = {'text': '', 'image' : ''}
    title = post_list[0]
    text = post_list[1]
    image = post_list[2]
    post_text = f'*{title}* \n\n {text}'
    if len(post_text) < 4095:
        post_dict['text']=post_text
        post_dict['image'] = image
    else: 
        post_dict['text'] = 'Error41 - большой текст с сайта sakha_day'
    return post_dict


def now_time():
    dt_now = datetime.datetime.now()
    dt_now_str = str(dt_now)
    dt_now_clear = dt_now_str.split('.')[0]
    return dt_now_clear