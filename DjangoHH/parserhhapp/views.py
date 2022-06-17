from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from parserhhapp.models import Cities, Skills
from parserhhapp.forms import RequestForm, PostForm
from parserhhapp.parser_site import parser_site


# Create your views here
def main_view(request):
    cities = Cities.objects.all()
    skills = Skills.objects.all()
    return render(request, 'parserhhapp/index.html', context={'cities': cities, 'skills': skills})


#создание формы
# получение данных если запрос POST, если нет, то отрисовка снова пустой формы,
# если да проверка на валидность, если норм, то заполнение данными если нет,
# то отрисока пустой формы


def create_pars(request):
    if request.method == 'POST':
        # form = RequestForm(request.POST)
        form = RequestForm(request.POST, files=request.FILES)

        if form.is_valid():
            region = form.cleaned_data['city']
            pages = form.cleaned_data['size']
            proff = form.cleaned_data['vacancy']
            parser_site(pages, proff, region)
            return HttpResponseRedirect(reverse('parser:result'))

        else:
            return render(request, 'parserhhapp/create.html', context={'form': form})
    else:
        form = RequestForm()
        return render(request, 'parserhhapp/create.html', context={'form': form})


def city_return(request):
    cities = Cities.objects.all()
    return render(request, 'parserhhapp/citycoat.html', context={'cities': cities})


def data_return(request, id):
    data = get_object_or_404(Skills, id=id)
    return render(request, 'parserhhapp/post.html', context={'data': data})


def create_post(request):
    if request.method == 'GET':
        form = PostForm()
        return render(request, 'parserhhapp/posts.html', context={'form': form})
    else:
        form = PostForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('parser:city'))
        else:
            return render(request, 'parserhhapp/posts.html', context={'form': form})


class SkillListView(ListView):
    model = Skills
    template_name = 'parserhhapp/skill_list.html'

class SkillDetailView(DetailView):
    model = Skills
    template_name = 'parserhhapp/skill_list_detail.html'


class SkillCreateView(CreateView):
    fields = '__all__'
    model = Skills
    success_url = reverse_lazy('parser:skill_list')
    template_name = 'parserhhapp/skill_list_create.html'


class SkillUpdateView(UpdateView):
    fields = '__all__'
    model = Skills
    success_url = reverse_lazy('parser:skill_list')
    template_name = 'parserhhapp/skill_list_create.html'

class SkillDeleteView(DeleteView):
    template_name = 'parserhhapp/skill_list_delete_confirm.html'
    model = Skills
    success_url = reverse_lazy('parser:skill_list')



class CityListView(ListView):
    model = Cities
    template_name = 'parserhhapp/city_list.html'


class CityDetailView(DetailView):
    model = Cities
    template_name = 'parserhhapp/city_list_detail.html'

class CityCreateView(CreateView):
    fields = '__all__'
    model = Cities
    success_url = reverse_lazy('parser:city_list')
    template_name = 'parserhhapp/city_list_create.html'

class CityUpdateView(UpdateView):
    fields = '__all__'
    model = Cities
    success_url = reverse_lazy('parser:city_list')
    template_name = 'parserhhapp/city_list_create.html'

class CityDeleteView(DeleteView):
    template_name = 'parserhhapp/city_list_delete_confirm.html'
    model = Cities
    success_url = reverse_lazy('parser:city_list')
