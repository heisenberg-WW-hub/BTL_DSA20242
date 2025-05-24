import tkinter as tk
from tkinter import ttk
from logic import Doctor_Controller

class DoctorFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self._build_ui()
        self.load_data()

    def _build_ui(self):
        # Header with Back button
        header = tk.Frame(self)
        header.pack(fill='x', pady=5)
        back_btn = tk.Button(header, text="◀ Quay lại", command=lambda: self.controller.show_page("MenuFrame"))
        back_btn.pack(side='left', padx=10)
        tk.Label(header, text="Quản lý Bác sĩ", font=("Arial", 18)).pack(side='left', padx=20)

        # Control panel
        ctrl = tk.Frame(self)
        ctrl.pack(fill='x', padx=20, pady=5)
        tk.Button(ctrl, text="Thêm", width=10, command=self.on_add).pack(side='left', padx=5)
        tk.Button(ctrl, text="Sửa",  width=10, command=self.on_edit).pack(side='left', padx=5)
        tk.Button(ctrl, text="Xóa",  width=10, command=self.on_delete).pack(side='left', padx=5)
        tk.Label(ctrl, text="Tìm kiếm:").pack(side='left', padx=(20,5))
        self.search_var = tk.StringVar()
        tk.Entry(ctrl, textvariable=self.search_var, width=30).pack(side='left')
        tk.Button(ctrl, text="Go", command=self.on_search).pack(side='left', padx=5)

        # Data table
        cols = ("ID","Tên bác sĩ","Chuyên khoa","Điện thoại")
        self.tree = ttk.Treeview(self, columns=cols, show='headings')
        for c in cols:
            self.tree.heading(c, text=c)
            self.tree.column(c, width=150, anchor='center')
        self.tree.pack(fill='both', expand=True, padx=20, pady=10)
        self.tree.bind('<<TreeviewSelect>>', self.on_select)
        
    def load_data(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        records = Doctor_Controller().read_all()
        for rec in records:
            self.tree.insert('', 'end', values=(
                rec.get('id'), rec.get('name'), rec.get('specialty'), rec.get('phone')
            ))

    # Stub methods
    def on_add(self):
        pass

    def on_edit(self):
        pass

    def on_delete(self):
        pass

    def on_search(self):
        query = self.search_var.get().strip()
        for item in self.tree.get_children():
            self.tree.delete(item)
        if query:
            results = Doctor_Controller.search(query)
        else:
            results = Doctor_Controller.read_all()
        for d in results:
            self.tree.insert('', 'end', values=(
                d.doctor_id, d.name, d.specialty, d.phone
            ))

    def on_select(self, event):
        pass