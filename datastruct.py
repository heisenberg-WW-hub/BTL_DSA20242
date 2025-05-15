# datastruct.py

class Patient:
    def __init__(self, id, name, priority, arrival_time):
        self.id = id
        self.name = name
        self.priority = priority
        self.arrival_time = arrival_time

class Doctor:
    def __init__(self, id, name, specialization):
        self.id = id
        self.name = name
        self.specialization = specialization
