from django.urls import path
from menu.views import index
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='test_html/main.html'), name='main'),
    path('contacts', TemplateView.as_view(template_name='test_html/contacts.html'), name='contacts'),
    path('content', TemplateView.as_view(template_name='test_html/content.html'), name='content'),
    path('messages', TemplateView.as_view(template_name='test_html/messages.html'), name='messages'),
    path('audio', TemplateView.as_view(template_name='test_html/audio.html'), name='audio'),
    path('audio_1', TemplateView.as_view(template_name='test_html/audio_1.html'), name='audio_1'),
    path('audio_1_1', TemplateView.as_view(template_name='test_html/audio_1_1.html'), name='audio_1_1'),
    path('audio_2', TemplateView.as_view(template_name='test_html/audio_2.html'), name='audio_2'),
    path('audio_2_1', TemplateView.as_view(template_name='test_html/audio_2_1.html'), name='audio_2_1'),
    path('audio_3', TemplateView.as_view(template_name='test_html/audio_3.html'), name='audio_3'),
    path('video', TemplateView.as_view(template_name='test_html/video.html'), name='video'),
    path('video_1', TemplateView.as_view(template_name='test_html/video_1.html'), name='video_1'),
    path('video_2', TemplateView.as_view(template_name='test_html/video_2.html'), name='video_2'),
    path('video_3', TemplateView.as_view(template_name='test_html/video_3.html'), name='video_3'),
    path('pictures', TemplateView.as_view(template_name='test_html/pictures.html'), name='pictures'),
    path('clips', TemplateView.as_view(template_name='test_html/clips.html'), name='clips'),
    path('game', TemplateView.as_view(template_name='test_html/game.html'), name='game'),
    path('game_1', TemplateView.as_view(template_name='test_html/game_1.html'), name='game_1'),
    path('eat', TemplateView.as_view(template_name='test_html/eat.html'), name='eat'),
    path('products', TemplateView.as_view(template_name='test_html/products.html'), name='products'),
    path('eat_1', TemplateView.as_view(template_name='test_html/eat_1.html'), name='eat_1'),
    path('water', TemplateView.as_view(template_name='test_html/water.html'), name='water'),
]
