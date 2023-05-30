from rest_framework import routers
from cadastro_app.views import CadastroViewSet

router = routers.DefaultRouter()
router.register(r'', CadastroViewSet)

urlpatterns = router.urls