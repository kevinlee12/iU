from django.test import TestCase
from journal.models import Student


class StudentTest(TestCase):
    def setUp(self):
        Student.objects.create(first_name="Foo", last_name="Barish",
                               student_email="fooish@bar.com", school_id=110310,
                               student_id=2312, personal_code='abc123')

    def test_student_creation_simple(self):
        """Simple test to ensure that a student can be properly registered"""
        foo = Student.objects.get(first_name="Foo")
        self.assertEqual(foo.full_name(), "Foo Barish")
