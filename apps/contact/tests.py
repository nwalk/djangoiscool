from django.test import TestCase
from django.core.urlresolvers import resolve, reverse
from . import views
from django.shortcuts import render_to_response


class ContactPageTest(TestCase):
    """Test the contact page"""

    def test_contact_url(self):
        contact_url = resolve(reverse('contact:contact_form'))
        return self.assertEqual(contact_url.func.__name__,
                                views.ContactView.__name__)

    def test_uses_contact_form_html_template(self):
        """Test the template"""

        template = self.client.get('/contact')
        self.assertTemplateUsed(template, "contact_form.html")

    #CSRF token will cause this test to fail
    def test_returns_exact_html(self):
        """Test expected HTML"""

        contact_form = self.client.get("/contact")
        self.assertEquals(
           contact_form.content,
           render_to_response("contact_form.html").content
        )


class ContactThanksPageTest(TestCase):
    """Test the contact page"""
    
    def test_contact_thanks_url(self):
        contact_thanks = resolve(reverse('contact:contact_thanks'))
        return self.assertEqual(contact_thanks.func.__name__,
                                views.ContactThanksView.__name__)

    def test_uses_contact_thanks_html_template(self):
        """Test the template"""

        template = self.client.get('/contact/thanks')
        self.assertTemplateUsed(template, "contact_thanks.html")

    def test_returns_exact_html(self):
        """Test expected HTML"""

        contact_thanks = self.client.get("/contact/thanks")
        self.assertEquals(
            contact_thanks.content,
            render_to_response("contact_thanks.html").content
        )
