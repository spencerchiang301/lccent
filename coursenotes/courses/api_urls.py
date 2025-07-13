from rest_framework.routers import DefaultRouter
from .api_views import CourseViewSet, NoteViewSet

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'notes', NoteViewSet)

urlpatterns = router.urls