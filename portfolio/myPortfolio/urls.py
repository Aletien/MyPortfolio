from django.contrib import admin
from django.urls import path, include
#from myPortfolio.views import home
from . import views

#Django admin header customization
admin.site.site_header = "AllanBakwanamaha Dev"
admin.site.site_title = "Welcome to this Portal"
admin.site.index_title = "Welcome to Allan's Dashboard"

urlpatterns = [
    path('', views.home, name='home'),
]