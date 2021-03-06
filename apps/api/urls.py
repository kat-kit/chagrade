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
from apps.api.views.klasses import KlassViewSet, HomeworkAnswersCSVView, EnrollStudentsSampleCSVView
from apps.api.views.groups import TeamViewSet
from apps.api.views import metrics


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
    path('create_students_from_csv/', create_students_from_csv, name='create_students_from_csv'),

    # Enroll Students Upload Sample CSV
    path('enroll_students_sample_csv/', EnrollStudentsSampleCSVView.as_view(), name='enroll_students_sample_CSV'),

    # Metrics
    path('chagrade_overall_metrics/', metrics.chagrade_overall_metrics, name='chagrade_overall_metrics'),
    path('chagrade_student_metrics/', metrics.StudentMetricsView.as_view(), name='chagrade_student_metrics'),
    path('chagrade_instructor_metrics/', metrics.InstructorMetricsView.as_view(), name='chagrade_instructor_metrics'),
    path('chagrade_klass_metrics/', metrics.KlassMetricsView.as_view(), name='chagrade_klass_metrics'),
    path('chagrade_submission_metrics/', metrics.SubmissionMetricsView.as_view(), name='chagrade_submission_metrics'),
    path('student_submission_times/<int:student_pk>', metrics.StudentSubmissionTimesView.as_view(), name='student_submission_times'),
    path('student_scores/<int:student_pk>', metrics.StudentScoresView.as_view(), name='student_scores'),
    path('team_submission_times/<int:team_pk>', metrics.TeamSubmissionTimesView.as_view(), name='team_submission_times'),
    path('team_scores/<int:team_pk>', metrics.TeamScoresView.as_view(), name='team_scores'),
    path('team_contributions/<int:team_pk>', metrics.TeamContributionsView.as_view(), name='team_contributions'),
    path('klass_submission_times/<int:klass_pk>', metrics.KlassSubmissionTimesView.as_view(), name='klass_submission_times'),
    path('klass_scores/<int:klass_pk>', metrics.KlassScoresView.as_view(), name='klass_scores'),

    # CSV Metrics
    path('klass_csv/<int:klass_pk>', metrics.InstructorKlassCSVView.as_view(), name='klass_CSV'),
    path('student_csv/<int:student_pk>', metrics.InstructorStudentCSVView.as_view(), name='student_CSV'),
    path('team_csv/<int:team_pk>', metrics.InstructorTeamCSVView.as_view(), name='team_CSV'),

    path('klasses_csv/', metrics.AdminKlassCSVView.as_view(), name='klasses_CSV'),
    path('users_csv/', metrics.AdminUserCSVView.as_view(), name='users_CSV'),
    path('submissions_csv/', metrics.AdminSubmissionCSVView.as_view(), name='submissions_CSV'),

    # Homework answers CSV
    path('answers_csv/<int:klass_pk>/<int:definition_pk>/', HomeworkAnswersCSVView.as_view(), name='homework_answers_CSV'),
]
