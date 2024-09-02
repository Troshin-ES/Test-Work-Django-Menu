from django.urls import path
from test_menu.views import index


urlpatterns = [
    path('', index, name='index')
]
