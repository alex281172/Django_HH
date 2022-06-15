from django.urls import path
from parserhhapp import views



app_name = 'parserhhapp'

urlpatterns = [
    path('', views.create_pars, name='data'),
    path('index/', views.main_view, name='result'),
    # path('create/', views.create_pars, name='data'),
    path('post/<int:id>/', views.data_return, name='post'),
    path('city/', views.city_return, name='city'),
]

