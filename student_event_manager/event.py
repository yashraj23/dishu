class Event:
    def __init__(self, name, event_type, capacity):
        self.name = name
        self.event_type = event_type
        self.capacity = capacity
        self.assigned_students = []

    def assign_student(self, student):
        if len(self.assigned_students) < self.capacity:
            self.assigned_students.append(student)
            student.assigned_event = self.name
            return True
        return False

    def __repr__(self):
        return f"Event({self.name}, {self.event_type}, {self.capacity}, {self.assigned_students})"