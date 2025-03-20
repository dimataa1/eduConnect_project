from rest_framework import serializers

from accounts.models import Profile


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = ['id', 'profile_picture', 'first_name', 'last_name']