from django.core.cache import cache
from djqscsv import write_csv
from tracker.models import Person, Area


def export_file():
    people = Person.objects.filter(area__slug__in=['st-maarten', 'st-martin'], safe=False, duplicate=False).values(
        'name', 'district', 'phonenumber', 'address', 'safe', 'extra_info'
    )

    name = "sxm-safe.csv"
    with open(name, 'w') as csv_file:
        write_csv(people, csv_file)


def get_cached_area(slug):
    cache_key = slug
    cached_area = cache.get(cache_key)
    if cached_area:
        return cached_area
    area = Area.objects.get(slug=slug)
    cache.set(cache_key, area, 3600)
    return area


def get_missing_person_count(slug):
    area = get_cached_area(slug)
    cache_key = "{slug}.missin_count".format(slug=area.slug)
    cached_count = cache.get(cache_key)
    if cached_count:
        return cached_count
    count = area.person_set.filter(safe=False, duplicate=False).count()
    cache.set(cache_key, count, 600)
    return count


def get_safe_person_count(slug):
    area = get_cached_area(slug)
    cache_key = "{slug}.safe_count".format(slug=area.slug)
    cached_count = cache.get(cache_key)
    if cached_count:
        return cached_count
    count = area.person_set.filter(safe=True, duplicate=False).count()
    cache.set(cache_key, count, 600)
    return count