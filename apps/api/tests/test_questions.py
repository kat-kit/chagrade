from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from apps.homework.models import Definition
from apps.factory.factories import QuestionFactory
from apps.klasses.models import Klass
from apps.profiles.models import Instructor

User = get_user_model()

# TODO: Write POST/PUT/DELETE tests


class QuestionGETMethodTests(TestCase):

    def setUp(self):
        self.main_user = User.objects.create_user(username='user', password='pass', email='test@email.com')
        self.instructor = Instructor.objects.create(university_name='Test')
        self.main_user.instructor = self.instructor
        self.student_user = User.objects.create_user(username='student_user', password='pass')
        self.klass = Klass.objects.create(instructor=self.instructor, course_number="1")
        self.definition = Definition.objects.create(
            klass=self.klass,
            creator=self.instructor,
            due_date=timezone.now(),
            name='test',
            description='test',
            challenge_url=''
        )
        self.question = QuestionFactory(definition=self.definition, question='Test Question')

    def test_anonymous_user_cannot_get_questions(self):
        resp = self.client.get(reverse('api:question-list', kwargs={'version': 'v1'}))
        assert resp.status_code == 401

        resp = self.client.get(reverse('api:question-detail', kwargs={'version': 'v1', 'pk': self.question.pk}))
        assert resp.status_code == 401

    def test_student_user_can_get_questions(self):
        self.client.login(username='student_user', password='pass')
        resp = self.client.get(reverse('api:question-list', kwargs={'version': 'v1'}))
        assert resp.status_code == 200

        resp = self.client.get(reverse('api:question-detail', kwargs={'version': 'v1', 'pk': self.question.pk}))
        assert resp.json()['question'] == 'Test Question'

    def test_instructor_user_can_get_questions(self):
        self.client.login(username='user', password='pass')
        resp = self.client.get(reverse('api:question-list', kwargs={'version': 'v1'}))
        assert resp.status_code == 200

        resp = self.client.get(reverse('api:question-detail', kwargs={'version': 'v1', 'pk': self.question.pk}))
        assert resp.json()['question'] == 'Test Question'
