#Модуль, содержащий описание интерфейса приложения

import tkinter as tk, FormDataClass as fdc, math, datetime as dt, SnowMeltLogic as sml
from tkinter import filedialog as fd
from tkinter.ttk import Checkbutton
from tkinter.messagebox import showinfo

def heightClicked(): #обработчик для checkbox-a "Высота"
    forestCoefEntry.configure(state = "normal" if heightChk_state.get() else "disabled")
    fieldCoefEntry.configure(state = "normal" if heightChk_state.get() else "disabled")

def expClicked(): #обработчик для checkbox-a "Экспозиция"
    southEntry.configure(state = "normal" if expChk_state.get() else "disabled")
    westEntry.configure(state = "normal" if expChk_state.get() else "disabled")
    eastEntry.configure(state = "normal" if expChk_state.get() else "disabled")
    northEntry.configure(state = "normal" if expChk_state.get() else "disabled")
    plainEntry.configure(state = "normal" if expChk_state.get() else "disabled")

def forestClicked(): #обработчик для checkbox-a "Изменить водный эквивалент снега для леса"
    snowForestDefEntry.set("2")
    snowForestCoefEntry.configure(state = "normal" if snowForestChk_state.get() else "disabled")

def fieldClicked(): #обработчик для checkbox-a "Изменить водный эквивалент снега для поля"
    snowFieldDefEntry.set("5")
    snowFieldCoefEntry.configure(state = "normal" if snowFieldChk_state.get() else "disabled")

def pickFile(): #обработчик для кнопки "Выбрать файл"
    filetypes = [('Файлы DBF', '*.dbf')]
    filename = fd.askopenfilename(title = "Выберите файл", initialdir = "/", filetypes = filetypes)
    pathLbl.configure(text = filename if filename != "" else "Файл с данными о точках не выбран")

def parseEntry(elem, message): #преобразование строки в вещественное число
    try:
        res = float(elem.get().replace(",", ".")) #замена запятой на точку и преобразование к вещественному числу
        return res
    except: #преобразовать не удалось => было введено не число, сообщаем об этом
        showinfo(title = "Ошибка в параметрах", message = message)
        return float('NaN')

def parseDt(elem, isstart, message): #преобразование строки в datetime
    try:
        res = dt.datetime.strptime(elem.get(), "%d.%m.%Y") #попытка чтения в формате дд.мм.гггг
        return res
    except:
        try:
            res = dt.datetime.strptime(elem.get(), "%Y") #попытка чтения в формате гггг
            #установка даты 1 января, если читаем начало промежутка, иначе - 31 декабря
            if isstart: res = res.replace(month = 1, day = 1)
            else: res = res.replace(month = 12, day = 31)
            return res
        except: #была введена не дата - сообщаем об этом
            showinfo(title = "Ошибка в параметрах", message = message)
            return None

def run(): #обработчик для кнопки "Расчет"
    #чтение и проверка временного промежутка
    startTime = parseDt(startEntry, True, "Неверный формат для начала временного промежутка")
    endTime = parseDt(endEntry, False, "Неверный формат для конца временного промежутка")
    if startTime is None or endTime is None: return
    if startTime > endTime:
        showinfo(title = "Ошибка в параметрах", message = 
                 "Начало временного промежутка не может наступить позже, чем его конец")
        return

    #чтение и проверка порога высоты и коэффициентов водного эквивалента снега
    heightTh = parseEntry(heightEntry, "В качестве порога высоты введено не число")
    wEqField = parseEntry(snowFieldDefEntry, "В качестве водного эквивалента снега для поля введено не число")
    wEqForest = parseEntry(snowForestDefEntry, "В качестве водного эквивалента снега для леса введено не число")
    if math.isnan(heightTh) or math.isnan(wEqField) or math.isnan(wEqForest): return

    if not heightChk_state.get(): #если высота не учитывается, высотные коэффициенты имеют значения по умолчанию
        forestCoef = 0
        fieldCoef = 0
    else: #иначе - проверка этих коэффициентов
        forestCoef = parseEntry(forestCoefEntry, "В качестве высотного коэффициента для леса введено не число")
        fieldCoef = parseEntry(fieldCoefEntry, "В качестве высотного коэффициента для поля введено не число")
        if math.isnan(forestCoef) or math.isnan(fieldCoef): return
    
    if not expChk_state.get(): #если экспозиция не учитывается, экспозиционные коэффициенты имеют значения по умолчанию
        sCoef = 0
        nCoef = 0
        wCoef = 0
        eCoef =  0
        pCoef = 0
    else: #иначе - проверка этих коэффициентов
        sCoef = parseEntry(southEntry, "В качестве экспозиционного коэффициента для юга введено не число")
        nCoef = parseEntry(northEntry, "В качестве экспозиционного коэффициента для севера введено не число")
        wCoef = parseEntry(westEntry, "В качестве экспозиционного коэффициента для запада введено не число")
        eCoef = parseEntry(eastEntry, "В качестве экспозиционного коэффициента для востока введено не число")
        pCoef = parseEntry(plainEntry, "В качестве экспозиционного коэффициента для равнины введено не число")
        if math.isnan(sCoef) or math.isnan(nCoef) or math.isnan(wCoef) or math.isnan(eCoef) or math.isnan(pCoef): return

    #запуск расчетов
    data = fdc.FormData(pathLbl.cget("text"), startTime, endTime, heightTh, heightChk_state.get(), expChk_state.get(),
                       wEqField, wEqForest, forestCoef, fieldCoef, sCoef, nCoef, wCoef, eCoef, pCoef)
    sml.run(data)

