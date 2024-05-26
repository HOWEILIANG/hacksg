from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("dont_be_evil/", admin.site.urls),
    path('', include('dbschallenge.urls'))
]
