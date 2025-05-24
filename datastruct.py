# datastruct.py

class Patient:
    def __init__(self, id, name, birth_date, gender, priority, arrival_time, phone, address, address_email = None):

        self.id = id # mã bệnh nhân
        self.full_name = name # tên bệnh nhân
        self.priority = priority # mức độ ưu tiên
        self.birth_date = birth_date # ngày sinh
        self.gender = gender # giới tính
        self.arrival_time = arrival_time # thời gian đến
        self.phone = phone # số điện thoại
        self.address = address # địa chỉ
        self.address_email = address_email # địa chỉ email (nếu có)
        self.status = None # trạng thái (đang chờ, đã khám, đã thanh toán)

class Doctor:
    def __init__(self, id, name, specialization):
        self.id = id
        self.name = name
        self.specialization = specialization