form = tk.Tk() #создание окна
#параметры окна
form.title("Расчет снеготаяния")
form.minsize(400, 400)
form.resizable(False, False)

#временной промежуток, для которого ведутся расчеты
startLbl = tk.Label(form, text = "Период с")
startLbl.grid(column = 0, row = 0, sticky = "W")
startEntry = tk.Entry(form)
startEntry.grid(column = 1, row = 0, padx = 10)
endLbl = tk.Label(form, text = "по")
endLbl.grid(column = 2, row = 0)
endEntry = tk.Entry(form)
endEntry.grid(column = 3, row = 0, padx = 10)

#порог высоты
heightLbl = tk.Label(form, text = "Порог высоты")
heightLbl.grid(column = 0, row = 1, pady = 10, sticky = "W")
heightEntry = tk.Entry(form, width = 10)
heightEntry.grid(column = 1, row = 1)

#высота
heightChk_state = tk.BooleanVar()
heightChk_state.set(True)
heightChk = Checkbutton(form, text = "Высота", var = heightChk_state, command = heightClicked)
heightChk.grid(column = 0, row = 3, pady = 10, sticky = "W")
forestCoefLbl = tk.Label(form, text = "Коэф. для леса")
forestCoefLbl.grid(column = 1, row = 3)
forestCoefEntry = tk.Entry(form, width = 10)
forestCoefEntry.grid(column = 2, row = 3)
fieldCoefLbl = tk.Label(form, text = "Коэф. для поля")
fieldCoefLbl.grid(column = 1, row = 4)
fieldCoefEntry = tk.Entry(form, width = 10)
fieldCoefEntry.grid(column = 2, row = 4)

#экспозиция
expChk_state = tk.BooleanVar()
expChk_state.set(True)
expChk = Checkbutton(form, text = "Экспозиция", var = expChk_state, command = expClicked)
expChk.grid(column = 0, row = 5, pady = 10, sticky = "W")
southLbl = tk.Label(form, text = "Юг")
southLbl.grid(column = 1, row = 5)
southEntry = tk.Entry(form, width = 10)
southEntry.grid(column = 2, row = 5)
westLbl = tk.Label(form, text = "Запад")
westLbl.grid(column = 1, row = 6)
westEntry = tk.Entry(form, width = 10)
westEntry.grid(column = 2, row = 6)
northLbl = tk.Label(form, text = "Север")
northLbl.grid(column = 1, row = 7, pady = 10)
northEntry = tk.Entry(form, width = 10)
northEntry.grid(column = 2, row = 7)
eastLbl = tk.Label(form, text = "Восток")
eastLbl.grid(column = 1, row = 8)
eastEntry = tk.Entry(form, width = 10)
eastEntry.grid(column = 2, row = 8)
plainLbl = tk.Label(form, text = "Равнина")
plainLbl.grid(column = 1, row = 9, pady = 10)
plainEntry = tk.Entry(form, width = 10)
plainEntry.grid(column = 2, row = 9)

#коэффициенты водного эквивалента снега
snowForestChk_state = tk.BooleanVar()
snowForestChk_state.set(True)
snowForestChk = Checkbutton(form, text = "Изменить водный эквивалент снега для леса", var = snowForestChk_state,
                            command = forestClicked)
snowForestChk.grid(column = 0, row = 10, sticky = "W")
snowForestDefEntry = tk.StringVar()
snowForestDefEntry.set("2")
snowForestCoefEntry = tk.Entry(form, width = 10, textvariable = snowForestDefEntry)
snowForestCoefEntry.grid(column = 2, row = 10)
snowFieldChk_state = tk.BooleanVar()
snowFieldChk_state.set(True)
snowFieldChk = Checkbutton(form, text = "Изменить водный эквивалент снега для поля", var = snowFieldChk_state,
                           command = fieldClicked)
snowFieldChk.grid(column = 0, row = 11, pady = 10, sticky = "W")
snowFieldDefEntry = tk.StringVar()
snowFieldDefEntry.set("5")
snowFieldCoefEntry = tk.Entry(form, width = 10, textvariable = snowFieldDefEntry)
snowFieldCoefEntry.grid(column = 2, row = 11)

#путь к файлу с данными о точках
pathLbl = tk.Label(form, text = "Файл с данными о точках не выбран")
pathLbl.grid(column = 0, row = 12, sticky = "W")

#выбор файла и начало расчетов
fileBtn = tk.Button(form, text = "Выбрать файл", width = 20, command = pickFile)
fileBtn.grid(column = 0, row = 13, padx = 20, pady = 10)
runBtn = tk.Button(form, text = "Расчет", width = 20, command = run)
runBtn.grid(column = 1, row = 13)

#отображение окна и запуск приложения
form.mainloop()
