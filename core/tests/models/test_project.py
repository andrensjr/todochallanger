from django.test import TestCase
from core.models import Client, Project


class ProjectTestCase(TestCase):
    def test_creating_complete_project(self):
        Client1 = Client.objects.create(name='Client 1')
        Project1 = Project.objects.create(name='Project 1', client=Client1)
        
        self.assertEqual(Project1.name, 'Project 1')
        self.assertEqual(Project1.client.name, 'Client 1')

    def test_creating_project_without_client(self):
        Project1 = Project.objects.create(name='Project 1', client=None)
        
        self.assertEqual(Project1.name, 'Project 1')

    def test_creating_Project_without_name_should_give_error(self):
        try: 
            Project.objects.create(name=None)
        except Exception as err:
            self.assertEqual(type(err).__name__, 'IntegrityError')

    def test_str(self):
        Project1 = Project.objects.create(name='Project 1')
        self.assertEqual(Project1.__str__(), 'Project 1')