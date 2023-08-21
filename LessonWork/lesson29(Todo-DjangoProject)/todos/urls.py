from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),


    #Auth
    path('signup/', views.signupuser, name='signup'),
    # path('login/', views.loginuser, name='login'),

    #Todos
    path('current/', views.current_todos, name='current'),
]
