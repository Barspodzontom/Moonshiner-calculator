"""Окно калькулятора разбавления самогона водой."""
import tkinter as tk
from tkinter import ttk, messagebox
from logic import calc_dilution


class DilutionWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Разбавление самогона водой")
        self.geometry("320x320")
        self.resizable(False, False)
        self._build_ui()

    def _build_ui(self):
        pad = {"padx": 10, "pady": 5}

        ttk.Label(self, text="Крепость исходного (%)").pack(pady=(15, 0))
        self.entry_a = ttk.Entry(self)
        self.entry_a.pack(**pad)

        ttk.Label(self, text="Желаемая крепость (%)").pack()
        self.entry_b = ttk.Entry(self)
        self.entry_b.pack(**pad)

        ttk.Label(self, text="Объём самогона (л)").pack()
        self.entry_c = ttk.Entry(self)
        self.entry_c.pack(**pad)

        ttk.Button(self, text="Рассчитать", command=self._on_calc).pack(pady=20)

        self.label_result = ttk.Label(self, text="", font=("Arial", 11))
        self.label_result.pack()

    def _on_calc(self):
        try:
            a = float(self.entry_a.get())
            b = float(self.entry_b.get())
            c = float(self.entry_c.get())

            water = calc_dilution(a, b, c)
            self.label_result.config(text=f"Добавьте воды: {water:.2f} л")
        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))
