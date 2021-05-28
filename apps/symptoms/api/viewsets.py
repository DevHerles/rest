from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, DjangoModelPermissions, IsAuthenticated
from apps.symptoms.api.serializers import (
    SymptomSerializer, )

from apps.users.permissions import IsOwnerOrAdminUser
from apps.users.models import User
from apps.healths.models import Health


class SymptomViewSet(viewsets.ModelViewSet):
    serializer_class = SymptomSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdminUser]

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(
                is_active=True)
        else:
            return self.get_serializer().Meta.model.objects.filter(
                id=pk, is_active=True).first()

    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        data = request.data
        user = User.objects.filter(pk=request.user.id).first()
        health = Health.objects.filter(owner=user).first()
        if not health.fit:
            return Response(
                {
                    'detail':
                    'Su declaración jurada de salud no es apto. No puede continuar.'
                },
                status=status.HTTP_400_BAD_REQUEST)
        data['owner'] = user.id
        data['partner'] = user.partner.id
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk),
                                               data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'detail': 'DJ de Síntoma no existe'},
                        status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        instance = self.get_queryset().filter(id=pk).first()
        if instance:
            instance.is_active = False
            instance.save()
            return Response({'detail': 'Eliminado correctamente'},
                            status=status.HTTP_200_OK)
        return Response({'detail': 'DJ de Síntoma no existe'},
                        status=status.HTTP_400_BAD_REQUEST)
