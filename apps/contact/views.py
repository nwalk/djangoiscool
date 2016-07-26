from django.core.mail import send_mail, BadHeaderError
from django.views import generic
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from . import forms


class ContactView(generic.FormView):
    template_name = 'contact_form.html'
    form_class = forms.EmailForm

    def form_valid(self, form):
        message = "Reply to: {sender}\n".format(sender=form.cleaned_data.get('sender'))
        message += "\n\nMessage:\n{0}".format(form.cleaned_data.get('message'))
        try:
            send_mail(
                subject=form.cleaned_data.get('subject').strip(),
                message=message,
                from_email='FROM_EMAIL@domain.com',
                recipient_list=['RECIPIENT@domain.com'],
            )
        except BadHeaderError:
                return HttpResponse('Invalid header found.')

        return super(ContactView, self).form_valid(form)

    def form_invalid(self, form):
        return HttpResponse("<h4>Form invalid...</h4>")

    def get_success_url(self):
        return reverse('contact:contact_thanks')


class ContactThanksView(generic.TemplateView):
    template_name = 'contact_thanks.html'
