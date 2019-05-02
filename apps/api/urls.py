from django.conf.urls import url, include
from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework.routers import SimpleRouter

from apps.api.views.homework import DefinitionViewSet, CriteriaViewSet, QuestionViewSet, SubmissionViewSet, \
    GradeViewSet, CustomChallengeURLViewSet
from apps.api.views.profiles import ProfileViewSet, StudentViewSet, create_students_from_csv, \
    TestStudentViewSet
from apps.api.views.klasses import KlassViewSet
from apps.api.views.groups import TeamViewSet
from apps.api.views.stats import chagrade_general_stats

app_name = 'api'
API_PREFIX = "v1"

# API routes
router = SimpleRouter()
router.register('users', ProfileViewSet)
router.register('students', StudentViewSet)
router.register('test_students', TestStudentViewSet)
router.register('klasses', KlassViewSet)
router.register('definitions', DefinitionViewSet)
router.register('criterias', CriteriaViewSet)
router.register('questions', QuestionViewSet)
router.register('submissions', SubmissionViewSet)
router.register('grades', GradeViewSet)
router.register('teams', TeamViewSet)
router.register('custom_challenge_urls', CustomChallengeURLViewSet)

# Documentation details
schema_view = get_schema_view(
    openapi.Info(
        title="Chagrade API",
        default_version='v1',
        description="Chagrade is a platform for machine learning resources, like competitions, test sets, and example solutions",
        contact=openapi.Contact(email="info@codalab.org"),
        license=openapi.License(name="MIT License"),
    ),
    validators=['flex', 'ssv'],
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    url('^', include(router.urls)),

    url('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Docs
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=None), name='schema-json'),
    url(r'^$', schema_view.with_ui('swagger', cache_timeout=None), name='docs'),

    # Custom API point for handling student creation
    # path('create_student/', create_student, name='create_student'),
    path('create_students_from_csv/', create_students_from_csv, name='create_students_from_csv'),
    path('chagrade_general_stats/', chagrade_general_stats, name='chagrade_general_stats')

    # Optionally, use "redoc" style
    # url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=None), name='schema-redoc'),
]
