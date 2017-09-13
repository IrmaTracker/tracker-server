# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import generic
from tracker.models import Area
from tracker.utils import get_safe_person_count, get_missing_person_count


class AreaListView(generic.ListView):
    """
    The landing page - shows all areas
    """
    model = Area
    template_name = 'tracker/area/list.html'


class AreaDetailView(generic.DetailView):
    """
    Detail page for a given area
    """
    model = Area
    template_name = 'tracker/area/detail.html'

    def get_context_data(self, **kwargs):
        area_slug = self.kwargs.get('slug')
        context = super(AreaDetailView, self).get_context_data(**kwargs)
        context['safe'] = get_safe_person_count(area_slug)
        context['missing'] = get_missing_person_count(area_slug)
        return context