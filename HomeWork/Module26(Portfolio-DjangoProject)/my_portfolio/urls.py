from django.contrib import admin
from django.urls import path
from about import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # About
    path('about/', views.about, name='about')
]
