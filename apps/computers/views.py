from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import ComputerModel
from .serializers import ComputerSerializer


class ComputerListCreateView(APIView):
	def get(self, *args, **kwargs):
		qs = ComputerModel.objects.all()
		serializer = ComputerSerializer(qs, many=True)
		return Response(serializer.data, status.HTTP_200_OK)

	def post(self, *args, **kwargs):
		data = self.request.data
		serializer = ComputerSerializer(data=data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data, status.HTTP_201_CREATED)


class ComputerUpdateretrieveDestroyView(APIView):
	def get(self, *args, **kwargs):
		computer_id = kwargs.get('pk')

		if not ComputerModel.objects.filter(pk=computer_id).exists():
			return Response('Computer with this id is not found.', status.HTTP_404_NOT_FOUND)

		computer = ComputerModel.objects.get(pk=computer_id)
		serializer = ComputerSerializer(computer)
		return Response(serializer.data, status.HTTP_200_OK)

	def put(self, *args, **kwargs):
		computer_id = kwargs.get('pk')
		data = self.request.data

		if not ComputerModel.objects.filter(pk=computer_id).exists():
			return Response('Computer with this id is not found.', status.HTTP_404_NOT_FOUND)

		computer = ComputerModel.objects.get(pk=computer_id)
		serializer = ComputerSerializer(computer, data)

		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data, status.HTTP_200_OK)

	def patch(self, *args, **kwargs):
		computer_id = kwargs.get('pk')
		data = self.request.data

		if not ComputerModel.objects.filter(pk=computer_id).exists():
			return Response('Computer with this id is not found.', status.HTTP_404_NOT_FOUND)

		computer = ComputerModel.objects.get(pk=computer_id)
		serializer = ComputerSerializer(computer, data, partial=True)

		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data, status.HTTP_200_OK)

	def delete(self, *args, **kwargs):
		computer_id = kwargs.get('pk')

		if not ComputerModel.objects.filter(pk=computer_id).exists():
			return Response('Computer with this id is not found.', status.HTTP_404_NOT_FOUND)

		computer = ComputerModel.objects.get(pk=computer_id)
		computer.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
