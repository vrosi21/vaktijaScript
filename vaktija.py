import json
from icalendar import Calendar, Event
from datetime import datetime, timedelta

def create_event(date, time, summary):
    event = Event()
    start = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
    end = start + timedelta(minutes=10)
    event.add('dtstart', start)
    event.add('dtend', end)
    event.add('summary', summary)
    return event

def convert_to_ical(json_data):
    cal = Calendar()
    prayers = ["Fajr", "Sunrise", "Dhuhr", "Asr", "Maghrib", "Isha"]
    year = json_data['godina']
    for month_index, month in enumerate(json_data['mjesec']):
        for day_index, day in enumerate(month['dan']):
            date = datetime(year, month_index + 1, day_index + 1).strftime("%Y-%m-%d")
            vakat_times = day['vakat']
            for time, prayer in zip(vakat_times, prayers):
                event = create_event(date, time, prayer)
                cal.add_component(event)
    return cal.to_ical()

with open('year.json', 'r') as f:
    data_year = json.load(f)

ical_data = convert_to_ical(data_year)

with open('prayer_times.ics', 'wb') as f:
    f.write(ical_data)
