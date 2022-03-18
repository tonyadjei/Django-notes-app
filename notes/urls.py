from django.urls import path
from . import views

# namespacing our urls by using the built-in app_name variable
app_name = 'notes'

urlpatterns = [
    path('', views.note_list, name="list"),
    path('create/', views.note_create, name="create"),
    path('<slug:slug>/', views.note_detail, name="detail"),
]
