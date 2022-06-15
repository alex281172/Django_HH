from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse

from parserhhapp.models import Cities, Skills
from parserhhapp.forms import RequestForm
from parserhhapp.parser_site import parser_site


# Create your views here
def main_view(request):
    cities = Cities.objects.all()
    skills = Skills.objects.all()
    return render(request, 'parserhhapp/index.html', context={'cities': cities, 'skills': skills})


def create_pars(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)

        if form.is_valid():
            region = form.cleaned_data['city']
            pages = form.cleaned_data['size']
            proff = form.cleaned_data['vacancy']
            parser_site(pages, proff, region)


            return HttpResponseRedirect(reverse('parser:result'))

        else:
            return render(request, 'parserhhapp/create.html', context={'form': form})
    else:
        pass
        form = RequestForm()
        return render(request, 'parserhhapp/create.html', context={'form': form})


def city_return(request):
    cities = Cities.objects.all()
    return render(request, 'parserhhapp/citycoat.html', context={'cities': cities})

def data_return(request, id):
    data = get_object_or_404(Skills, id=id)
    return render(request, 'parserhhapp/post.html', context={'data': data})

