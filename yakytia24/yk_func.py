def check_title(title):
    try:
        file = open('yakytia24/yakytia.txt', encoding='utf-8')
        last_title = file.readline()
        if title in last_title:
            return True
        else:
            file = open('yakytia24/yakytia.txt', 'w', encoding='utf-8')
            file.write(title)
            return False
        
    except Exception as ex:
        print(ex)
        return f'Что-то пошло не так в функции Check_title на сайте sakha_day - '