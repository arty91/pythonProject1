from rest_framework.serializers import ModelSerializer
from .models import CarModel


class CarSerializer(ModelSerializer):
	class Meta:
		model = CarModel
		# fields = '__all__'
		fields = ('id', 'brand', 'price', 'year')
