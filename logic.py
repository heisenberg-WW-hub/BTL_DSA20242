# logic.py
from database import execute_query, fetch_query
from algorithm import assign_doctor

def add_patient(name, priority):
    # Thêm bệnh nhân vào DB
    query = "INSERT INTO patients (name, priority) VALUES (%s, %s)"
    execute_query(query, (name, priority))

    # Gán bác sĩ
    doctors = fetch_query("SELECT d.id, d.name, COUNT(p.id) AS patient_count FROM doctors d LEFT JOIN patients p ON d.id = p.assigned_doctor_id GROUP BY d.id")
    doctor = assign_doctor({'name': name, 'priority': priority}, doctors)

    if doctor:
        update_query = "UPDATE patients SET assigned_doctor_id = %s WHERE name = %s"
        execute_query(update_query, (doctor['id'], name))
