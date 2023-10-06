from rest_framework.permissions import BasePermission


class BookPermission(BasePermission):

    def has_permission(self, request, view):
        
        if request.method == 'GET':
            return True
        
        elif request.method in ['POST']:
            return request.user.is_staff