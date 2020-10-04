import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import *


def run():
    fhand = open('many/load.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Category.objects.all().delete()
    State.objects.all().delete()
    Region.objects.all().delete()
    ISO.objects.all().delete()
    Site.objects.all().delete()

    # Format
    # email,role,course
    # jane@tsugi.org,I,Python
    # ed@tsugi.org,L,Python

    for row in reader:
        print(row)

        category, created = Category.objects.get_or_create(name=row[7])
        state, created = State.objects.get_or_create(name=row[8])
        region, created = Region.objects.get_or_create(name=row[9])
        iso, created = ISO.objects.get_or_create(name=row[10])

        m = Site(name=row[0],
                 description=row[1],
                 justification=row[2],
                 year=row[3],
                 longitude=row[4],
                 latitude=row[5],
                 area_hectares=row[6],
                 category=category,
                 states=state,
                 region=region,
                 iso=iso)
        m.save()
