
from django.contrib import admin
from django.urls import path
from two import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.two)
]
