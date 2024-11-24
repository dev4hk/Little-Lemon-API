from django.test import TestCase
from restaurant.models import MenuItem

class MenuItemTest(TestCase):
    
    def test_menu_item_creation(self):
        item = MenuItem.objects.create(
            title = 'Pasta',
            price = 12.99,
            inventory = 10
        )
        
        self.assertEqual(str(item), 'Pasta : 12.99')
        