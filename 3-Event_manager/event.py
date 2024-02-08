from datetime import datetime, timedelta


class Event:
    def __init__(self, name, date, time, location):
        self.name = name
        self.date = date
        self.time = time
        self.location = location


    def calculate_reminders(self):
        event_datetime = datetime.strptime(f"{self.date} {self.time}", "%Y-%m-%d %H:%M")
        
        reminder_7_days = event_datetime - timedelta(days=7)
        
        reminder_1_hour = event_datetime - timedelta(hours=1)
        
        return reminder_7_days, reminder_1_hour

class EventManager:
    def __init__(self):
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def view_events(self):
        for event in self.events:
            print(f"{event.name} - {event.date} at {event.time}, {event.location}")

    def save_events(self, filename):
        with open(filename, 'w') as file:
            for event in self.events:
                file.write(f"{event.name},{event.date},{event.time},{event.location}\n")
