from distutils.command.build_scripts import first_line_re
from rest_framework import serializers
from .models import User

class CustomUserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')
        read_only_fields = ('email',)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'age', 'bio'
        'birth_place', 'school', 'occupation', 'what_are_you_seeking_on_site',
        'is_active')