from student import Student
from event import Event

def collect_students():
    # Sample data collection (can be replaced with file/database input)
    students = [
        Student("Alice", "S001", ["Football", "Dance"], "alice@email.com", "2153789"),
        Student("Bob", "S002", ["Music", "Football"], "bob@email.com"),
        Student("Charlie", "S003", ["Dance"], "charlie@email.com"),
        Student("David", "S004", ["Football", "Music"], "david@email.com"),
        Student("Eve", "S005", ["Music"], "eve@email.com"),
        Student("Frank", "S006", ["Dance"], "frank@email.com"),
        Student("Grace", "S007", ["Football"], "grace@email.com"),
    ]
    return students

def collect_events():
    events = [
        Event("Football", "Sports", 2),
        Event("Dance", "Cultural", 2),
        Event("Music", "Cultural", 1),
    ]
    return events

def save_assignments(students):
    with open("assignments.txt", "w") as f:
        for student in students:
            assigned_event = student.assigned_event if student.assigned_event else "None"
            f.write(f"{student.name} ({student.reg_no}): {assigned_event}\n")
