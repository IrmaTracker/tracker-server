# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import generic
from tracker.forms import PersonForm
from tracker.models import Person
from tracker.utils import get_missing_person_count, get_cached_area, get_safe_person_count


class PersonListView(generic.ListView):
    """
    Unfiltered list of all submitted people
    """
    model = Person
    paginate_by = 50
    template_name = 'tracker/person/list.html'

    def get_context_data(self, **kwargs):
        area_slug = self.kwargs.get('slug')
        context = super(PersonListView, self).get_context_data(**kwargs)
        context['area'] = get_cached_area(area_slug)
        context['safe'] = get_safe_person_count(area_slug)
        context['missing'] = get_missing_person_count(area_slug)
        context['showing'] = 'All'
        return context

    def get_queryset(self):
        area_slug = self.kwargs.get('slug')
        if self.request.GET.get('q'):
            name = self.request.GET.get('q')
            return Person.objects.filter(name__icontains=name, area__slug=area_slug)
        return Person.objects.filter(area__slug=area_slug)


class PersonMarkedSafeListView(generic.ListView):
    """
    View that filters by people who have been marked safe.
    """
    model = Person
    paginate_by = 50
    template_name = 'tracker/person/list.html'

    def get_context_data(self, **kwargs):
        area_slug = self.kwargs.get('slug')
        context = super(PersonMarkedSafeListView, self).get_context_data(**kwargs)
        context['area'] = get_cached_area(area_slug)
        context['safe'] = get_safe_person_count(area_slug)
        context['missing'] = get_missing_person_count(area_slug)
        context['showing'] = 'Marked Safe'
        return context

    def get_queryset(self):
        area_slug = self.kwargs.get('slug')
        if self.request.GET.get('q'):
            name = self.request.GET.get('q')
            return Person.objects.filter(name__icontains=name, area__slug=area_slug, safe=True)
        return Person.objects.filter(area__slug=area_slug, safe=True)


class PersonMissingListView(generic.ListView):
    """
    View that filters by people who have not been
    marked safe.
    """
    model = Person
    paginate_by = 50
    template_name = 'tracker/person/list.html'

    def get_context_data(self, **kwargs):
        area_slug = self.kwargs.get('slug')
        context = super(PersonMissingListView, self).get_context_data(**kwargs)
        context['area'] = get_cached_area(area_slug)
        context['safe'] = get_safe_person_count(area_slug)
        context['missing'] = get_missing_person_count(area_slug)
        context['showing'] = 'Missing'
        return context

    def get_queryset(self):
        area_slug = self.kwargs.get('slug')
        if self.request.GET.get('q'):
            name = self.request.GET.get('q')
            return Person.objects.filter(name__icontains=name, area__slug=area_slug, safe=False)
        return Person.objects.filter(area__slug=area_slug, safe=False)


class CreatePersonView(generic.CreateView):
    """
    Add a missing person to the tracker database.
    """

    model = Person
    form_class = PersonForm
    template_name = 'tracker/person/create.html'

    def get_context_data(self, **kwargs):
        area_slug = self.kwargs.get('slug')
        context = super(CreatePersonView, self).get_context_data(**kwargs)
        context['area'] = get_cached_area(area_slug)
        return context

    def form_valid(self, form):
        area_slug = self.kwargs.get('slug')
        area = get_cached_area(area_slug)
        form.instance.area_id = area.id
        return super(CreatePersonView, self).form_valid(form)


class UpdatePersonView(generic.UpdateView):
    """
    View or make updates to a person's profiles
    """
    model = Person
    form_class = PersonForm
    template_name = 'tracker/person/update.html'

    def get_context_data(self, **kwargs):
        area_slug = self.kwargs.get('slug')
        context = super(UpdatePersonView, self).get_context_data(**kwargs)
        context['area'] = get_cached_area(area_slug)
        return context