# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import generic
from django.urls import reverse
from django.contrib import messages
from tracker.forms import SupplySharingForm
from tracker.models import SupplySharing
from tracker.utils import get_cached_area


class SubmitSupplyShareRequestView(generic.CreateView):
    model = SupplySharing
    form_class = SupplySharingForm
    template_name = 'tracker/supply_sharing/create.html'

    def get_context_data(self, **kwargs):
        area_slug = self.kwargs.get('slug')
        context = super(SubmitSupplyShareRequestView, self).get_context_data(**kwargs)
        context['area'] = get_cached_area(area_slug)
        return context

    def get_success_url(self):
        area_slug = self.kwargs.get('slug')
        message = "Thank you for your submission!"
        messages.add_message(self.request, messages.SUCCESS, message)
        return reverse('tracker:submit_supplies', kwargs={'slug': area_slug})