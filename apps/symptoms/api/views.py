from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from apps.symptoms.models import Symptom
from apps.symptoms.api.serializers import SymptomSerializer, SymptomListSerializer


@api_view(['GET', 'POST'])
def symptoms_api_view(request):
    if request.method == 'GET':
        symptoms = Symptom.objects.all()
        symptoms_serializer = SymptomListSerializer(symptoms, many=True)
        return Response(symptoms_serializer.data, status=status.HTTP_200_OK)

    # create
    elif request.method == 'POST':
        symptom_serializer = SymptomSerializer(data=request.data)

        # validation
        if symptom_serializer.is_valid():
            symptom_serializer.save()
            return Response({'message': 'Registro creado correctamente!'},
                            status=status.HTTP_201_CREATED)

        return Response(symptom_serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def symptom_detail_api_view(request, pk=None):
    # queryset
    symptom = Symptom.objects.filter(id=pk).first()

    # validation
    if symptom:

        # retrieve
        if request.method == 'GET':
            symptom_serializer = SymptomSerializer(symptom)
            return Response(symptom_serializer.data, status=status.HTTP_200_OK)

        # update
        elif request.method == 'PUT':
            symptom_serializer = SymptomSerializer(symptom, data=request.data)
            if symptom_serializer.is_valid():
                symptom_serializer.save()
                return Response(symptom_serializer.data,
                                status=status.HTTP_200_OK)
            return Response(symptom_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

        # delete
        elif request.method == 'DELETE':
            symptom.delete()
            return Response({'message': 'Registro eliminado correctamente'},
                            status=status.HTTP_200_OK)

    return Response({'message': 'Usuario no existe!'},
                    status=status.HTTP_400_BAD_REQUEST)
