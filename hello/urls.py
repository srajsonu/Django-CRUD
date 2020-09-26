from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name='hello'
urlpatterns = [
    path('', TemplateView.as_view(template_name='hello/main.html')),
    path('hello', views.cookie),
    path('polls', views.session),
    path('polls/owner', views.owner),
]