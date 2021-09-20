
from django.urls import path
from app import views

urlpatterns = [
    path('', views.home,name='home_page'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('logout', views.logout, name='logout'),
    path('add-todo', views.add_todo, name='add_todo'),
    path('delete_todo/<int:id>', views.delete_todo, name='delete_todo'),
    path('change_status/<int:id>/<str:status>', views.change_status, name='change_status'),
]
