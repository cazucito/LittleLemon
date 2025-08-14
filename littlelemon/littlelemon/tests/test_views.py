from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        """Add a few test instances of the Menu model"""
        # Create test menu items
        self.menu_item1 = Menu.objects.create(
            title="Pasta",
            price=12.99,
            inventory=50
        )
        self.menu_item2 = Menu.objects.create(
            title="Pizza",
            price=15.50,
            inventory=30
        )
        self.menu_item3 = Menu.objects.create(
            title="Burger",
            price=9.99,
            inventory=25
        )
        
        # Set up API client
        self.client = APIClient()
    
    def test_getall(self):
        """Test retrieving all Menu objects and check serialized data"""
        # Make GET request to retrieve all menu items
        response = self.client.get('/restaurant/items/')
        
        # Get all menu objects from database
        menus = Menu.objects.all()
        
        # Serialize the menu objects
        serializer = MenuSerializer(menus, many=True)
        
        # Assert that the request was successful
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Assert that the response data equals the serialized data
        self.assertEqual(response.data, serializer.data)
        
        # Additional assertions to verify the content
        self.assertEqual(len(response.data), 3)  # Should have 3 menu items
        
        # Verify specific menu items are in the response
        titles = [item['title'] for item in response.data]
        self.assertIn('Pasta', titles)
        self.assertIn('Pizza', titles)
        self.assertIn('Burger', titles)
