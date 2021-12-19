from django.urls import path
from customers_hdg import views
from django.conf.urls.static import static
from django.conf import settings
app_name = 'customers_hdg'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('my-account/', views.my_account, name='my_account'),
    path('logout/', views.logout, name='logout'),

]
