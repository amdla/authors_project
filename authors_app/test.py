from django.test import TestCase
from django.urls import reverse

from .models import Author


class AuthorCRUDTestCase(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="John", surname="Doe")
        self.list_url = reverse('author-list')
        self.detail_url = reverse('author-update', args=[self.author.id])
        self.create_url = reverse('author-create')
        self.delete_url = reverse('author-delete', args=[self.author.id])

    def test_author_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.author.name)
        self.assertContains(response, self.author.surname)

    def test_author_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.author.name)
        self.assertContains(response, self.author.surname)

    def test_author_create(self):
        new_author_data = {
            'name': 'Jane',
            'surname': 'Smith'
        }
        response = self.client.post(self.create_url, new_author_data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful creation
        self.assertTrue(Author.objects.filter(name='Jane', surname='Smith').exists())

    def test_author_update(self):
        updated_data = {
            'name': 'John',
            'surname': 'Updated'
        }
        response = self.client.post(self.detail_url, updated_data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful update
        self.author.refresh_from_db()
        self.assertEqual(self.author.surname, 'Updated')

    def test_author_delete(self):
        response = self.client.post(self.delete_url)
        self.assertEqual(response.status_code, 302)  # Redirect after successful deletion
        self.assertFalse(Author.objects.filter(id=self.author.id).exists())

    def test_author_create_invalid_data(self):
        invalid_data = {
            'name': '',  # Empty name should be invalid
            'surname': 'Smith'
        }
        response = self.client.post(self.create_url, invalid_data)
        self.assertEqual(response.status_code, 200)  # Should return to the form
        self.assertFalse(Author.objects.filter(surname='Smith').exists())
        self.assertContains(response, "This field is required")  # Check for error message

    def test_author_update_invalid_data(self):
        invalid_data = {
            'name': 'John',
            'surname': ''  # Empty surname should be invalid
        }
        response = self.client.post(self.detail_url, invalid_data)
        self.assertEqual(response.status_code, 200)  # Should return to the form
        self.author.refresh_from_db()
        self.assertNotEqual(self.author.surname, '')  # Surname should not be updated
        self.assertContains(response, "This field is required")  # Check for error message
