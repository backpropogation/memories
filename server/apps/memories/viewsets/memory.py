from apps.memories.models import Memory
from apps.memories.serializers import MemorySerializer
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated


class MemoryViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    Viewset for creating and getting list of memories.
    """

    serializer_class = MemorySerializer
    queryset = Memory.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """
        Return only memories of current user.
        """

        return self.queryset.filter(owner=self.request.user)
