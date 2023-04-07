# from django.shortcuts import render
# from rest_framework.generics import *
# from main.serializers import *
# from main.models import *
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import filters

# class CategoryCreateListView(ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

# class CategoryRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     lookup_field = "pk"

# class BrandCreateListView(ListCreateAPIView):
#     queryset = Brand.objects.all()
#     serializer_class = BrandSerializer

# class BrandRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
#     queryset = Brand.objects.all()
#     serializer_class = BrandSerializer
#     lookup_field = "pk"

# class ProductCreateListView(ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
    
# class ProductRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field = 'pk'



import django_filters
from django.shortcuts import render
from rest_framework.generics import *
from main.serializers import *
from main.models import *
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from django.contrib.auth.models import User
from rest_framework.authentication import *
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from .permissions import *
from rest_framework import filters

class CategoryCreateListView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'title', 'slug']

    def get_queryset(self):
        queryset = Category.objects.all()
        name = self.request.query_params.get("name")
        if name is not None:
               return Category.objects.filter(title__icontains=name) 
        return queryset

class CategoryRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "pk"

class BrandCreateListView(ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'title']

    def get_queryset(self):
        queryset = Brand.objects.all()
        name = self.request.query_params.get("name")
        if name is not None:
               return Brand.objects.filter(title__icontains=name) 
        return queryset

class BrandRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    lookup_field = "pk"

class ProductCreateListView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'title', 'desc']

    def get_queryset(self):
        queryset = Product.objects.all()
        name = self.request.query_params.get("name")
        if name is not None:
               return Product.objects.filter(title__icontains=name) 
        return queryset

class ProductRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

class RegisterAPIView(APIView):
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({})

class LoginAPIView(APIView):
    permission_classes = (AllowAny, )
        

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.save()
        return Response({"key": token.key})

class LogoutAPIView(APIView):
    def post(self, request):
        request.user.auth_token.delete()        
        return Response({"detail": "Successfully loged out"})

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAdminUser, )

    def create(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({}, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'], permission_classes=[IsAdminOrSelf])
    def set_password(self, request, pk):
        user = self.get_object()
        serializer = PasswordSerializer(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.validated_data["password"])
            user.save()
            return Response({"status": "Password Set"})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def recent_users(self, request):
        return Response({"detail" "Working..."})