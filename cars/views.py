from rest_framework.views import APIView
from rest_framework.response import Response

from .models import CarModel
from .serializers import CarSerializer


class CarListCreateView(APIView):
	def get(self, *args, **kwargs):
		qs = CarModel.objects.all()  # request to db: select * from cars;
		serializer = CarSerializer(qs, many=True)
		return Response(serializer.data)

	def post(self, *args, **kwargs):
		data = self.request.data
		# instance = CarModel.objects.create(**data)
		serializer = CarSerializer(data=data)
		if not serializer.is_valid():
			return Response(serializer.errors)
		serializer.save()
		return Response(serializer.data)
