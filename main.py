#!/usr/bin/env python3
"""Точка входа. Показывает меню с двумя кнопками."""
import sys, os
import tkinter as tk
from tkinter import ttk

from mix_window import MixWindow
from dilution_window import DilutionWindow
from fractional_window import FractionalWindow


class MainMenu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Калькуляторы")
        self.geometry("280x180")
        self.resizable(False, False)
        self._build_ui()

    def _build_ui(self):
        ttk.Label(self, text="Выберите калькулятор", font=("Arial", 13)).pack(pady=20)

        ttk.Button(self, text="Разбавление самогона водой", command=self._open_dilution).pack(pady=5)
        ttk.Button(self, text="Смешивание двух жидкостей", command=self._open_mix).pack(pady=5)
        ttk.Button(self, text="Дробная перегонка", command=self._on_fract).pack(pady=5)

    def _open_dilution(self):
        DilutionWindow(self)

    def _open_mix(self):
        MixWindow(self)

    def _on_fract(self):
        FractionalWindow(self)

    def resource_path(relative_path):
        if getattr(sys, 'frozen', False):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)



if __name__ == "__main__":
    app = MainMenu()
    app.mainloop()
