from data_manager import collect_students, collect_events
from matcher import match_students_to_events
from notifier import notify_students

def main():
    students = collect_students()
    events = collect_events()
    match_students_to_events(students, events)
    notify_students(students)

if __name__ == "__main__":
    main()
