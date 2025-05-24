import tkinter as tk
from Doctor_UI import DoctorFrame
from Partient_UI import PatientFrame


class ClinicApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hệ thống quản lý khám bệnh")
        self.geometry("1200x800")

        container = tk.Frame(self)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.pages = {}
        for PageClass in (MenuFrame, PatientFrame, DoctorFrame): #, RoomFrame, AppointmentFrame
            page = PageClass(container, self)
            page.grid(row=0, column=0, sticky="nsew")
            self.pages[PageClass.__name__] = page

        self.show_page("MenuFrame")

    def show_page(self, page_name):
        frame = self.pages[page_name]
        frame.tkraise()


class MenuFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        tk.Label(self, text="Menu Chính", font=("Arial", 24)).pack(pady=40)
        options = [
            ("Quản lý bệnh nhân", "PatientFrame"),
            ("Quản lý bác sĩ",    "DoctorFrame"),
            # ("Quản lý phòng khám","RoomFrame"),
            # ("Quản lý lượt khám", "AppointmentFrame"),
        ]
        for text, frame in options:
            btn = tk.Button(self, text=text, width=30, height=2,
                            command=lambda f=frame: controller.show_page(f))
            btn.pack(pady=10)


if __name__ == "__main__":
    app = ClinicApp()
    app.mainloop()

