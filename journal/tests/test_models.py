from django.test import TestCase

from journal.models import Users, Advisor, Coordinator, Student
from journal.models import Entry, Activity
from journal.models import LearningObjectiveOptions, ActivityOptions
from journal.models import School


class UsersTest(TestCase):
    """Tests to ensure that users are properly registered"""
    def setUp(self):
        Users.objects.create(email='coor@bar.com', user_type='C')
        Users.objects.create(email='advise@ones.com', user_type='A')
        Users.objects.create(email='fooish@bar.com', user_type='S')
        School.objects.create(school_name="One HS", school_code=110310)

    def test_advisor_creation(self):
        """Tests to ensure that advisors have been created successfully"""
        school = School.objects.get(school_code=110310)
        Advisor.objects.create(first_name='Advise', last_name='Ones',
                               email='advise@ones.com', school=school)
        advisor = Advisor.objects.get(email='advise@ones.com')
        self.assertTrue(type(advisor) == Advisor)

    def test_coordinator(self):
        """Tests to ensure that coordinatorshave been created successfully"""
        school = School.objects.get(school_code=110310)
        Coordinator.objects.create(first_name='Coor', last_name='One',
                                   email='coor@bar.com', school=school)
        coordinator = Coordinator.objects.get(email='coor@bar.com')
        self.assertTrue(type(coordinator) == Coordinator)

    def test_student_creation_simple(self):
        """Simple test to ensure that a student is properly registered"""
        foo_auth = Users.objects.get(email='fooish@bar.com')
        self.assertEqual(foo_auth.user_type, 'S')


        school = School.objects.get(school_code=110310)

        Advisor.objects.create(first_name='Advise', last_name='Ones',
                               email='advise@ones.com', school=school)

        Coordinator.objects.create(first_name='Coor', last_name='One',
                                   email='coor@bar.com', school=school)

        stu_advisor = Advisor.objects.get(email='advise@ones.com')
        stu_coordinator = Coordinator.objects.get(email='coor@bar.com')

        Student.objects.create(first_name='Foo', last_name='Barish',
                               email='fooish@bar.com', student_id=2312,
                               personal_code='abc123',
                               school=school,
                               coordinator=stu_coordinator,
                               advisor=stu_advisor)
        student = Student.objects.get(email='fooish@bar.com')
        self.assertTrue(type(student) == Student)
        self.assertEqual(student.full_name(), 'Foo Barish')
        self.assertEqual(student.advisor.full_name(), 'Advise Ones')
        self.assertEqual(student.coordinator.full_name(), 'Coor One')

# TODO: Remove this, will keep until a proper forms test is completed
# class Journals(TestCase):
#     """"Tests to ensure that Journal Entries are properly inserted"""
#     def setUp(self):
#         LearningObjectiveOptions.objects.create(objective='Undertaken new challenges')
#         ActivityOptions.objects.create(name='Action')
#
#         School.objects.create(school_name="One HS", school_code=110310)
#
#         school = School.objects.get(school_code=110310)
#
#         Advisor.objects.create(first_name='Advise', last_name='Ones',
#                                email='advise@ones.com', school=school)
#
#         Coordinator.objects.create(first_name='Coor', last_name='One',
#                                    email='coor@bar.com', school=school)
#
#         stu_advisor = Advisor.objects.get(email='advise@ones.com')
#         stu_coordinator = Coordinator.objects.get(email='coor@bar.com')
#
#         Student.objects.create(first_name='Foo', last_name='Barish',
#                                email='fooish@bar.com', student_id=2312,
#                                personal_code='abc123',
#                                school=school,
#                                coordinator=stu_coordinator,
#                                advisor=stu_advisor)
#
#         # TODO: Test Images
#         # Entry.objects.create(email='fooish@bar.com', entry_type='I'
#         #                     entry='/here.jpg')
#
#     def test_entries(self):
#         """Test to ensure that the entries appear in the right order"""
#         foo = Student.objects.get(email='fooish@bar.com')
#
#         Entry.objects.create(stu_email=foo.email,
#                              activity_pk='Walking',
#                              entry_type='T',
#                              entry='Today I walked around the block.')
#
#         Entry.objects.create(stu_email=foo.email,
#                              activity_pk='Walking',
#                              entry_type='V',
#                              entry='http://www.youtube.com')
#
#         # Newest first, oldest last for all entries
#         entries = Entry.objects.all().filter(stu_email='fooish@bar.com',
#             activity_pk='Walking').order_by('last_modified').reverse()
#         self.assertEqual(entries[1].entry, 'Today I walked around the block.')
#         self.assertEqual(entries[0].entry, 'http://www.youtube.com')
#
#     def test_activity(self):
#         """Tests to ensure that the activity is linked with the user"""
#         foo = Student.objects.get(email='fooish@bar.com')
#
#         Activity.objects.create(student=foo, activity_pk='Walking',
#                                 activity_description='Walking around the block.')
#
#         foo_activity = Activity.objects.get(student=foo)
#         self.assertEqual(foo_activity.activity_pk, 'Walking')
#         self.assertEqual(foo_activity.student, foo)
#
#     def test_add_entries(self):
#         """Tests to ensure that entries and activity are properly linked with
#            user"""
#         foo = Student.objects.get(email='fooish@bar.com')
#         Activity.objects.create(student=foo, activity_pk='Walking',
#                                 activity_description='Walking around the block.',)
#
#         foo_activity = Activity.objects.get(student=foo)
#
#         Entry.objects.create(stu_email=foo.email,
#                              activity_pk=foo_activity.activity_pk,
#                              entry_type='T',
#                              entry='Today I walked around the block.')
#
#         Entry.objects.create(stu_email=foo.email,
#                              activity_pk=foo_activity.activity_pk,
#                              entry_type='V',
#                              entry='http://www.youtube.com')
#
#         entries = Entry.objects.all().filter(stu_email='fooish@bar.com',
#                                              activity_pk='Walking')\
#                                      .order_by('last_modified')
#         for entry in entries:
#             foo_activity.entries.add(entry)
#
#         entries = entries.all()
#
#         # Tests to ensure entries are the same
#         in_foo = foo_activity.entries.all()
#         for i in range(len(entries)):
#             expected = entries[i].entry
#             actual = in_foo[i].entry
#             self.assertEqual(actual, expected)
