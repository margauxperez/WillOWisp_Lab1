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
		#header_text = self.browser.find_element_by_tag_name('h1')
		#self.assertIn('The Will of the Wisps Wiki', header_text)
		
		# She sees a list containing three heroes with their corresponding 
		# names, health points, and damage
		#names
		cloud_text = self.browser.find_element_by_id('cloud')
		self.assertIn('Cloud', cloud_text)
		jester_text = self.browser.find_element_by_id('jester')
		self.assertIn('Jester', jester_text)
		sunflowey_text = self.browser.find_element_by_id('sunflowey')
		self.assertIn('Sunflowey', sunflowey_text)
		
		#health points
		cloud_health = self.browser.find_element_by_id('cloudHealth')
		self.assertIn('Cloud', cloud_health)
		jester_health = self.browser.find_element_by_id('jesterHealth')
		self.assertIn('Jester', jester_health)
		sunflowey_health = self.browser.find_element_by_id('sunfloweyHealth')
		self.assertIn('Sunflowey', sunflowey_health)
		
		#damage
		cloud_damage = self.browser.find_element_by_id('cloudDamage')
		self.assertIn('Cloud', cloud_damage)
		jester_damage = self.browser.find_element_by_id('jesterDamage')
		self.assertIn('Jester', jester_damage)
		sunflowey_damage = self.browser.find_element_by_id('sunfloweyDamage')
		self.assertIn('Sunflowey', sunflowey_damage)

		# When she selects one of the heroes, she is sent to another page
		# containing more information about the hero (additional stats, lore, image).
		#stats
		cloud_skills = self.browser.find_element_by_tag_id('cloudSkills')
		self.assertIn('Nimbus, Rain Cloud, Thunderbolt', cloud_skills)
		jester_skills = self.browser.find_element_by_tag_id('jesterSkills')
		self.assertIn('Laugh, Dance, Smile', jester_skills)
		sunflowey_skills = self.browser.find_element_by_tag_id('sunfloweySkills')
		self.assertIn('Power Pellet, Sunshine, Pollen Punch', sunflowey_skills)

		#lore
		cloud_lore = self.browser.find_element_by_tag_id('cloudLore')
		self.assertIn('I am a cloud. When I pee you call it "rain".', cloud_lore)
		jester_lore = self.browser.find_element_by_tag_id('jesterLore')
		self.assertIn('I do it for the LOLs.', jester_lore)
		sunflowey_lore = self.browser.find_element_by_tag_id('sunfloweyLore')
		self.assertIn('I am Sunflowey. Sometimes a sun, sometimes a flower.', sunflowey_lore)
		
		# She spots the page title and header mentions the name of the hero she selected.
		#cloud
		self.browser.find_element_by_link_text('cloud').click()
		self.assertIn('/hero/cloud', self.browser.current_url)
		self.assertIn('Detail - Cloud', self.browser.title)

		#jester
		self.browser.find_element_by_link_text('jester').click()
		self.assertIn('/hero/jester', self.browser.current_url)
		self.assertIn('Detail - Jester', self.browser.title)
		
		#sunflowey
		self.browser.find_element_by_link_text('sunflowey').click()
		self.assertIn('/hero/sunflowey', self.browser.current_url)
		self.assertIn('Detail - Sunflowey', self.browser.title)

		# While she is in a specific hero's page, she sees a button labeled "Back to Heroes List".
		# She clicks this and she is redirected back to the wiki's homepage.
		self.browser.find_element_by_link_text('Back to Heroes').click()
		self.assertIn('/heroes/', self.browser.current_url)
		
		self.fail('Finish the test!')
		
#main method
if __name__ == '__main__':
	unittest.main(warnings='ignore')