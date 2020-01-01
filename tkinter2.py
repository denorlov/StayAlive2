import tkinter as tk

while True:
    s = input("Введите имя картинки (от 1 до 3):")

    # главное и единственное окно, на котором будет расположена canvas
    root = tk.Tk()

    # загружаем разные картинки в зависимости от того, что ввел пользователь
    if s == "1":
        img = tk.PhotoImage(file="map_кабинет_директора.gif")
    elif s == "2":
        img = tk.PhotoImage(file="map_камера_содержания.gif")
    elif s == "3":
        img = tk.PhotoImage(file="map_комната_с_другом.gif")
    else:
        continue

    # канва (холст) на которой будет рисовать картинку
    canvas = tk.Canvas(root)
    # выставляем размеры холста равными размерам загруженной картинки
    canvas.configure(width=img.width(), height=img.height())
    canvas.create_image((0, 0), image=img, anchor='nw', )
    # размещаем холст на главном окне
    canvas.pack()

    # выставляем атрибуты отрисовки нашего окна так, чтобы он отображлся поверх остальных окон
    root.call('wm', 'attributes', '.', '-topmost', '1')

    # запускаем отрисовку всех элементов нашего оконного интрефейса
    root.mainloop()

    print("После показа карты")