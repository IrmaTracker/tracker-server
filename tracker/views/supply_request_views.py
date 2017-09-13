# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import generic
from django.urls import reverse
from django.contrib import messages
from tracker.forms import SupplyRequestForm
from tracker.models import SupplyRequest
from tracker.utils import get_cached_area


class SubmitSupplyRequestView(generic.CreateView):
    model = SupplyRequest
    form_class = SupplyRequestForm
    template_name = 'tracker/supply_request/create.html'

    def get_context_data(self, **kwargs):
        area_slug = self.kwargs.get('slug')
        context = super(SubmitSupplyRequestView, self).get_context_data(**kwargs)
        context['area'] = get_cached_area(area_slug)
        return context

    def get_success_url(self):
        area_slug = self.kwargs.get('slug')
        message = "Thank you for your submission!"
        messages.add_message(self.request, messages.SUCCESS, message)
        return reverse('tracker:request_supplies', kwargs={'slug': area_slug})