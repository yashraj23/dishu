class Student:
    def __init__(self, name, reg_no, preferences, contact, phone=None):
        self.name = name
        self.reg_no = reg_no
        self.preferences = preferences  # List of event names
        self.contact = contact
        self.assigned_event = None
        self.phone = None

    def __repr__(self):
        return f"Student({self.name}, {self.reg_no}, {self.preferences}, {self.contact}, {self.assigned_event})"