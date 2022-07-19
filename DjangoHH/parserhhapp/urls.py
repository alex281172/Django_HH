from django.urls import path
from parserhhapp import views



app_name = 'parserhhapp'

urlpatterns = [
    path('', views.create_pars, name='data'),
    path('index/', views.main_view, name='result'),
    path('post/<int:id>/', views.data_return, name='post'),
    path('city/', views.city_return, name='city'),
    path('posts/', views.create_post, name='post'),
    path('city_list/', views.CityListView.as_view(), name='city_list'),
    path('city_list_detail/<int:pk>/', views.CityDetailView.as_view(), name='city_list_detail'),
    path('city_list_create/', views.CityCreateView.as_view(), name='city_list_create'),
    path('city_list_update/<int:pk>/', views.CityUpdateView.as_view(), name='city_list_update'),
    path('city_list_delete/<int:pk>/', views.CityDeleteView.as_view(), name='city_list_delete'),
    path('skill_list/', views.SkillListView.as_view(), name='skill_list'),
    path('skill_list_detail/<int:pk>/', views.SkillDetailView.as_view(), name='skill_list_detail'),
    path('skill_list_create/', views.SkillCreateView.as_view(), name='skill_list_create'),
    path('skill_list_update/<int:pk>/', views.SkillUpdateView.as_view(), name='skill_list_update'),
    path('skill_list_delete/<int:pk>/', views.SkillDeleteView.as_view(), name='skill_list_delete'),
    path('simple/', views.SimpleMainAjax.as_view(), name='simple_ajax'),

]

