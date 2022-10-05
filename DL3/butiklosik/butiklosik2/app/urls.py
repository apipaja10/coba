from django.urls import path
from . import views

urlpatterns = [
    path('pelanggan',views.pelanggan, name='pelanggan'),
    path('createdata',views.createdata, name='createdata'),

]