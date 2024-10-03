from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="main-page"),
    path("questions/<str:database>/", views.get_all_questions, name="questions-by-db"),
]
