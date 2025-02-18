import tkinter as tk
from tkinter import ttk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Beautiful Form UI")
        self.geometry("400x300")
        self.create_widgets()

    def create_widgets(self):
        # Create a frame for the form
        form_frame = ttk.Frame(self, padding="10")
        form_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Add form fields
        ttk.Label(form_frame, text="Name:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.name_entry = ttk.Entry(form_frame, width=30)
        self.name_entry.grid(row=0, column=1, pady=5)

        ttk.Label(form_frame, text="Email:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.email_entry = ttk.Entry(form_frame, width=30)
        self.email_entry.grid(row=1, column=1, pady=5)

        ttk.Label(form_frame, text="Phone:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.phone_entry = ttk.Entry(form_frame, width=30)
        self.phone_entry.grid(row=2, column=1, pady=5)

        # Add submit button
        self.submit_button = ttk.Button(form_frame, text="Submit", command=self.submit_form)
        self.submit_button.grid(row=3, column=0, columnspan=2, pady=10)

    def submit_form(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        print(f"Name: {name}, Email: {email}, Phone: {phone}")

if __name__ == "__main__":
    app = Application()
    app.mainloop()
