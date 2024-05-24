from rest_framework import views, status, response, \
    permissions, authentication
from .serializers import EmailSerializer
from django.contrib.auth import authenticate
from .models import Mail
from rest_framework.authtoken.models import Token


class LoginView(views.APIView):
    authentication_classes = [authentication.TokenAuthentication]

    def post(self, request):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return response.Response({'token': token.key})
        else:
            return response.Response({'error': 'Invalid credentials'}, status=401)

class EmailView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
       serializer = EmailSerializer(data=request.data)
       if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
       return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, *args, **kwargs):
        emails = Mail.objects.all()

        serializer = EmailSerializer(emails, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)