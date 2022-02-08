from django.test import TestCase
from .models import Article,Editor,tags
# Create your tests here.
class EditorTestClass(TestCase):
    def setUp(self):
        self.james = Editor(first_name = 'james', last_name = 'mwakio', email = 'mwakio@gmail.com')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.james,Editor)) 
    def test_save_method(self):
        self.james.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors)>0)
    def test_delete_method(self):
        self.james.delete_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors)<1)           
