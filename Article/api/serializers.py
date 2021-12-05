from rest_framework import serializers

from Article.models import PetPost


class PetPostSerializer(serializers.ModelSerializer):
	class Meta:
		model = PetPost
		fields = ['title', 'body', 'image', ]
