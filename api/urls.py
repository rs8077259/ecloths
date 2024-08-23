from django.urls import path
from .views import ClothListView,ProductView

urlpatterns = [
    path('man/',view=ClothListView.as_view()),
    path('man/<fit>/<id>',view=ProductView.as_view())
]