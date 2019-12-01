from rest_framework.routers import DefaultRouter

from apps.memories.viewsets import MemoryViewSet
from apps.users.views import GetUserInfoView

router = DefaultRouter()

router.register('user/info', GetUserInfoView, base_name='user-info')
router.register('memories', MemoryViewSet, base_name='memory')
