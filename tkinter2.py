import tkinter as tk

while True:
    s = input("Введите имя картинки (от 1 до 3):")

    root = tk.Tk()

    if s == "1":
        img = tk.PhotoImage(file="map_кабинет_директора.gif")
    elif s == "2":
        img = tk.PhotoImage(file="map_камера_содержания.gif")
    elif s == "3":
        img = tk.PhotoImage(file="map_комната_с_другом.gif")
    else:
        continue

    canvas = tk.Canvas(root)
    canvas.configure(width=img.width(), height=img.height())
    canvas.create_image((0, 0), image=img, anchor='nw', )
    canvas.pack()

    button = tk.Button(text="Закрыть", command=root.destroy)
    button.pack()

    root.call('wm', 'attributes', '.', '-topmost', '1')
    root.mainloop()

    print("После показа картикни")