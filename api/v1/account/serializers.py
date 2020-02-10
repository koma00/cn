from rest_framework import serializers
from account.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'date_of_birth', 'sex', 'photo')
