from django.test import TestCase, Client
from models import Backlog
from django.contrib.auth.models import AnonymousUser, User

from views import BacklogListView
from django.core.urlresolvers import reverse
# Create your tests here.
class BacklogModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='carl',
            email='carl.bednorz@gmail.com',
            password='super_secret_password'
        )

        self.name = "My first Backlog with User Stories"
        self.description = "That is the description for my Backlog. It's optional tough."
        self.short_id = "test"

        self.backlog = Backlog.objects.create(
            user=self.user,
            name=self.name,
            description=self.description,
            short_id=self.short_id
        )

    def tearDown(self):
        pass

    def test_backlog_model_works(self):
        """
        Get's the model instance created in the setUp method and tests if field content
        contains the stuff as expected.
        """
        backlog = Backlog.objects.get(id=self.backlog.id)

        self.assertTrue(backlog)
        self.assertEqual(backlog.id, self.backlog.id)
        self.assertEqual(backlog.uuid, self.backlog.uuid)
        self.assertEqual(backlog.user.username, 'carl')
        self.assertEqual(backlog.user.email, 'carl.bednorz@gmail.com')
        self.assertEqual(backlog.name, self.backlog.name)
        self.assertEqual(backlog.user, self.user)


class BacklogListViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='carl',
            email='carl.bednorz@gmail.com',
            password='super_secret_password'
        )

        self.name = "My first Backlog with User Stories"
        self.description = "That is the description for my Backlog. It's optional tough."

        self.backlog = Backlog.objects.create(
            user=self.user,
            name=self.name,
            description=self.description
        )

        self.client = Client()

    def tearDown(self):
        pass

    def test_backlog_list_view_works(self):
        """
        Check if BacklogListView works as expected
        """

        #backlogs is protected by username and pw
        response = self.client.get(reverse('backlog_list_view'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login/?redirect_to=/backlogs/')

        #Now login the user
        self.client = Client()
        #self.client.login(username=self.user.username, password=self.user.password)
        self.client.force_login(user=self.user)
        response = self.client.get(reverse('backlog_list_view'))
        self.assertEqual(response.status_code, 200)

class BacklogDetailViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='carl',
            email='carl.bednorz@gmail.com',
            password='super_secret_password'
        )

        self.name = "My first Backlog with User Stories"
        self.description = "That is the description for my Backlog. It's optional tough."

        self.backlog = Backlog.objects.create(
            user=self.user,
            name=self.name,
            description=self.description
        )

        self.client = Client()


    def tearDown(self):
        pass

    def test_backlog_detail_view_works(self):
        #backlogs is protected by username and pw
        response = self.client.get(reverse('backlog_detail_view',
                                            kwargs={'uuid': str(self.backlog.uuid)}))
        self.assertEqual(response.status_code, 302)

        self.client.force_login(user=self.user)

        response = self.client.get(reverse('backlog_detail_view',
                                            kwargs={'uuid': str(self.backlog.uuid)}))
        self.assertEqual(response.status_code, 200)
