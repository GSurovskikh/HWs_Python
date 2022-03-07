import  tkinter as tk

def start():
    window = tk.Tk()
    lbl = tk.Label(window,text="Введите имя")
    lbl.grid(columnspan=3,row=0)
    entry1 = tk.Entry(window)
    entry1.grid(column=1,row=1)

    window.mainloop()

if __name__ == '__main__':
    app = start()
