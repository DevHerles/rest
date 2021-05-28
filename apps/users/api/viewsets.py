from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import (IsAdminUser, DjangoModelPermissions,
                                        AllowAny, IsAuthenticated)
from apps.users.api.serializers import (
    CustomUserSerializer as UserSerializer, )
from apps.partners.models import Partner
from apps.users.permissions import (IsOwnerOrAdminUser, IsAdminUser,
                                    IsLoggedInUserOrSuperAdmin,
                                    IsAdminOrAnonymousUser)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            if self.action == 'list':
                if self.request.user.groups.name == 'admin':
                    return self.get_serializer().Meta.model.objects.filter(
                        is_active=True)
                else:
                    return self.get_serializer().Meta.model.objects.filter(
                        is_active=True, owner=self.request.user)
        else:
            if self.request.user.groups.name in ['admin', 'user']:
                return self.get_serializer().Meta.model.objects.filter(
                    id=pk, is_active=True).first()
            else:
                return Response(status=status.HTTP_402_NOT_ALLOWED)

    def retrieve(self, request, pk=None):
        print('retrieve' * 100, pk)
        serializer = self.get_serializer(self.get_queryset(pk))
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request):
        print('request=' * 30, request.user)
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            Partner(owner=user, email=user.email, name=user.username).save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk),
                                               data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'message': 'Usuario no existe'},
                        status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        instance = self.get_queryset().filter(id=pk).first()
        if instance:
            instance.is_active = False
            instance.save()
            return Response({'message': 'Usuario eliminado correctamente'},
                            status=status.HTTP_200_OK)
        return Response({'message': 'Usuario no existe'},
                        status=status.HTTP_400_BAD_REQUEST)

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsAdminUser]
        elif self.action == 'list':
            permission_classes = [IsOwnerOrAdminUser]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsOwnerOrAdminUser]
        elif self.action == 'destroy':
            permission_classes = [IsLoggedInUserOrSuperAdmin]
        return [permission() for permission in permission_classes]
