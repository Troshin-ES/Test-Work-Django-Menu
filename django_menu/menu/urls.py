from django.urls import path
from menu.views import index
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index/index.html'), name='index')
]
