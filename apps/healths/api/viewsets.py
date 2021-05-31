from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, DjangoModelPermissions, IsAuthenticated
from apps.healths.api.serializers import (HealthSerializer,
                                          HealthCreateSerializer)

from apps.users.permissions import IsOwnerOrAdminUser
from apps.users.models import User


class HealthViewSet(viewsets.ModelViewSet):
    serializer_class = HealthSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdminUser]

    def get_queryset(self, pk=None):
        if pk is None:
            if self.request.user.groups.name in ['admin', 'supervisor']:
                return self.get_serializer().Meta.model.objects.filter(
                    is_active=True)
            else:
                return self.get_serializer().Meta.model.objects.filter(
                    is_active=True, owner=self.request.user)
        else:
            return self.get_serializer().Meta.model.objects.filter(
                id=pk, is_active=True).first()

    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        data = request.data
        _id = data.pop('_id', None)
        user = User.objects.filter(pk=request.user.id).first()
        data['owner'] = user.id
        data['partner'] = user.partner.id
        write_serializer = HealthCreateSerializer(data=data)
        if write_serializer.is_valid():
            instance = write_serializer.save()
            read_serializer = self.serializer_class(instance)
            return Response({'message': 'Creado correctamente.'},
                            status=status.HTTP_201_CREATED)
        return Response(write_serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        data = request.data
        if self.get_queryset(pk):
            data['partner'] = request.user.partner.id
            serializer = HealthCreateSerializer(self.get_queryset(pk),
                                                data=request.data)
            if serializer.is_valid():
                instance = serializer.save()
                read_serializer = self.serializer_class(instance)
                return Response({'message': 'Actualizado correctamente.'},
                                status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'DJ Salud no existe'},
                        status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        instance = self.get_queryset().filter(id=pk).first()
        if instance:
            instance.is_active = False
            instance.save()
            return Response({'message': 'Eliminado correctamente.'},
                            status=status.HTTP_200_OK)
        return Response({'message': 'DJ Salud no existe'},
                        status=status.HTTP_404_NOT_FOUND)
