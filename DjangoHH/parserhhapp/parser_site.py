import requests
from collections import Counter
from operator import itemgetter
import json
from django.core.management.base import BaseCommand
from parserhhapp.models import Cities, Skills, CitiesSalary, SkillCloud
import pprint
from wordcloud import WordCloud
from stop_words import get_stop_words

from PIL import Image
import numpy as np

import matplotlib.pyplot as plt
from wordcloud import WordCloud



# Записываем в переменную стоп-слова русского языка
STOPWORDS_RU = get_stop_words('russian')


def parser_site(pages, proff, region):

    Cities.objects.all().delete()
    Skills.objects.all().delete()
    CitiesSalary.objects.all().delete()
    SkillCloud.objects.all().delete()

    DOMAIN = 'https://api.hh.ru/'
    url_vacancies = f'{DOMAIN}vacancies'


    my_skill_list = []
    my_city_list = []
    my_salary_list = []
    my_salary_list1 = []
    my_salary_list2 = []
    my_salary_list3 = []
    my_salary_list4 = []
    total_skill = []

    total_city = []
    total_city_sql = []
    main_count = 0


    if int(pages) < 20:
        pages = 20
    if int(pages) > 2000:
        pages = 2000
    page = int(int(pages) / 20)

    # Перебор страниц
    text = f'{proff} {region}'

    for page_count in range(page):

        print(f'Парсинг страницы {page_count + 1}')

        params = {
            'text': text,
            'page': page_count
        }
        page_count += 1
        vacancy_count = 0
        # Перебор 20 вакансий на странице
        for k in range(20):
            try:
                main_count += 1
                vacancy_count += 1
                # Счетчик - сколько ваканский спарсили на текущей странице
                print(vacancy_count)
                # Первичные данные с сайта полученные по запросу с заданными параметрами
                result = requests.get(url_vacancies, params=params).json()
                # Вытаскиваем нужный url (где есть skill) из rersult для дальнейшей обработки    # 'https://api.hh.ru/vacancies'
                # т.к. в удобном формате навыки находятся в другом месте
                url_skill = result['items'][k]['url']
                print(url_skill) #Ex.: https://api.hh.ru/vacancies/68618859?host=hh.ru


                #Вторичные данные с уточненного url где есть skill в удомном формате
                my_result = requests.get(url_skill).json()

                # print(result)
                # print(my_result)

                # Записываем Skill в список
                my_skill = my_result['key_skills'] #[{'name': 'Разработка ПО'}, {'name': 'Python'}, {'name': 'PostgreSQL'}]
                #print(my_skill)
                lens = len(my_skill)

                #переформатируем данные из {[]} в []
                if len(my_skill) != 0:
                    for counter in range(lens):
                        my_skill_list.append(my_skill[counter]['name']) #['Django Framework', 'Python', 'Django Rest Framework', 'Django']
                else:
                    pass

                my_address = my_result['area'] #{'id': '2', 'name': 'Санкт-Петербург', 'url': 'https://api.hh.ru/areas/2?host=hh.ru'}


                if my_address == None:
                    my_city = 'Неизвестно'
                else:
                    my_city = my_address['name']

                my_city_list.append(my_city) #формируем список городов, город может несколько раз быть в списке#['Алматы', 'Москва', 'Москва', 'Новосибирск']





                if result['items'][k]['salary'] == None or my_result['salary']['currency'] != 'RUR':
                    pass
                else:
                    if my_result['salary']['from'] != None and my_result['salary']['to'] != None:
                        pass
                    elif my_result['salary']['from'] != None and my_result['salary']['to'] == None:
                        my_result['salary']['to'] = my_result['salary']['from'] #если нет данных о зарплате ДО, то устанавливаем ее как ОТ
                    elif my_result['salary']['to'] != None and my_result['salary']['from'] == None:
                        my_result['salary']['from'] = my_result['salary']['to']#если нет данных о зарплате ОТ, то устанавливаем ее как ДО

                print(my_result['salary']['from'], my_result['salary']['to'])

                #формируем пробуем разные варианты списков с зарплатами
                if my_result['salary']['currency'] == 'RUR':
                    my_salary_list.append({'city': my_city, 'salary_from': my_result['salary']['from'],
                                       'salary_to': my_result['salary']['to']}) #[{'city': 'Йошкар-Ола', 'salary_from': 50000, 'salary_to': 200000},
                    my_salary_list1.append([my_city, my_result['salary']['from'], my_result['salary']['to']])#[['Йошкар-Ола', 50000, 200000],
                    aver_salary = (my_result['salary']['from'] + my_result['salary']['to']) / 2
                    my_salary_list2.append({my_city: aver_salary})#[{'Йошкар-Ола': 125000.0},
                    my_salary_list3.append({'name': my_city, 'aver': aver_salary})

            except:
                pass

    resultdict = {}  # результирующий словарь
    resultdict1 = {}

    for dictionary in my_salary_list2:  # пробегаем по списку словарей
        # print(dictionary)
        for key in dictionary:  # пробегаем по ключам словаря
            # print(key)
            try:
                resultdict[key] += dictionary[key]  # складываем значения
                resultdict1[key] += 1
                # print(resultdict[key])

            except KeyError:  # если ключа еще нет - создаем
                resultdict[key] = dictionary[key]
                # print(resultdict[key])
                resultdict1[key] = 1

    for dictionary in resultdict:
        resultdict[dictionary] = (int(resultdict[dictionary] / resultdict1[dictionary]))

    for key in resultdict:
        my_salary_list4.append({'name': key, 'aver': resultdict[key]})



    lens_skill_list = len(my_skill_list)
    lens_my_city_list = len(my_city_list)

    #модифицируем списки (подсчитываем количество) в новые
    modify_skill_list = Counter(my_skill_list)#Counter({'Python': 18,
    modify_my_city_list = Counter(my_city_list)#Counter({'Москва': 10,

    # pprint.pprint(modify_skill_list)
    # pprint.pprint(modify_my_city_list)


    lens_end_skill = len(modify_skill_list)
    lens_end_city = len(modify_my_city_list)

    #подсчитываем доли каждого навыка и формируем новый список
    for counter in range(lens_end_skill):
        name = list(modify_skill_list.keys())[counter]
        count = list(modify_skill_list.values())[counter]
        path = count / lens_skill_list
        percent = '{percent:.1%}'.format(percent=path)
        total_skill.append({'name': name, 'percent': percent, 'count': count})#[{'count': 4, 'name': 'Django Framework', 'percent': '3.6%'},

    #сортируем новый список по возрастанию
    total_skill = (sorted(total_skill, key=itemgetter('count'), reverse=True))#[{'count': 18, 'name': 'Python', 'percent': '16.4%'}

    for counter1 in total_skill:
        name = counter1['name']
        percent = counter1['percent']
        count = counter1['count']
        # new = f'{name} {percent} {count}'
        # new_new.append(new)
        # total_skill_current = (name, percent, count)
        # total_skill_sql.append(total_skill_current)

        Skills.objects.create(name=name, count=count, percent=percent)

    result_skill = {
        'keywords': proff,
        'count': str(lens_end_skill),
        'requirements': total_skill
    }
    result_skill_json = json.dumps(result_skill, ensure_ascii=False, indent=4)

    # подсчитываем доли каждого города и формируем новый список
    for counter in range(lens_end_city):
        name = list(modify_my_city_list.keys())[counter]
        count = list(modify_my_city_list.values())[counter]
        path = count / lens_my_city_list
        percent = '{percent:.1%}'.format(percent=path)
        total_city.append({'name': name, 'percent': percent, 'count': count})
        total_city_current = (name, percent, count)
        total_city_sql.append(total_city_current)

    # pprint.pprint(total_city)

    list6 = []

    # for counter in list5:
    #     for counter1 in counter.keys():
    #         if counter1 == 'name':
    #             print(counter[counter1])
    for counter in my_salary_list4:  # перебираем словари списока 1
        # print(counter.get('name'))
        for counter1 in total_city:
            if counter.get('name') == counter1.get('name'):
                # print(counter1.get('name'))
                # print(counter.get('aver'))
                list6.append({'aver': counter.get('aver'), 'name': counter1.get('name'), 'count': counter1.get('count'),
                              'percent': counter1.get('percent')})

    pprint.pprint(list6) #[{'aver': 125000, 'count': 1, 'name': 'Йошкар-Ола', 'percent': '2.5%'},


    # сортируем новый список по возрастанию
    total_city = (sorted(total_city, key=itemgetter('count'), reverse=True))#[{'count': 10, 'name': 'Москва', 'percent': '50.0%'},
    list6 = (sorted(list6, key=itemgetter('aver'), reverse=True))
    pprint.pprint(list6)


    for counter1 in total_city:
        name = counter1['name']
        percent = counter1['percent']
        count = counter1['count']

        Cities.objects.create(name=name, count=count, percent=percent)

    for counter1 in list6:

        name = counter1['name']
        percent = counter1['percent']
        count = counter1['count']
        aver = counter1['aver']
        CitiesSalary.objects.create(name=name, count=count, percent=percent, salary=aver)

    text_skills = str()
    text_cities = str()

    for skills in my_skill_list:
        text_skills = text_skills + ' ' + skills

    for cities in my_city_list:
        text_cities = text_cities + ' ' + cities


    print(text_skills)
    print(text_cities)

    mask = np.array(Image.open(f'media/oval.png'))
    # x, y = np.ogrid[:300, :300]
    # mask = (x - 150) ** 2 + (y - 150) ** 2 > 130 ** 2
    # mask = 255 * mask.astype(int)

    # Генерируем облако слов
    wordcloud = WordCloud(
                        # width=1200,
                        # height=800,
                        # random_state=1,
                        background_color='white',
                        # margin=20,
                        # colormap='Pastel1',
                        collocations=True,
                        stopwords = STOPWORDS_RU,
                        mask = mask).generate(text_skills)

    wordcloud.to_file(f'media/cloud1.png')

    def plot_cloud(wordcloud):
        # Устанавливаем размер картинки
        plt.figure(figsize=(40, 30))
        # Показать изображение
        plt.imshow(wordcloud)
        # Без подписей на осях
        plt.axis("off")

    # Рисуем картинку
    plot_cloud(wordcloud)

    # Генерируем облако слов
    wordcloud_black = WordCloud(
                        # width=1200,
                        # height=800,
                        # random_state=1,
                        background_color='white',
                        # margin=20,
                        contour_color='black',
                        contour_width = 3,
                        # colormap='Pastel2',
                        collocations=True,
                        stopwords = STOPWORDS_RU).generate(text_cities)

    wordcloud_black.to_file(f'media/cloud2.png')

    SkillCloud.objects.create(cover='cloud2.png', book='cloud1.png')
