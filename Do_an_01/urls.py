from django.urls import path
from Do_an_01 import views
from django.conf.urls.static import static
from django.conf import settings
app_name = 'Do_an_01'
urlpatterns = [
    path('Masterbase.html', views.Masterbase),
    path('', views.index, name='index'),
    path('single/<int:pk>/', views.single, name='single'),
    path('book/<int:pk>/', views.book, name='book'),
    path('category/<int:pk>/', views.category, name='category'),
    path('search/', views.search, name='search'),
    path('contact/', views.contact_hdg, name='contact'),
    path('storys_service/', views.storys_service, name='storys_service'),
    path('story_service/<int:pk>/', views.story_service, name='story_service'),

]
