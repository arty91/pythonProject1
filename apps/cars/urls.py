from django.urls import path

from .views import CarListCreateView, CarUpdateretrieveDestroyView

urlpatterns = [
	path('', CarListCreateView.as_view()),
	path('/<int:pk>', CarUpdateretrieveDestroyView.as_view())
]
