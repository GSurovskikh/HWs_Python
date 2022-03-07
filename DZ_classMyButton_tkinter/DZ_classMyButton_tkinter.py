import tkinter as tk


def start_demo():
    root = tk.Tk()
    root.mainloop()
class MyButton(tk.Tk):#Непонятно как наследоваться от Tk.Button
    def __init__(self, *args, **kwargs):
        super(MyButton, self).__init__(*args, **kwargs)
        self.add_btn = tk.Button(self, text="Мой класс - MyButton")
        self.add_btn.pack()
    def run(self):
        self.mainloop()


if __name__ == '__main__':
    Button = MyButton()
    Button.run()


