from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin

from .models import CarModel
from .serializers import CarSerializer


class CarListCreateView(GenericAPIView, CreateModelMixin, ListModelMixin):
	queryset = CarModel.objects.all()
	serializer_class = CarSerializer
	#
	def get(self, *args, **kwargs):
		return super().list(self.request, *args, **kwargs)

	# 	qs = self.get_queryset()
	#
	# 	# qs = qs.filter(price__gt=1000).order_by('-price', 'year')[:2]
	# 	# price_gt = self.request.query_params.get('price_gt')
	# 	# if price_gt:
	# 	# 	qs = qs.filter(price__gt=price_gt)
	# 	serializer = self.serializer_class(qs, many=True)
	# 	return Response(serializer.data, status.HTTP_200_OK)

	def post(self, *args, **kwargs):
		return super().create(self.request, *args, **kwargs)
# data = self.request.data
		# # instance = CarModel.objects.create(**data)
		# serializer = CarSerializer(data=data)
		# if not serializer.is_valid():
		# 	return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
		# serializer.save()
		# return Response(serializer.data, status.HTTP_201_CREATED)


class CarUpdateretrieveDestroyView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
	queryset = CarModel.objects.all()
	serializer_class = CarSerializer

	def get(self, *args, **kwargs):
		return super().retrieve(self.request, *args, **kwargs)

	# car_id = kwargs.get('pk')
		#
		# if not CarModel.objects.filter(pk=car_id).exists():
		# 	return Response('Car with this id is not found.', status.HTTP_404_NOT_FOUND)
		#
		# car = CarModel.objects.get(pk=car_id)

		# car = self.get_object()
		#
		# serializer = self.serializer_class(car)
		# return Response(serializer.data, status.HTTP_200_OK)

	def put(self, *args, **kwargs):
		return super().update(self.request, *args, **kwargs)

	# car_id = kwargs.get('pk')
		# data = self.request.data
		#
		# if not CarModel.objects.filter(pk=car_id).exists():
		# 	return Response('Car with this id is not found.', status.HTTP_404_NOT_FOUND)
		#
		# car = CarModel.objects.get(pk=car_id)
		# serializer = CarSerializer(car, data)
		#
		# # if not serializer.is_valid():
		# # 	return Response(serializer.errors)
		# # a shorter version below:
		# serializer.is_valid(raise_exception=True)
		# serializer.save()
		# return Response(serializer.data, status.HTTP_200_OK)

	def patch(self, *args, **kwargs):
		return super().partial_update(self.request, *args, **kwargs)

	# car_id = kwargs.get('pk')
		# data = self.request.data
		#
		# if not CarModel.objects.filter(pk=car_id).exists():
		# 	return Response('Car with this id is not found.', status.HTTP_404_NOT_FOUND)
		#
		# car = CarModel.objects.get(pk=car_id)
		# serializer = CarSerializer(car, data, partial=True)
		#
		# serializer.is_valid(raise_exception=True)
		# serializer.save()
		# return Response(serializer.data, status.HTTP_200_OK)

	def delete(self, *args, **kwargs):
		return super().destroy(self.request, *args, **kwargs)

# car_id = kwargs.get('pk')
		#
		# if not CarModel.objects.filter(pk=car_id).exists():
		# 	return Response('Car with this id is not found.', status.HTTP_404_NOT_FOUND)
		#
		# car = CarModel.objects.get(pk=car_id)
		# car.delete()
		# return Response(status=status.HTTP_204_NO_CONTENT)

