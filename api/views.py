from urllib import response
from .models import User
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_auth.registration.views import RegisterView


class CustomRegisterView(RegisterView):
    queryset = User.objects.all()

class UserAPIView(APIView):
    @staticmethod
    def get(request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return response(serializer.data)

class GenericUserAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                        mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
        
    def post(self, request):
        return self.create(request)
    
    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)