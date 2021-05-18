# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tkinter import *
from tkinter import scrolledtext, filedialog

from os import getcwd

def main():
    window = Tk()
    window.title("Text analyzer")
    window.geometry('700x300')

    label = Label(window, text="Файлы")
    label.place(x=10, y=10)

    listbox = Listbox(window, width=40, height=10)
    listbox.place(x=10, y=40)

    add_file_button = Button(window, text="Добавить файл", command=lambda: add_file_button_clicked(listbox))
    add_file_button.place(x=270, y=40)

    delete_file_button = Button(window, text="Удалить файл", command=lambda: delete_file_button_clicked(listbox))
    delete_file_button.place(x=270, y=70)


    alg = IntVar()

    clust_x = 450
    Label(window, text="Кластеризация").place(x=clust_x, y=10)

    Radiobutton(window, text="ДБ scan", variable=alg, value=0).place(x=clust_x, y=40)
    Radiobutton(window, text="K means", variable=alg, value=1).place(x=clust_x, y=70)


    class_x = 570
    Label(window, text="Классификация").place(x=class_x, y=10)

    Radiobutton(window, text="K nearest neighbors", variable=alg, value=2).place(x=class_x, y=40)
    Radiobutton(window, text="Naive bayes", variable=alg, value=3).place(x=class_x, y=70)


    window.mainloop()

def add_file_button_clicked(listbox: Listbox):
    filename = filedialog.askopenfilename(initialdir=getcwd())
    listbox.insert(END, filename)

def delete_file_button_clicked(listbox: Listbox):
    index = listbox.curselection()
    if index != ():
        listbox.delete(index)
    
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

