# logic.py
from database import execute_query, fetch_query
from algorithm import assign_doctor

class Patient_Controller:
    def __init__(self):
        pass

    def add_patient(self, name, priority):
        # Thêm bệnh nhân vào DB
        query = "INSERT INTO patients (name, priority) VALUES (%s, %s)"
        execute_query(query, (name, priority))

        # Gán bác sĩ
        doctors = fetch_query("SELECT d.id, d.name, COUNT(p.id) AS patient_count FROM doctors d LEFT JOIN patients p ON d.id = p.assigned_doctor_id GROUP BY d.id")
        doctor = assign_doctor({'name': name, 'priority': priority}, doctors)

        if doctor:
            update_query = "UPDATE patients SET assigned_doctor_id = %s WHERE name = %s"
            execute_query(update_query, (doctor['id'], name))
            
    def read_all(self):
        # Lấy danh sách bệnh nhân từ DB
        query = "SELECT * FROM patients"
        return fetch_query(query)

class Doctor_Controller:
    def __init__(self):
        pass

    def add_doctor(self, name, specialization):
        # Thêm bác sĩ vào DB
        query = "INSERT INTO doctors (name, specialization) VALUES (%s, %s)"
        execute_query(query, (name, specialization))

    def read_all(self):
        # Lấy danh sách bác sĩ từ DB
        query = "SELECT * FROM doctors"
        return fetch_query(query)
    