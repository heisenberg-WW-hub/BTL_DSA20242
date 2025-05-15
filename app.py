# app.py
import tkinter as tk
from tkinter import messagebox
from logic import add_patient

def submit_patient():
    name = entry_name.get()
    priority = int(entry_priority.get())
    add_patient(name, priority)
    messagebox.showinfo("Thành công", "Đã thêm bệnh nhân")

root = tk.Tk()
root.title("Hệ thống khám bệnh")

tk.Label(root, text="Tên bệnh nhân:").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Mức độ ưu tiên (1-10):").pack()
entry_priority = tk.Entry(root)
entry_priority.pack()

tk.Button(root, text="Gửi", command=submit_patient).pack()

root.mainloop()
