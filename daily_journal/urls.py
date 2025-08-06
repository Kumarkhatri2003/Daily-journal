
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from journal import views as journal_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('',include('journal.urls')),

    #Authentic
]
