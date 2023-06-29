from django.urls import path
from .views import ImageProcessSet, HomepageRender

app_anme = "images_app"

urlpatterns = [
    path('', HomepageRender, name="homepage"),
    path('process_image/', ImageProcessSet.as_view(), name="process_image"),
]
