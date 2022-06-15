from django import forms


class RequestForm(forms.Form):

    vacancy = forms.CharField(label='Профессия для парсинга')
    city = forms.CharField(label='Город для парсинга*', required=False)
    size = forms.IntegerField(label='Количество вакансий**')


