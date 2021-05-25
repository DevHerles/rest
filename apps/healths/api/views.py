from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from apps.healths.models import Health
from apps.healths.api.serializers import HealthSerializer, HealthListSerializer


@api_view(['GET', 'POST'])
def healths_api_view(request):
    if request.method == 'GET':
        healths = Health.objects.all()
        healths_serializer = HealthListSerializer(healths, many=True)
        return Response(healths_serializer.data, status=status.HTTP_200_OK)

    # create
    elif request.method == 'POST':
        health_serializer = HealthSerializer(data=request.data)

        # validation
        if health_serializer.is_valid():
            health_serializer.save()
            return Response({'message': 'DJ Salud creado correctamente!'},
                            status=status.HTTP_201_CREATED)

        return Response(health_serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def health_detail_api_view(request, pk=None):
    # queryset
    health = Health.objects.filter(id=pk).first()

    # validation
    if health:

        # retrieve
        if request.method == 'GET':
            health_serializer = HealthSerializer(health)
            return Response(health_serializer.data, status=status.HTTP_200_OK)

        # update
        elif request.method == 'PUT':
            health_serializer = HealthSerializer(health, data=request.data)
            if health_serializer.is_valid():
                health_serializer.save()
                return Response(health_serializer.data,
                                status=status.HTTP_200_OK)
            return Response(health_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

        # delete
        elif request.method == 'DELETE':
            health.delete()
            return Response({'message': 'Registro eliminado correctamente'},
                            status=status.HTTP_200_OK)

    return Response({'message': 'Usuario no existe!'},
                    status=status.HTTP_400_BAD_REQUEST)
