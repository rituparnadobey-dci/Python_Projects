
from event import Event, EventManager


def get_user_input():
    event_name = input("Enter event name: ")
    event_date = input("Enter event date (YYYY-MM-DD): ")
    event_time = input("Enter event time: ")
    event_location = input("Enter event location: ")

    return Event(event_name, event_date, event_time, event_location)

if __name__ == "__main__":
    event_manager = EventManager()

    while True:
        new_event = get_user_input()
        event_manager.add_event(new_event)
   
        for event in event_manager.events:
            save_filename = f"{event.name}_events.txt"
            with open(save_filename, 'w') as file:
                file.write(f"{event.name},{event.date},{event.time},{event.location}\n")
                print(f"Events saved to {save_filename}")

        save_another = input("Do you want to save another event? (yes/no): ").lower()
        if save_another != 'yes':
            print("\nAll Events:")
            event_manager.view_events()

            print("Goodbye!")
            break
