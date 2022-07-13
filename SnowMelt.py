import tkinter as tk
from tkinter.ttk import Checkbutton

class Form(tk.Tk):
    def __init__(self):
        super(Form, self).__init__()

        #параметры окна
        self.title("Расчет снеготаяния")
        self.minsize(400, 400) #оставить, но подкорректировать цифры
        self.resizable(False, False)

        #временной промежуток, для которого ведутся расчеты
        startLbl = tk.Label(self, text = "Период с")
        startLbl.grid(column = 0, row = 0, sticky = "W")
        startEntry = tk.Entry(self)
        startEntry.grid(column = 1, row = 0, padx = 10)
        endLbl = tk.Label(self, text = "по")
        endLbl.grid(column = 2, row = 0)
        endEntry = tk.Entry(self)
        endEntry.grid(column = 3, row = 0, padx = 10)

        # порог высоты
        heightLbl = tk.Label(self, text = "Порог высоты")
        heightLbl.grid(column = 0, row = 1, pady = 10, sticky = "W")
        heightEntry = tk.Entry(self, width = 10)
        heightEntry.grid(column = 1, row = 1)

        #высота
        heightChk_state = tk.BooleanVar()
        heightChk_state.set(True)
        heightChk = Checkbutton(self, text = "Высота", var = heightChk_state)
        heightChk.grid(column = 0, row = 3, pady = 10, sticky = "W")
        forestCoefLbl = tk.Label(self, text = "Коэф. для леса")
        forestCoefLbl.grid(column = 1, row = 3)
        forestCoefEntry = tk.Entry(self, width = 10)
        forestCoefEntry.grid(column = 2, row = 3)
        fieldCoefLbl = tk.Label(self, text = "Коэф. для поля")
        fieldCoefLbl.grid(column = 1, row = 4)
        fieldCoefEntry = tk.Entry(self, width = 10)
        fieldCoefEntry.grid(column = 2, row = 4)

        #экспозиция
        expChk_state = tk.BooleanVar()
        expChk_state.set(True)
        expChk = Checkbutton(self, text = "Экспозиция", var = expChk_state)
        expChk.grid(column = 0, row = 5, pady = 10, sticky = "W")
        southLbl = tk.Label(self, text = "Юг")
        southLbl.grid(column = 1, row = 5)
        southEntry = tk.Entry(self, width = 10)
        southEntry.grid(column = 2, row = 5)
        westLbl = tk.Label(self, text = "Запад")
        westLbl.grid(column = 1, row = 6)
        westEntry = tk.Entry(self, width = 10)
        westEntry.grid(column = 2, row = 6)
        northLbl = tk.Label(self, text = "Север")
        northLbl.grid(column = 1, row = 7, pady = 10)
        northEntry = tk.Entry(self, width = 10)
        northEntry.grid(column = 2, row = 7)
        eastLbl = tk.Label(self, text = "Восток")
        eastLbl.grid(column = 1, row = 8)
        eastEntry = tk.Entry(self, width = 10)
        eastEntry.grid(column = 2, row = 8)
        plainLbl = tk.Label(self, text = "Равнина")
        plainLbl.grid(column = 1, row = 9, pady = 10)
        plainEntry = tk.Entry(self, width = 10)
        plainEntry.grid(column = 2, row = 9)

        #доп комбики для коэффициентов (row 10 и 11)
        snowChk_state = tk.BooleanVar()
        snowChk_state.set(True)
        snowChk = Checkbutton(self, text = "Водный эквивалент снега", var = heightChk_state)
        snowChk.grid(column = 0, row = 10, sticky = "W")
        snowForestCoefLbl = tk.Label(self, text = "для леса")
        snowForestCoefLbl.grid(column = 1, row = 10)
        snowForestCoefEntry = tk.Entry(self, width = 10)
        snowForestCoefEntry.grid(column = 2, row = 10)
        snowFieldCoefLbl = tk.Label(self, text = "для поля")
        snowFieldCoefLbl.grid(column = 1, row = 11, pady = 10)
        snowFieldCoefEntry = tk.Entry(self, width = 10)
        snowFieldCoefEntry.grid(column = 2, row = 11)

        #путь к файлу с данными о точках
        pathLbl = tk.Label(self, text = "Путь к файлу с данными о точках: ")
        pathLbl.grid(column = 0, row = 12, sticky = "W")

        #выбор файла и начало расчетов
        fileBtn = tk.Button(self, text = "Выбрать файл", width = 20)
        fileBtn.grid(column = 0, row = 13, padx = 20, pady = 10)
        runBtn = tk.Button(self, text = "Расчет", width = 20)
        runBtn.grid(column = 1, row = 13)

form = Form()
form.mainloop()
