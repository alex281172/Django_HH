from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from parserhhapp.models import Cities, Skills
from parserhhapp.forms import RequestForm, PostForm
from parserhhapp.parser_site import parser_site
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.cache import cache




# Create your views here
def main_view(request):

    skills = cache.get('skills')
    if not skills:
        skills = Skills.objects.all()
        cache.set('skills', skills, 60)

    paginator = Paginator(skills, 5)

    page = request.GET.get('page')
    try:
        skills = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        skills = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        skills = paginator.page(paginator.num_pages)

    title = 'навыки'

    return render(request, 'parserhhapp/index.html', context={'skills': skills, 'title': title})

def city_return(request):
    cities = cache.get('cities')
    if not cities:
        cities = Cities.objects.all()
        cache.set('cities', cities, 60)

    paginator_city = Paginator(cities, 5)

    page = request.GET.get('page')
    try:
        cities = paginator_city.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        cities = paginator_city.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        cities = paginator_city.page(paginator_city.num_pages)

    title = 'города'

    return render(request, 'parserhhapp/citycoat.html', context={'cities': cities, 'title': title})
#создание формы
# получение данных если запрос POST, если нет, то отрисовка снова пустой формы,
# если да проверка на валидность, если норм, то заполнение данными если нет,
# то отрисока пустой формы

@login_required
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
            title = '5'
            return render(request, 'parserhhapp/create.html', context={'form': form, 'title': title})
    else:
        form = RequestForm()
        title = 'запрос'
        return render(request, 'parserhhapp/create.html', context={'form': form, 'title': title})



def data_return(request, id):
    data = get_object_or_404(Skills, id=id)
    title = 'статистика'
    return render(request, 'parserhhapp/post.html', context={'data': data, 'title': title})

@user_passes_test(lambda u: u.is_superuser)
def create_post(request):
    if request.method == 'GET':
        form = PostForm()
        title = 'новый город'
        return render(request, 'parserhhapp/posts.html', context={'form': form, 'title': title})
    else:
        form = PostForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('parser:city'))
        else:
            return render(request, 'parserhhapp/posts.html', context={'form': form})


class SkillListView(LoginRequiredMixin, ListView):
    model = Skills
    template_name = 'parserhhapp/skill_list.html'
    paginate_by = 5

class SkillDetailView(LoginRequiredMixin, DetailView):
    model = Skills
    template_name = 'parserhhapp/skill_list_detail.html'
    paginate_by = 5


class SkillCreateView(LoginRequiredMixin, CreateView):
    fields = '__all__'
    model = Skills
    success_url = reverse_lazy('parser:skill_list')
    template_name = 'parserhhapp/skill_list_create.html'
    paginate_by = 5


class SkillUpdateView(LoginRequiredMixin, UpdateView):
    fields = '__all__'
    model = Skills
    success_url = reverse_lazy('parser:skill_list')
    template_name = 'parserhhapp/skill_list_create.html'
    paginate_by = 5


class SkillDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'parserhhapp/skill_list_delete_confirm.html'
    model = Skills
    success_url = reverse_lazy('parser:skill_list')
    paginate_by = 5



class CityListView(LoginRequiredMixin, ListView):
    model = Cities
    template_name = 'parserhhapp/city_list.html'
    paginate_by = 5


class CityDetailView(LoginRequiredMixin, DetailView):
    model = Cities
    template_name = 'parserhhapp/city_list_detail.html'
    paginate_by = 5

class CityCreateView(LoginRequiredMixin, CreateView):
    fields = '__all__'
    model = Cities
    success_url = reverse_lazy('parser:city_list')
    template_name = 'parserhhapp/city_list_create.html'
    paginate_by = 5

class CityUpdateView(LoginRequiredMixin, UpdateView):
    fields = '__all__'
    model = Cities
    success_url = reverse_lazy('parser:city_list')
    template_name = 'parserhhapp/city_list_create.html'
    paginate_by = 5

class CityDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'parserhhapp/city_list_delete_confirm.html'
    model = Cities
    success_url = reverse_lazy('parser:city_list')
    paginate_by = 5


class SimpleMainAjax(TemplateView):
    template_name = 'parserhhapp/simple.html'

