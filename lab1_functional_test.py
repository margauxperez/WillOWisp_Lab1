from selenium import webdriver
import unittest

browser = webdriver.Firefox()
#browser.get('http://localhost:8000')

class NewVisitorTest(unittest.TestCase):
	#This is another test for git.
	def setUp(self):
		self.browser = webdriver.Firefox()
		
	def tearDown(self):
		self.browser.quit()

	def test_can_display_a_heroes_list_and_more_information_per_hero(self):
		# Widget has heard about a new wiki app for the game called The Will of the Wisps. 
		# She goes to check out its homepage
		browser.get('http://localhost:8000')

		# She notices the page title and header mention 
		# 'The Will of the Wisps Wiki'
		self.assertIn('The Will of the Wisps Wiki', self.browser.title)
		
		# She sees a list containing three heroes with their corresponding 
		# names, health points, and damage
		#names
		cloud_text = self.browser.find_element_by_id('cloud')
		self.assertIn('Cloud', cloud_text.text)
		jester_text = self.browser.find_element_by_id('jester')
		self.assertIn('Jester', jester_text.text)
		sunflowey_text = self.browser.find_element_by_id('sunflowey')
		self.assertIn('Sunflowey', sunflowey_text.text)
		#health points
		cloud_health = self.browser.find_element_by_id('cloudHealth')
		self.assertIn('Cloud', cloud_health.text)
		jester_health = self.browser.find_element_by_id('jesterHealth')
		self.assertIn('Jester', jester_health.text)
		sunflowey_health = self.browser.find_element_by_id('sunfloweyHealth')
		self.assertIn('Sunflowey', sunflowey_health.text)
		#damage
		cloud_damage = self.browser.find_element_by_id('cloudDamage')
		self.assertIn('Cloud', cloud_damage.text)
		jester_damage = self.browser.find_element_by_id('jesterDamage')
		self.assertIn('Jester', jester_damage.text)
		sunflowey_damage = self.browser.find_element_by_id('sunfloweyDamage')
		self.assertIn('Sunflowey', sunflowey_damage.text)


		# When she selects one of the heroes, she is sent to another page
		# containing more information about the hero (additional stats, lore, image).
		#cloud_stat = self.browser.find_element_by_id('cloud')
		#self.assertIn('Cloud', cloud_text.text)

		#jester_text = self.browser.find_element_by_id('jester')
		#self.assertIn('Jester', jester_text.text)

		#sunflowey_text = self.browser.find_element_by_id('sunflowey')
		#self.assertIn('Sunflowey', sunflowey_text.text)
		
		# She spots the page title and header mentions the name of the hero she selected.
		
		# While she is in a specific hero's page, she sees a button labeled "Back to Heroes List".
		# She clicks this and she is redirected back to the wiki's homepage.	
		
		self.fail('Finish the test!')
		
#main method
if __name__ == '__main__':
	unittest.main(warnings='ignore')