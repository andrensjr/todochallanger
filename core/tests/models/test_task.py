from django.test import TestCase
from core.models import Project, Task
from datetime import datetime


class TaskTestCase(TestCase):
    def test_creating_complete_task(self):
        expected_date = datetime.now()
        Project1 = Project.objects.create(name='Project 1')
        Task1 = Task.objects.create(
            title='Task 1', 
            description='Description task 1', 
            project=Project1, 
            completed=True, 
            created_at=expected_date)
        
        self.assertEqual(Task1.title, 'Task 1')
        self.assertEqual(Task1.description, 'Description task 1')
        self.assertEqual(Task1.project.name, 'Project 1')
        self.assertTrue(Task1.completed)

    def test_creating_task_without_project(self):
        Task1 = Task.objects.create(title='Task 1', description='Description task 1', project=None)
        
        self.assertEqual(Task1.title, 'Task 1')

    def test_creating_task_without_description_should_give_error(self):
        try: 
            Task.objects.create(title='Task 1', description=None)
        except Exception as err:
            self.assertEqual(type(err).__name__, 'IntegrityError')

    def test_creating_task_without_title_should_give_error(self):
        try: 
            Task.objects.create(title=None)
        except Exception as err:
            self.assertEqual(type(err).__name__, 'IntegrityError')

    def test_str(self):
        Task1 = Task.objects.create(title='Task 1', description='Description task 1')
        self.assertEqual(Task1.__str__(), 'Task 1')