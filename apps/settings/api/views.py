from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from apps.settings.models import Setting
from apps.settings.api.serializers import SettingSerializer, SettingListSerializer


@api_view(['GET', 'POST'])
def settings_api_view(request):
    if request.method == 'GET':
        settings = Setting.objects.all()
        settings_serializer = SettingSerializer(settings, many=True)
        return Response(settings_serializer.data, status=status.HTTP_200_OK)

    # create
    elif request.method == 'POST':
        setting_serializer = SettingSerializer(data=request.data)

        # validation
        if setting_serializer.is_valid():
            setting_serializer.save()
            return Response({'message': 'Setting creado correctamente!'},
                            status=status.HTTP_201_CREATED)

        return Response(setting_serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def setting_detail_api_view(request, pk=None):
    # queryset
    setting = Setting.objects.filter(id=pk).first()

    # validation
    if setting:

        # retrieve
        if request.method == 'GET':
            setting_serializer = SettingSerializer(setting)
            return Response(setting_serializer.data, status=status.HTTP_200_OK)

        # update
        elif request.method == 'PUT':
            setting_serializer = SettingSerializer(setting, data=request.data)
            if setting_serializer.is_valid():
                setting_serializer.save()
                return Response(setting_serializer.data,
                                status=status.HTTP_200_OK)
            return Response(setting_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

        # delete
        elif request.method == 'DELETE':
            setting.delete()
            return Response({'message': 'Registro eliminado correctamente'},
                            status=status.HTTP_200_OK)

    return Response({'message': 'Usuario no existe!'},
                    status=status.HTTP_400_BAD_REQUEST)
