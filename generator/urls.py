from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
]
urlpatterns += [
    path('verse', views.display_verse, name='display-verse'),
]