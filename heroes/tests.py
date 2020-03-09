#heroes/tests.py

from django.test import TestCase

# Create your tests here. 
class HomepageTest(TestCase):
	def homepage_test(self):
		response = self.client.get('/heroes/')
		self.assertTemplateUsed(response, 'homepage.html')

class CloudTest(TestCase):
	def cloud_test(self):
		response = self.client.get('/hero/cloud/')
		self.assertTemplateUsed(response, 'detail_cloud.html')

class SunfloweyTest(TestCase):
	def sunflowey_test(self):
		response = self.client.get('/hero/sunflowey/')
		self.assertTemplateUsed(response, 'detail_sunflowey.html')

class JesterTest(TestCase):
	def jester_test(self):
		response = self.client.get('/hero/jester/')
		self.assertTemplateUsed(response, 'detail_jester.html')
