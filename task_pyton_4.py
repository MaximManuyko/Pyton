#Изучите содержимое и импортируйте модуль this.py

import this


#1. Найдите пакет http(относится к Стандартной библиотеке), изучите модули, из которых он состоит.

import http
help('http')

from http import client

if __name__ == '__main__':
    # 3.1. Создаем соединение по адресу 'www.google.com'
    # Для этого обращаемся к модулю client
    # И вызываем конструктор класса HTTPConnection()
    connection = client.HTTPConnection('www.google.com')
    # 3.2. Отправляем GET запрос к корневой странице веб-сервера
    connection.request('GET', '/')
    # 3.3. Получаем ответ на наш запрос
    res = connection.getresponse()
    # Из полного ответа достаем интересующую нас веб-страницу(ее HTML код)
    page = res.read()
    print(page)
