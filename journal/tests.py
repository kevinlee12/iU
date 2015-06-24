from django.test import TestCase
from journal.models import Student, Coordinator, Users, Entry


class StudentTest(TestCase):
    def setUp(self):
        Users.objects.create(email='fooish@bar.com', user_type='S')
        Student.objects.create(first_name='Foo', last_name='Barish',
                               email='fooish@bar.com', school_code=110310,
                               student_id=2312, personal_code='abc123')

        Users.objects.create(email='coor@bar.com', user_type='C')
        Coordinator.objects.create(first_name='Coor', last_name='One',
                                   email='coor@bar.com', school_code=110310)

    def test_student_creation_simple(self):
        """Simple test to ensure that a student is properly registered"""
        foo_auth = Users.objects.get(email='fooish@bar.com')
        self.assertEqual(foo_auth.user_type, 'S')
        foo = Student.objects.get(email='fooish@bar.com')
        self.assertEqual(foo.full_name(), 'Foo Barish')

    def test_coordinator_creation_simple(self):
        """Simple test to ensure that a coordinator is properly registered"""
        coor_auth = Users.objects.get(email='coor@bar.com')
        self.assertEqual(coor_auth.user_type, 'C')
        coor = Coordinator.objects.get(email='coor@bar.com')
        self.assertEqual(coor.full_name(), 'Coor One')
        self.assertTrue(type(coor) == Coordinator)


class Journals(TestCase):
    def setUp(self):
        Entry.objects.create(email='fooish@bar.com', entry_type='T',
                             entry='Today I walked around the block.')

        Entry.objects.create(email='fooish@bar.com', entry_type='V',
                            entry='http://www.youtube.com')
        # TODO: Test Images
        # Entry.objects.create(email='fooish@bar.com', entry_type='I'
        #                     entry='/here.jpg')

    def test_entries(self):
        """Test to ensure that the entries appear in the right order"""
        entries = Entry.objects.all().filter(email='fooish@bar.com')\
            .order_by('last_modified').reverse()  # Newest first, oldest last
        self.assertEqual(entries[1].entry, 'Today I walked around the block.')
        self.assertEqual(entries[0].entry, 'http://www.youtube.com')
