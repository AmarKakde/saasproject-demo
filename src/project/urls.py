from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.return_view),
    path('admin/', admin.site.urls),
    path('page/', view=views.return_view),
]
