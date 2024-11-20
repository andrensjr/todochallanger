from django.test import TestCase
from core.models import Client, Project, Task


class ClientTestCase(TestCase):
    def test_creating_complete_client(self):
        client1 = Client.objects.create(name='Client 1', email='client1@test.com', enterprise='enterprise1')
        
        self.assertEqual(client1.name, 'Client 1')
        self.assertEqual(client1.email, 'client1@test.com')
        self.assertEqual(client1.enterprise, 'enterprise1')

    def test_creating_client_just_with_name(self):
        client1 = Client.objects.create(name='Client 1')
        
        self.assertEqual(client1.name, 'Client 1')
        self.assertEqual(client1.email, None)
        self.assertEqual(client1.enterprise, None)

    def test_creating_client_without_name_should_give_error(self):
        try: 
            Client.objects.create(name=None)
        except Exception as err:
            self.assertEqual(type(err).__name__, 'IntegrityError')

    def test_str(self):
        client1 = Client.objects.create(name='Client 1')
        self.assertEqual(client1.__str__(), 'Client 1')
