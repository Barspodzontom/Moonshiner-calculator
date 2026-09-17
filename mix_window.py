"""Окно калькулятора смешивания двух жидкостей."""
import tkinter as tk
from tkinter import ttk, messagebox
from logic import calc_mix


class MixWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Смешивание двух жидкостей")
        self.geometry("300x450")
        self.resizable(False, False)
        self._build_ui()

    def _build_ui(self):
        pad = {"padx": 10, "pady": 3}

        ttk.Label(self, text="Жидкость 1").pack(pady=(10, 0))

        ttk.Label(self, text="Крепость (%)").pack()
        self.entry_c1 = ttk.Entry(self)
        self.entry_c1.pack(**pad)

        ttk.Label(self, text="Объём (л)").pack()
        self.entry_v1 = ttk.Entry(self)
        self.entry_v1.pack(**pad)

        ttk.Label(self, text="Жидкость 2").pack(pady=(10, 0))

        ttk.Label(self, text="Крепость (%)").pack()
        self.entry_c2 = ttk.Entry(self)
        self.entry_c2.pack(**pad)

        ttk.Label(self, text="Объём (л)").pack()
        self.entry_v2 = ttk.Entry(self)
        self.entry_v2.pack(**pad)

        ttk.Button(self, text="Рассчитать", command=self._on_calc).pack(pady=15)

        self.label_result = ttk.Label(self, text="", font=("Arial", 11))
        self.label_result.pack()

    def _on_calc(self):
        try:
            c1 = float(self.entry_c1.get())
            v1 = float(self.entry_v1.get())
            c2 = float(self.entry_c2.get())
            v2 = float(self.entry_v2.get())

            strength, volume = calc_mix(c1, v1, c2, v2)
            self.label_result.config(
                text=f"Крепость: {strength:.2f}%\nОбъём: {volume:.2f} л"
            )
        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))
