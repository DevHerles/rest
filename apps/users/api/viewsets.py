from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import (IsAdminUser, DjangoModelPermissions,
                                        AllowAny, IsAuthenticated)
from apps.users.api.serializers import (CustomUserSerializer as UserSerializer,
                                        UsersListSerializer,
                                        UserUpdateSerializer)
from apps.partners.models import Partner
from apps.partners.api.serializers.partners_api_serializers import PartnerCreateSerializer
from apps.settings.models import Setting
from apps.users.permissions import (IsOwnerOrAdminUser, IsAdminUser,
                                    IsLoggedInUserOrSuperAdmin,
                                    IsAdminOrAnonymousUser)
from django.contrib.auth.models import Group


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def get_queryset(self, pk=None):
        if pk is None:
            if self.action == 'list':
                if self.request.user.groups.name in ['admin', 'moderator']:
                    return self.get_serializer().Meta.model.objects.filter(
                        is_active=True, is_superuser=False)
                else:
                    return self.get_serializer().Meta.model.objects.filter(
                        is_active=True, owner=self.request.user)
        else:
            if self.request.user.groups.name in ['admin', 'user']:
                return self.get_serializer().Meta.model.objects.filter(
                    id=pk, is_active=True).first()
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        serializer = self.get_serializer(self.get_queryset(pk))
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request):
        serializer = UsersListSerializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        data = request.data
        data['owner'] = request.user
        group_name = data.pop('role', 'user')
        new_group, created = Group.objects.get_or_create(name=group_name)
        print('new_group', new_group)
        print('created', created)
        data['groups'] = new_group.id if new_group else created.id
        serializer = self.serializer_class(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

        partner_data = {
            'name': data.get('username', False),
            'email': data.get('email', False)
        }

        partner_serializer = PartnerCreateSerializer(data=partner_data)
        partner = None
        if partner_serializer.is_valid():
            partner = partner_serializer.save()
        else:
            return Response(partner_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

        data['partner'] = partner.id
        serializer = self.serializer_class(data=data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Usuario creado correctamente.'},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        data = request.data
        group_name = data.pop('role', 'user')
        password = data.pop('password', None)
        new_group, created = Group.objects.get_or_create(name=group_name)
        data['groups'] = new_group.id if new_group else created.id
        print(data)
        if self.get_queryset(pk):
            serializer = UserUpdateSerializer(self.get_queryset(pk), data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {'message': 'Usuario actualizado correctamente.'},
                    status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Usuario no existe'},
                        status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        instance = self.get_queryset(pk)
        print('instance====' * 10, instance)
        if instance:
            instance.is_active = False
            instance.save()
            return Response({'message': 'Usuario eliminado correctamente'},
                            status=status.HTTP_200_OK)
        return Response({'message': 'Usuario no existe'},
                        status=status.HTTP_400_BAD_REQUEST)

    # def get_permissions(self):
    #     permission_classes = []
    # if self.action == 'create':
    #     permission_classes = [IsAdminUser]
    # elif self.action == 'list':
    #     permission_classes = [IsOwnerOrAdminUser]
    # elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
    #     permission_classes = [IsOwnerOrAdminUser]
    # elif self.action == 'destroy':
    #     permission_classes = [IsLoggedInUserOrSuperAdmin]
    # return [permission() for permission in permission_classes]
