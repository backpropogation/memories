from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class GetUserInfoView(viewsets.ViewSet):

    permission_classes = (IsAuthenticated,)

    def list(self, request):
        user_data = {
            'name': request.user.get_full_name()
        }
        return Response(user_data)

