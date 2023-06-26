import tkinter as tk


def calculate_coefficient():
    # Получаем выбранную юзером формулу
    formula = formula_choice.get()

    # Выполняем расчет в соответствии с выбранной формулой
    if formula == 1:
        # Расчет коэффициента по формуле 1
        nд = float(nд_entry.get())
        Sд = float(Sд_entry.get())
        Sл = float(Sл_entry.get())
        Kб = 1.06
        K = (nд * Sд) / (Sл * Kб)
        result_label.config(text="Рассчитанный коэффициент: {:.2f}".format(K))
    elif formula == 2:
        # Расчет коэффициента по формуле 2
        nл = float(nл_entry.get())
        Sл = float(Sл_entry.get())
        Kб = 1.06
        Sзак = float(Sзак_entry.get())
        Kарх = (nл * Sл * Kб) / Sзак
        result_label.config(text="Рассчитанный коэффициент: {:.2f}".format(Kарх))
    elif formula == 3:
        # Расчет коэффициента по формуле 3
        nл = float(nл_entry.get())
        Sл = float(Sл_entry.get())
        Sост = float(Sост_entry.get())
        Sзак = float(Sзак_entry.get())
        Kб = 1.06
        Kарх_ост = (nл * Sл - Sост * 0.75) / (Sзак * Kб)
        result_label.config(text="Рассчитанный коэффициент: {:.2f}".format(Kарх_ост))
    else:
        # Выводим сообщение об ошибке при некорректном выборе формулы
        result_label.config(text="Некорректный выбор формулы.")


def handle_formula_selection():
    # Получаем выбранную юзером формулу
    formula = formula_choice.get()

    if formula == 1:
        # Для формулы 1 отключаем ненужные поля и включаем необходимые
        nд_entry.config(state=tk.NORMAL)
        Sд_entry.config(state=tk.NORMAL)
        Sл_entry.config(state=tk.NORMAL)
        Sзак_entry.config(state=tk.DISABLED)
        nл_entry.config(state=tk.DISABLED)
        Sост_entry.config(state=tk.DISABLED)
    elif formula == 2:
        # Для формулы 2 отключаем ненужные поля и включаем необходимые
        nд_entry.config(state=tk.DISABLED)
        Sд_entry.config(state=tk.DISABLED)
        Sл_entry.config(state=tk.NORMAL)
        Sзак_entry.config(state=tk.NORMAL)
        nл_entry.config(state=tk.NORMAL)
        Sост_entry.config(state=tk.DISABLED)
    elif formula == 3:
        # Для формулы 3 отключаем ненужные поля и включаем необходимые
        nд_entry.config(state=tk.DISABLED)
        Sд_entry.config(state=tk.DISABLED)
        Sл_entry.config(state=tk.NORMAL)
        Sзак_entry.config(state=tk.NORMAL)
        nл_entry.config(state=tk.NORMAL)
        Sост_entry.config(state=tk.NORMAL)


# Основное окно
window = tk.Tk()
window.title("Калькулятор коэффициента")

# Список выбора формулы
formula_choice = tk.IntVar()
formula_label = tk.Label(window, text="Выберите формулу для расчета коэффициента:")
formula_label.pack()

formula1_radio = tk.Radiobutton(window, text="1) K = (nд * Sд) / Sл * Kб", variable=formula_choice, value=1,
                                command=handle_formula_selection)
formula1_radio.pack()

formula2_radio = tk.Radiobutton(window, text="2) Kарх = nл * Sл * Kб / Sзак", variable=formula_choice, value=2,
                                command=handle_formula_selection)
formula2_radio.pack()

formula3_radio = tk.Radiobutton(window, text="3) Kарх(ост) = (nл * Sл - Sост * 0.75) / Sзак * Kб",
                                variable=formula_choice, value=3, command=handle_formula_selection)
formula3_radio.pack()

# Поля ввода
nд_label = tk.Label(window, text="nд - Количество изделий на листе:")
nд_label.pack()
nд_entry = tk.Entry(window, state=tk.DISABLED)
nд_entry.pack()

Sд_label = tk.Label(window, text="Sд - Площадь изделия:")
Sд_label.pack()
Sд_entry = tk.Entry(window, state=tk.DISABLED)
Sд_entry.pack()

Sл_label = tk.Label(window, text="Sл - Площадь листа:")
Sл_label.pack()
Sл_entry = tk.Entry(window, state=tk.DISABLED)
Sл_entry.pack()

Sзак_label = tk.Label(window, text="Sзак - Площадь заказа:")
Sзак_label.pack()
Sзак_entry = tk.Entry(window, state=tk.DISABLED)
Sзак_entry.pack()

nл_label = tk.Label(window, text="nл - Количество листов:")
nл_label.pack()
nл_entry = tk.Entry(window, state=tk.DISABLED)
nл_entry.pack()

Sост_label = tk.Label(window, text="Sост - Площадь остатка:")
Sост_label.pack()
Sост_entry = tk.Entry(window, state=tk.DISABLED)
Sост_entry.pack()

# Кнопка "Рассчитать"
calculate_button = tk.Button(window, text="Рассчитать", command=calculate_coefficient)
calculate_button.pack()

# Для вывода результата
result_label = tk.Label(window, text="")
result_label.pack()

# Главный цикл
window.mainloop()


