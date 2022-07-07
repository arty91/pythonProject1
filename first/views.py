from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request


class FirstView(APIView):
	def get(self, request):
		return Response('method GET used')

	def post(self, request):
		return Response('method POST used')

	def put(self, request):
		return Response('method PUT used')

	def patch(self, request):
		return Response('method PATCH used')

	def delete(self, request):
		return Response('method DELETE used')


class SecondView(APIView):
	def get(self, *args, **kwargs):
		query_params = self.request.query_params.dict()
		print(query_params)
		return Response(query_params)


class ThirdView(APIView):
	def get(self, *args, **kwargs):
		print(kwargs)
		return Response(kwargs)
