from curs.apps import CursConfig
from rest_framework.routers import DefaultRouter

from curs.views import CourseViewSet

app_name = CursConfig.name

router = DefaultRouter()
router.register(r'curs', CourseViewSet, basename='curs')

urlpatterns = [

] + router.urls
