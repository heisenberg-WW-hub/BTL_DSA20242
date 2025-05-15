# algorithm.py

def assign_doctor(patient, doctors):
    """
    Trả về bác sĩ có số bệnh nhân ít nhất
    """
    doctors_sorted = sorted(doctors, key=lambda d: d['patient_count'])
    return doctors_sorted[0] if doctors_sorted else None
