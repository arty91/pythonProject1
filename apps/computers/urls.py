from django.urls import path

from .views import ComputerListCreateView, ComputerUpdateretrieveDestroyView

urlpatterns = [
	path('', ComputerListCreateView.as_view()),
	path('/<int:pk>', ComputerUpdateretrieveDestroyView.as_view())
]