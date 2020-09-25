from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name='hello'
urlpatterns = [
    path('', TemplateView.as_view(template_name='hello/main.html')),
<<<<<<< HEAD
    path('polls', views.cookie),
    path('hello', views.session),
=======
    path('hello', views.cookie),
    path('polls', views.session),
>>>>>>> a1df82a655cd5c2c771671884cae21b45a8c3a87
    path('polls/owner', views.owner),
]
