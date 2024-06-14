#Разработать программу с применением пакета tk, взяв в качестве условия одну
#любую задачу из ПЗ № 2 – 9.
#Известно, что x кг шоколадных конфет стоит a рублей, а y кг ирисок стоит b рублей.
#Определить сколько стоит 1 кг шоколадных конфет, 1 кг ирисок, а также во сколько раз шоколадные конфеты дороже ирисок
import tkinter as tk
def calculate_price():
    x = float(entry_x.get())
    a = float(entry_a.get())
    y = float(entry_y.get())
    b = float(entry_b.get())

    price_choco_kg = a / x
    price_iris_per_kg = b / y
    price_ratio = price_choco_kg / price_iris_per_kg

    result_label.config(text=f"Цена за 1 кг шоколадных конфет: {price_choco_kg:.2f} рублей\n"
                             f"Цена за 1 кг ирисок: {price_iris_per_kg:.2f} рублей\n"
                             f"Шоколадные конфеты дороже ирисок в {price_ratio:.2f} раз(а)")

root = tk.Tk()
root.title("Расчет цен на шоколадные конфеты и ириски")
tk.Label(root, text="Введите, пожалуйста, сколько x-кг шоколадных конфет:").pack()
entry_x = tk.Entry(root)
entry_x.pack()

tk.Label(root, text="Введите, пожалуйста, цену a за них:").pack()
entry_a = tk.Entry(root)
entry_a.pack()

tk.Label(root, text="Введите, пожалуйста, сколько y-кг ирисок:").pack()
entry_y = tk.Entry(root)
entry_y.pack()

tk.Label(root, text="Введите, пожалуйста, цену b за них:").pack()
entry_b = tk.Entry(root)
entry_b.pack()

calculate_button = tk.Button(root, text="Рассчитать", command=calculate_price)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()