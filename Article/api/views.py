from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from account.models import Account
from Article.models import PetPost
from Article.api.serializers import PetPostSerializer

SUCCESS = 'success'
ERROR = 'error'
DELETE_SUCCESS = 'deleted'
UPDATE_SUCCESS = 'updated'
CREATE_SUCCESS = 'created'


@api_view(['GET', ])
def api_detail_pet_view(request, slug):

	try:
		pet_post = PetPost.objects.get(slug=slug)
	except PetPost.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = PetPostSerializer(pet_post)
		return Response(serializer.data)


@api_view(['PUT', ])
def api_update_pet_view(request, slug):

	try:
		pet_post = PetPost.objects.get(slug=slug)
	except PetPost.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'PUT':
		serializer = PetPostSerializer(pet_post, data=request.data)
		data = {}
		if serializer.is_valid():
			serializer.save()
			data[SUCCESS] = UPDATE_SUCCESS
			return Response(data=data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', ])
def api_delete_pet_view(request, slug):

	try:
		pet_post = PetPost.objects.get(slug=slug)
	except PetPost.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'DELETE':
		operation = pet_post.delete()
		data = {}
		if operation:
			data[SUCCESS] = DELETE_SUCCESS
		return Response(data=data)


@api_view(['POST'])
def api_create_pet_view(request):

	account = Account.objects.get(pk=1)

	pet_post = PetPost(author=account)

	if request.method == 'POST':
		serializer = PetPostSerializer(pet_post, data=request.data)
		data = {}
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
