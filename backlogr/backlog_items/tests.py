from django.test import TestCase, Client
from models import BacklogItem
from backlogs.models import Backlog
from django.contrib.auth.models import AnonymousUser, User

from django.core.urlresolvers import reverse
# Create your tests here.
class BacklogItemViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='carl',
            email='carl.bednorz@gmail.com',
            password='super_secret_password'
        )

        self.name = "My first Backlog with User Stories"
        self.description = "That is the description for my Backlog. It's optional tough."
        self.short_id = "FRNKN"
        self.backlog = Backlog.objects.create(
            user=self.user,
            name=self.name,
            description=self.description,
            short_id=self.short_id
        )

        self.who = "Product Manager"
        self.what = "create a backlog item"
        self.why = "I can write down a user story for my requirement"
        self.acceptance_criteria = "* Product Manager is logged in"
        self.notes = "***Needs breakdown***"

        self.story_points = 5
        self.business_value = 150

        self.backlog_item = BacklogItem.objects.create(
            user=self.user,
            backlog=self.backlog,
            who=self.who,
            what=self.what,
            why=self.why,
            acceptance_criteria=self.acceptance_criteria,
            notes=self.notes,
            story_points=self.story_points,
            business_value=self.business_value
        )

        self.client = Client()

    def test_backlog_item_update_view(self):
        response = self.client.get(reverse('backlog_item_update_view', kwargs={'backlog_item_uuid':self.backlog_item.uuid}))

        self.assertEqual(response.status_code, 302)

    def test_backlog_item_create_view(self):
        response = self.client.get(reverse('backlog_item_create_view', kwargs={'backlog_uuid':self.backlog.uuid}))

        self.assertEqual(response.status_code, 302)


    """
    def test_backlog_item_view(self):
        response = self.client.get('/backlog/item/333')
        self.assertEqual(response.status_code, 555)
    """

class BacklogItemModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='carl',
            email='carl.bednorz@gmail.com',
            password='super_secret_password'
        )

        self.name = "My first Backlog with User Stories"
        self.description = "That is the description for my Backlog. It's optional tough."
        self.short_id = "FRNKN"
        self.backlog = Backlog.objects.create(
            user=self.user,
            name=self.name,
            description=self.description,
            short_id=self.short_id
        )

        self.who = "Product Manager"
        self.what = "create a backlog item"
        self.why = "I can write down a user story for my requirement"
        self.acceptance_criteria = "* Product Manager is logged in"
        self.notes = "***Needs breakdown***"

        self.story_points = 5
        self.business_value = 150

        self.backlog_item = BacklogItem.objects.create(
            user=self.user,
            backlog=self.backlog,
            who=self.who,
            what=self.what,
            why=self.why,
            acceptance_criteria=self.acceptance_criteria,
            notes=self.notes,
            story_points=self.story_points,
            business_value=self.business_value
        )


    def tearDown(self):
        pass

    def test_backlog_item_model(self):
        bi = BacklogItem.objects.get(id=self.backlog_item.id)

        self.assertEqual("As a Product Manager I'd like to create a backlog item, so that I can write down a user story for my requirement.", bi.get_user_story())
        self.assertTrue(bi)
        self.assertEqual(self.user, bi.user)
        self.assertEqual(self.backlog, bi.backlog)
        self.assertEqual(self.who, bi.who)
        self.assertEqual(self.what, bi.what)
        self.assertEqual(self.why, bi.why)
        self.assertEqual(self.acceptance_criteria, bi.acceptance_criteria)
        self.assertEqual(self.notes, bi.notes)
        self.assertEqual(self.story_points, bi.story_points)
        self.assertEqual(self.business_value, bi.business_value)
        self.assertTrue(bi.created_on)
        self.assertTrue(bi.updated_on)
