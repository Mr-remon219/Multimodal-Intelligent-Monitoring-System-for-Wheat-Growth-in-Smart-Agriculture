from django.urls import path
from web_page.views import index

urlpatterns = [
    path("", index, name="index"),
]
