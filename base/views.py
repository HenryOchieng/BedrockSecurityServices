from __future__ import unicode_literals

from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.contrib.messages.views import SuccessMessageMixin

from django.core.mail import send_mail, get_connection
from django.conf import settings

from .forms import ContactForm
from .models import Service

class ServiceListAndFormView(SuccessMessageMixin, ListView, FormView):
    model = Service # data from database
    template_name = 'base/index.html'
    context_object_name = 'list_services' # name of the var in html template
    queryset = Service.objects.all().order_by("-pub_date")#  list of all projects
    object_list = None

    form_class = ContactForm
    success_url = '/' # After submiting the form keep staying on the same url
    success_message = 'Thank you for reaching out, a reply will be sent to you shortly!'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        cd = form.cleaned_data
        con = get_connection('django.core.mail.backends.console.EmailBackend')
        send_mail(
            cd['name'],
            cd['message'],
            cd.get('email', ''),
            ['henryochieng8@gmail.com'],
            fail_silently=True
        )
        return super(ServiceListAndFormView, self).form_valid(form)