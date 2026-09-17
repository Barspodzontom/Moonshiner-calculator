import tkinter as tk
from tkinter import ttk, messagebox
from logic import calc_fractional_distillation

class FractionalWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Дробная перегонка")
        self.configure(bg="#6ea6de")
        self.geometry("400x550")  # Чуть меньше, чтобы не было пустот, как на скринах
        self.resizable(False, False)

        self._build_ui()

    def _build_ui(self):
        # Общий контейнер для формы.
        # Используем Frame, чтобы задать ему фон и управлять отступами всей формы сразу.
        form_frame = tk.Frame(self, bg="#6ea6de")
        form_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Настраиваем веса колонок для grid, чтобы они растягивались красиво
        # Колонка 0 (текст) - занимает все свободное место
        form_frame.columnconfigure(0, weight=1)
        # Колонка 1 (поле ввода) - фиксированная ширина
        form_frame.columnconfigure(1, weight=0)
        # Колонка 2 (единицы) - минимальная ширина
        form_frame.columnconfigure(2, weight=0)

        row_idx = 0
        label_fg = "#333333"
        entry_bg = "#ffffff"
        entry_font = ("Arial", 10)

        # --- 1. Объем спирта-сырца ---
        tk.Label(form_frame, text="Объем спирта-сырца:", bg="#6ea6de", fg=label_fg).grid(row=row_idx, column=0, sticky="w", pady=10)
        self.entry_a = tk.Entry(form_frame, width=10, justify="right", font=entry_font, relief="flat", bg=entry_bg)
        self.entry_a.grid(row=row_idx, column=1, padx=5, pady=10)
        tk.Label(form_frame, text="литров", bg="#6ea6de", fg=label_fg).grid(row=row_idx, column=2, sticky="w", pady=10)
        row_idx += 1

        # --- 2. Крепость сырья ---
        tk.Label(form_frame, text="Крепость спирта-сырца:", bg="#6ea6de", fg=label_fg).grid(row=row_idx, column=0, sticky="w", pady=10)
        self.entry_c = tk.Entry(form_frame, width=10, justify="right", font=entry_font, relief="flat", bg=entry_bg)
        self.entry_c.grid(row=row_idx, column=1, padx=5, pady=10)
        tk.Label(form_frame, text="°", bg="#6ea6de", fg=label_fg).grid(row=row_idx, column=2, sticky="w", pady=10)
        row_idx += 1

        # --- 3. Крепость на выходе ---
        tk.Label(form_frame, text="Крепость на выходе:", bg="#6ea6de", fg=label_fg).grid(row=row_idx, column=0, sticky="w", pady=10)
        self.entry_b = tk.Entry(form_frame, width=10, justify="right", font=entry_font, relief="flat", bg=entry_bg)
        self.entry_b.grid(row=row_idx, column=1, padx=5, pady=10)
        tk.Label(form_frame, text="°", bg="#6ea6de", fg=label_fg).grid(row=row_idx, column=2, sticky="w", pady=10)
        row_idx += 1

        # --- 4. Доля «голов» (используем ttk.Combobox для современного вида) ---
        tk.Label(form_frame, text="Доля «голов»:", bg="#6ea6de", fg=label_fg).grid(row=row_idx, column=0, sticky="w", pady=10)

        style = ttk.Style()
        style.configure("My.TCombobox", fieldbackground=entry_bg, background=entry_bg, foreground=label_fg)

        self.combo_d = ttk.Combobox(form_frame, values=["5%", "7%", "10%"], state="readonly", width=8, style="My.TCombobox")
        self.combo_d.current(2)
        self.combo_d.grid(row=row_idx, column=1, padx=5, pady=10, sticky="ew")
        # У комбобокса нет отдельной метки единицы, % уже внутри значения
        row_idx += 1

        # --- 5. Доля «хвостов» ---
        tk.Label(form_frame, text="Доля «хвостов»:", bg="#6ea6de", fg=label_fg).grid(row=row_idx, column=0, sticky="w", pady=10)
        self.combo_e = ttk.Combobox(form_frame, values=["10%", "15%", "20%"], state="readonly", width=8, style="My.TCombobox")
        self.combo_e.current(1)
        self.combo_e.grid(row=row_idx, column=1, padx=5, pady=10, sticky="ew")
        row_idx += 1

        # --- Кнопка ---
        btn_frame = tk.Frame(form_frame, bg="#6ea6de")
        btn_frame.grid(row=row_idx, column=0, columnspan=3, pady=30) # Растягиваем на 3 колонки

        calc_btn = tk.Button(btn_frame, text="Рассчитать", command=self._on_fract,
                             bg="#2c3e50", fg="white", font=("Arial", 11, "bold"),
                             relief="flat", padx=20, pady=8)
        calc_btn.pack()

        # --- Результат ---
        self.label_result = tk.Label(form_frame, text="", bg="#6ea6de", fg="#2c3e50",
                                      font=("Consolas", 11), justify="left", anchor="n")
        self.label_result.grid(row=row_idx+1, column=0, columnspan=3, sticky="nsew", pady=20)

    def _on_fract(self):
        try:
            # Проверка на пустоту
            val_a = self.entry_a.get().strip()
            val_c = self.entry_c.get().strip()
            val_b = self.entry_b.get().strip()

            if not val_a or not val_c or not val_b:
                raise ValueError("Заполните все числовые поля!")

            a = float(val_a)
            c = float(val_c)
            b = float(val_b)

            # Для Combobox get() возвращает строку, например "10%"
            d = float(self.combo_d.get().replace("%", ""))
            e = float(self.combo_e.get().replace("%", ""))

            # Здесь будет твой расчет
            result = calc_fractional_distillation(a, c, b, d, e)

            # Для теста, если нет файла logic.py, закомментируй строку выше и раскомментируй этот блок:
            #result = {'heads': a * d/100, 'body': a * 0.7, 'tails': a * e/100, 'total': a * 0.85}

            self.label_result.config(text=(
                f"Головы: {result['heads']:.2f} л\n"
                f"Тело: {result['body']:.2f} л\n"
                f"Хвосты: {result['tails']:.2f} л\n"
                f"Абсолютного спирта: {result['total']:.2f} л"
            ))

        except ValueError as e:
            messagebox.showerror("Ошибка ввода", str(e))
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))
