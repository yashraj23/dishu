def match_students_to_events(students, events):
    event_dict = {event.name: event for event in events}
    for student in students:
        for pref in student.preferences:
            event = event_dict.get(pref)
            if event and event.assign_student(student):
                break  # Stop after assigning to one event
