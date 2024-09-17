from django.urls import path
from .import views
from .views import generate_qr_code
from .views import anonymous_access_page  # Import the view function

urlpatterns = [
    path('home', views.home_page, name='home'),
    path('generate-qr/', generate_qr_code, name='generate_qr_code'),
    path('anonymous/', anonymous_access_page, name='anonymous_access_page'),

]



