from django.test import TestCase
from journal.models import Student

# Create your tests here.

class PersonSimpleTest(TestCase):
    def setup(self):
        Student.objects.create(name="Foo Barish", student_email="fooish@bar.com",
                            school_id=011010, student_id=2312, personal_code='abc123')
