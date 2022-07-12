from .models import ComputerModel
from rest_framework.serializers import ModelSerializer


class ComputerSerializer(ModelSerializer):
	class Meta:
		model = ComputerModel
		fields = ('id', 'brand', 'model', 'ram', 'monitor')
