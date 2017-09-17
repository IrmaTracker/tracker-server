# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import generic
from tracker.forms import ActivityReportForm
from tracker.models import ActivityReport
from tracker.utils import get_cached_area


class CreateActivityReportView(generic.CreateView):
    model = ActivityReport
    form_class = ActivityReportForm
    template_name = 'tracker/activity_report/create.html'

    def form_valid(self, form):
        area_slug = self.kwargs.get('slug')
        form.instance.area = get_cached_area(area_slug)
        return super(CreateActivityReportView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        area_slug = self.kwargs.get('slug')
        context = super(CreateActivityReportView, self).get_context_data(**kwargs)
        context['area'] = get_cached_area(area_slug)
        return context


class ActivityReportListView(generic.ListView):
    model = ActivityReport
    paginate_by = 25
    template_name = 'tracker/activity_report/list.html'

    def get_queryset(self):
        area_slug = self.kwargs.get('slug')
        area = get_cached_area(area_slug)
        return self.model.objects.filter(area_id=area.id)

    def get_context_data(self, **kwargs):
        area_slug = self.kwargs.get('slug')
        context = super(ActivityReportListView, self).get_context_data(**kwargs)
        context['area'] = get_cached_area(area_slug)
        return context


class ActivityReportDetailView(generic.DetailView):
    model = ActivityReport
    template_name = 'tracker/activity_report/detail.html'

    def get_queryset(self):
        area_slug = self.kwargs.get('slug')
        area = get_cached_area(area_slug)
        return self.model.objects.filter(area_id=area.id)

    def get_context_data(self, **kwargs):
        area_slug = self.kwargs.get('slug')
        context = super(ActivityReportDetailView, self).get_context_data(**kwargs)
        context['area'] = get_cached_area(area_slug)
        return context