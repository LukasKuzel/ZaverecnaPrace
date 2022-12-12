from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.
class UserAccountsTests(TestCase):
    def test_new_super(self):
        db = get_user_model()
        super_user = db.objects.create_superuser(
            'testuser@super.com','username','firstname','lastname','password')
        self.assertEqual(super_user.email,'testuser@super.com')
        self.assertEqual(super_user.username, 'username')
        self.assertEqual(super_user.first_name, 'firstname')
        self.assertEqual(super_user.last_name, 'lastname')
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_active)
        self.assertEqual(str(super_user),"username")

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='testuser@super.com', username='username1',first_name='first_name', last_name='last_name', password='password',is_superuser=False)

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='', username='username1', first_name='first_name', last_name='last_name',
                password='password', is_superuser=False)

    def test_new_user(self):
        db = get_user_model()
        user = db.objects.create_user(
            'testuser@super.com','username','first_name','last_name',
            'password')
        self.assertEqual(user.email, 'testuser@user.com')
        self.assertEqual(user.username, 'username')
        self.assertEqual(user.first_name, 'firstname')
        self.assertEqual(user.last_name, 'lastname')
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)

        with self.assertRaises(ValueError):
            db.objects.create_user(
                email='',username='a',first_name='first_name', password='password'
            )