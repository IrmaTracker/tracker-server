# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import generic
from django.urls import reverse
from django.contrib import messages
from tracker.forms import EmergencyRequestForm
from tracker.models import EmergencyRequest
from tracker.utils import get_cached_area


class SubmitEmergencyRequestView(generic.CreateView):
    model = EmergencyRequest
    form_class = EmergencyRequestForm
    template_name = 'tracker/emergency_request/create.html'

    def get_context_data(self, **kwargs):
        area_slug = self.kwargs.get('slug')
        context = super(SubmitEmergencyRequestView, self).get_context_data(**kwargs)
        context['area'] = get_cached_area(area_slug)
        return context

    def get_success_url(self):
        area_slug = self.kwargs.get('slug')
        message = "Your emergency request has been received."
        messages.add_message(self.request, messages.SUCCESS, message)
        return reverse('tracker:submit_supplies', kwargs={'slug': area_slug})
