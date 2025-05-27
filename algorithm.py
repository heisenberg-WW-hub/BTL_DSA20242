# algorithm.py
from datastruct import Patient, PriorityQueue
import time
from datetime import datetime

def assign_doctor(patient, doctors):
    """
    Trả về bác sĩ có số bệnh nhân ít nhất
    """
    doctors_sorted = sorted(doctors, key=lambda d: d['patient_count'])
    return doctors_sorted[0] if doctors_sorted else None


class HospitalAlgorithms:
    def __init__(self):
        self.queue = PriorityQueue()
        self.patient_id_counter = 1

    def enqueue_patient(self, name, priority):
        """Thêm bệnh nhân vào hàng đợi với độ ưu tiên."""
        if not (1 <= priority <= 3):
            raise ValueError("Ưu tiên phải từ 1 đến 3")
        patient = Patient(
            patient_id=self.patient_id_counter,
            name=name.strip(),
            arrival_time=time.time(),
            priority=priority,
            status="đang chờ"
        )
        self.queue.enqueue(patient)
        self.patient_id_counter += 1
        return patient.patient_id

    def dequeue_patient(self):
        """Lấy bệnh nhân có độ ưu tiên cao nhất ra khỏi hàng đợi."""
        patient = self.queue.dequeue()
        if not patient:
            raise ValueError("Hàng đợi trống")
        return patient

    def search_by_id(self, patient_id):
        """Tìm bệnh nhân theo ID."""
        patients = self.queue.to_list()
        for patient in patients:
            if patient.patient_id == patient_id:
                return patient
        return None

    def search_by_name(self, name):
        """Tìm bệnh nhân theo tên (khớp một phần, không phân biệt hoa thường)."""
        name = name.lower().strip()
        patients = self.queue.to_list()
        result_queue = PriorityQueue()
        for patient in patients:
            if name in patient.name.lower():
                result_queue.enqueue(patient)
        return result_queue

    def get_sorted_patients(self, sort_by="name"):
        """Lấy danh sách bệnh nhân đang chờ, sắp xếp theo trường yêu cầu."""
        valid_sort_keys = {"name", "priority", "arrival_time"}
        if sort_by not in valid_sort_keys:
            raise ValueError(f"Sort_by phải là một trong {valid_sort_keys}")

        # Lấy danh sách và lọc bệnh nhân đang chờ
        patients = self.queue.to_list()
        patients = [p for p in patients if p.status == "đang chờ"]

        # Sắp xếp
        if sort_by == "name":
            sorted_patients = sorted(patients, key=lambda x: x.name.lower())
        elif sort_by == "priority":
            sorted_patients = sorted(patients, key=lambda x: x.priority)
        else:  # arrival_time
            sorted_patients = sorted(patients, key=lambda x: x.arrival_time)

        # Chuyển về PriorityQueue
        result_queue = PriorityQueue()
        for patient in sorted_patients:
            result_queue.enqueue(patient)
        return result_queue

    def mark_done(self, patient_id):
        """Đánh dấu bệnh nhân đã khám (không xóa khỏi hàng đợi)."""
        patient = self.search_by_id(patient_id)
        if not patient:
            raise ValueError("Không tìm thấy bệnh nhân")
        if patient.status == "đã khám":
            raise ValueError("Bệnh nhân đã được đánh dấu là đã khám")
        patient.status = "đã khám"

    def display_queue(self):
        """Hiển thị hàng đợi hiện tại."""
        print("\nHàng đợi hiện tại:")
        patients = self.queue.to_list()
        for patient in patients:
            print(f"ID: {patient.patient_id}, Tên: {patient.name}, Ưu tiên: {patient.priority}, "
                  f"Đến: {datetime.fromtimestamp(patient.arrival_time).strftime('%Y-%m-%d %H:%M:%S')}, "
                  f"Trạng thái: {patient.status}")
