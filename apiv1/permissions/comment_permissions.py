from rest_framework.permissions import BasePermission, SAFE_METHODS

class CommentPermission(BasePermission):
    """ 
        Permite GET Y POST a cualquiera. 
        Otros métodos son solo para usuarios autenticados.
    """
    def has_permission(self, request, view):
        if request.method in ['GET', 'POST']:
            return True
        return request.user and request.user.is_authenticated