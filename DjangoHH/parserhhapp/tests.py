from django.test import TestCase

from .models import Cities, Skills
from mixer.backend.django import mixer

class SkillsTestCase(TestCase):
    def setUp(self):
        self.skill = Skills.objects.create(name='skill_test', percent='percent_test', count='count_test')
        self.skill_str = Skills.objects.create(name='skill_test_str', percent='percent_test_str', count='count_test_str')

    def test_skill_name(self):
        self.assertFalse(self.skill.has_name())

    def test_skill_count(self):
        self.assertFalse(self.skill.has_count())

    def test_skill_percent(self):
        self.assertFalse(self.skill.has_percent())

    def test_skill(self):
        skill = Skills.objects.create(name='skill_test', percent='percent_test', count='count_test')
        self.assertTrue(skill.some_method() == 'test')

    def test_str(self):
        test_line = 'skill_test_str, percent_test_str, count_test_str'
        self.assertEqual(str(self.skill_str), test_line)


class CitiesTestCase(TestCase):
    def setUp(self):
        self.city = Cities.objects.create(name='city_test', percent='percent_test', count='count_test')
        self.city_str = Cities.objects.create(name='city_test_str', percent='percent_test_str', count='count_test_str')


    def test_city_name(self):
        self.assertFalse(self.city.has_name())

    def test_city_count(self):
        self.assertFalse(self.city.has_count())

    def test_city_percent(self):
        self.assertFalse(self.city.has_percent())

    def test_city_image(self):
        self.assertFalse(self.city.has_image())

    def test_str(self):
        test_line = 'city_test_str, percent_test_str, count_test_str'
        self.assertEqual(str(self.city_str), test_line)


class SkillsTestCaseMixer(TestCase):
    def setUp(self):
        self.skill = mixer.blend(Skills)
        self.skill_str = mixer.blend(Skills)

    def test_skill_name(self):
        self.assertFalse(self.skill.has_name())

    def test_skill_count(self):
        self.assertFalse(self.skill.has_count())

    def test_skill_percent(self):
        self.assertFalse(self.skill.has_percent())

    def test_skill(self):
        skill = Skills.objects.create(name='skill_test', percent='percent_test', count='count_test')
        self.assertTrue(skill.some_method() == 'test')




class CitiesTestCaseMixer(TestCase):
    def setUp(self):
        self.city = mixer.blend(Cities)
        self.city_str = mixer.blend(Cities)


    def test_city_name(self):
        self.assertFalse(self.city.has_name())

    def test_city_count(self):
        self.assertFalse(self.city.has_count())

    def test_city_percent(self):
        self.assertFalse(self.city.has_percent())

    def test_city_image(self):
        self.assertFalse(self.city.has_image())




