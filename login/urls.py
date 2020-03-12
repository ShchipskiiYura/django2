from django.urls import include, path
# from .views import ExampleView


urlpatterns = [
    # path('users/', include('users.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    # path('login/', ExampleView.as_view()),
]