def notify_students(students):
    for student in students:
        if student.assigned_event:
            print(f"Notification sent to {student.name} ({student.contact}): Assigned to {student.assigned_event}")
        else:
            print(f"Notification sent to {student.name} ({student.contact}): No event assigned")
