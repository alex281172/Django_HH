import requests
from collections import Counter
from operator import itemgetter
import json
from django.core.management.base import BaseCommand
from parserhhapp.models import Cities, Skills



def parser_site(pages, proff, region):

    Cities.objects.all().delete()
    Skills.objects.all().delete()


    DOMAIN = 'https://api.hh.ru/'
    url_vacancies = f'{DOMAIN}vacancies'


    my_skill_list = []
    my_city_list = []
    total_skill = []
    total_skill_sql = []
    total_city = []
    total_city_sql = []
    main_count = 0
    new_new = []

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
                # Сколько ваканский спарсили на текущей странице
                print(vacancy_count)
                # Вытаскиваем нужный url (где есть skill) для дальнейшей обработки
                result = requests.get(url_vacancies, params=params).json()
                url_skill = result['items'][k]['url']
                my_result = requests.get(url_skill).json()
                # Записываем Skill в список
                my_skill = my_result['key_skills']
                lens = len(my_skill)

                if len(my_skill) != 0:
                    for counter in range(lens):
                        my_skill_list.append(my_skill[counter]['name'])
                else:
                    pass

                # my_name = my_result['name']
                my_address = my_result['area']
                if my_address == None:
                    my_city = 'Неизвестно'
                else:
                    my_city = my_address['name']

                my_city_list.append(my_city)
            except:
                pass

        # total_result = result['found']

    lens_skill_list = len(my_skill_list)
    lens_my_city_list = len(my_city_list)

    modify_skill_list = Counter(my_skill_list)
    modify_my_city_list = Counter(my_city_list)

    lens_end_skill = len(modify_skill_list)
    lens_end_city = len(modify_my_city_list)

    for counter in range(lens_end_skill):
        name = list(modify_skill_list.keys())[counter]
        count = list(modify_skill_list.values())[counter]
        path = count / lens_skill_list
        percent = '{percent:.1%}'.format(percent=path)
        total_skill.append({'name': name, 'percent': percent, 'count': count})

    total_skill = (sorted(total_skill, key=itemgetter('count'), reverse=True))



    for counter1 in total_skill:
        name = counter1['name']
        percent = counter1['percent']
        count = counter1['count']
        new = f'{name} {percent} {count}'
        new_new.append(new)
        total_skill_current = (name, percent, count)
        total_skill_sql.append(total_skill_current)

        Skills.objects.create(name=name, count=count, percent=percent)

    result_skill = {
        'keywords': proff,
        'count': str(lens_end_skill),
        'requirements': total_skill
    }
    result_skill_json = json.dumps(result_skill, ensure_ascii=False, indent=4)


    for counter in range(lens_end_city):
        name = list(modify_my_city_list.keys())[counter]
        count = list(modify_my_city_list.values())[counter]
        path = count / lens_my_city_list
        percent = '{percent:.1%}'.format(percent=path)
        total_city.append({'name': name, 'percent': percent, 'count': count})
        total_city_current = (name, percent, count)
        total_city_sql.append(total_city_current)





    total_city = (sorted(total_city, key=itemgetter('count'), reverse=True))


    for counter1 in total_city:
        name = counter1['name']
        percent = counter1['percent']
        count = counter1['count']

        Cities.objects.create(name=name, count=count, percent=percent)
