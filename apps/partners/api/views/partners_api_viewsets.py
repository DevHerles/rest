from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from apps.partners.api.serializers.partners_api_serializers import (
    PartnerSerializer, )


class PartnerViewSet(viewsets.ModelViewSet):
    serializer_class = PartnerSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(active=True)
        else:
            return self.get_serializer().Meta.model.objects.filter(
                id=pk, active=True).first()

    def list(self, request):
        partner_serializer = self.get_serializer(self.get_queryset(),
                                                 many=True)
        return Response(partner_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Registro creado'},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            partner_serializer = self.serializer_class(self.get_queryset(pk),
                                                       data=request.data)

            if partner_serializer.is_valid():
                partner_serializer.save()
                return Response(partner_serializer.data,
                                status=status.HTTP_200_OK)
        return Response({'message': 'Partner no existe'},
                        status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        partner = self.get_queryset().filter(id=pk).first()
        if partner:
            partner.active = False
            partner.save()
            return Response({'message': 'Eliminado correctamente'},
                            status=status.HTTP_200_OK)
        return Response({'message': 'Partner no existe'},
                        status=status.HTTP_400_BAD_REQUEST)
