from django.urls import path
from .import views
import sys
urlpatterns = [
    path('', views.home, name="home"),
    path('pdf/', views.gen_pdf, name='pdf'),

]
print(sys.path)