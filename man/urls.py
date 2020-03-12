from django.urls import include, path
from .views import CategoryView

app_name = 'Time Manager'

urlpatterns = [

    path('get/', CategoryView.as_view()),
    path('get/<int:pk>', CategoryView.as_view()),
]