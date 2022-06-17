from django import forms
from parserhhapp.models import Cities, Skills


class RequestForm(forms.Form):

    vacancy = forms.CharField(label='Профессия для парсинга', widget=forms.TextInput(attrs={'placeholder': 'профессия для парсинга', 'class': 'form-control', }))
    city = forms.CharField(label='Город для парсинга*', required=False, widget=forms.TextInput(attrs={'placeholder': 'название города', 'class': 'form-control', }))
    size = forms.IntegerField(label='Количество вакансий**', widget=forms.TextInput(attrs={'placeholder': 'количество вакансий', 'class': 'form-control', }))
    #
    # class Meta:
    #     model = Skills
    #     fields = '__all__'
    #     # exclude = ('image',)


class PostForm(forms.ModelForm):
    # name = forms.CharField(label='Город')
    name = forms.CharField(label='Город', widget=forms.TextInput(attrs={'placeholder': 'название города', 'class': 'form-control', }))
    percent = forms.CharField(label='доля', widget=forms.TextInput(attrs={'placeholder': 'доля в %', 'class': 'form-control', }))
    count = forms.IntegerField(label='количество', widget=forms.TextInput(attrs={'placeholder': 'количество', 'class': 'form-control', }))

    class Meta:
        model = Cities
        # fields = '__all__'
        exclude = ('image',)


class SkillForm(forms.Form):

    class Meta:
        model = Skills
        fields = '__all__'
