from .models import CCTVFootage
from datetime import timedelta


def calculate_working_hours(person):
    # Filter entries and exits
    entries = CCTVFootage.objects.filter(person=person, is_entry=True).order_by('timestamp')
    exits = CCTVFootage.objects.filter(person=person, is_entry=False).order_by('timestamp')

    total_work_time = timedelta()

    # Pair each entry with a corresponding exit (if any)
    for entry, exit in zip(entries, exits):
        total_work_time += (exit.timestamp - entry.timestamp)

    return total_work_time
