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

class CustomRegisterSerializer(RegisterSerializer):
    email = serializers.EmailFiels(required=True)
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    age = serializers.DateField(required=True)

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()

        return {
            'password': self.validated_data.get('password', ''),
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'age': self.validated_data.get('age', ''),
        }