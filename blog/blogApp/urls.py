from django.urls import path
from .views import home, post

urlpatterns = [
    path('home/', home, name="home"),
    path('blog/<slug:url>', post)
]



