from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):

  def has_object_permission(self,request, view, obj):
    print(request)
    if obj.user_id == request.user:
      return True
    else:
      return False