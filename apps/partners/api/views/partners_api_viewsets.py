from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, DjangoModelPermissions, IsAuthenticated
from apps.partners.api.serializers.partners_api_serializers import (
    PartnerSerializer, )

from apps.users.permissions import IsOwnerOrAdminUser


class PartnerViewSet(viewsets.ModelViewSet):
    serializer_class = PartnerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(
                is_active=True)
        else:
            return self.get_serializer().Meta.model.objects.filter(
                id=pk, is_active=True).first()

    def retrieve(self, request, pk=None):
        print('retrievexxxx' * 100, pk)
        serializer = self.get_serializer(self.get_queryset(pk))
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request):
        print('list' * 100)
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        print('create---*' * 20)
        data = request.data
        data['user'] = request.user.id
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Creado correctamente.'},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        data = request.data
        dob = data.pop('dob', None)
        if dob:
            dob = dob[:10]
            data['dob'] = dob
        print('UPDATE:' * 10, data)
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk),
                                               data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Actualizado correctamente.'},
                                status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Partner no existe'},
                        status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        instance = self.get_queryset().filter(id=pk).first()
        if instance:
            instance.is_active = False
            instance.save()
            return Response({'message': 'Eliminado correctamente'},
                            status=status.HTTP_200_OK)
        return Response({'message': 'Partner no existe'},
                        status=status.HTTP_400_BAD_REQUEST)
