import os.path
from tkinter import filedialog, INSERT
from tkinter import messagebox as mes


from Model import Model
from View import View


class Controller:

    def __init__(self):
        self.model = Model()
        self.view = View(self, self.model)

    def main(self):
        self.view.main()

    def click_btn_names(self):
        names = filedialog.askopenfilename(filetypes=[("txt file", ".txt")])
        self.view.textbox_names.delete('1.0', 'end')
        if names != '':
            self.model.open_file_names(names)
            if len(self.model.names) > 0:
                for names in self.model.names:
                    self.view.textbox_names.insert(INSERT, names + '\n')
            else:
                mes.showerror('Error', 'Fail on tühi!')


    def click_btn_task(self):
        task = filedialog.askopenfilename(filetypes=[("txt file", ".txt")])
        self.view.textbox_task.delete('1.0', 'end')
        if task != '':
            self.model.open_file_task(task)
            if len(self.model.task) > 0:
                for task in self.model.task:
                    self.view.textbox_task.insert(INSERT, task + '\n')
            else:
                mes.showerror('Error', 'Fail on tühi!')

    def click_btn_shuffle(self):
        if len(self.model.names) > len(self.model.task):
            mes.showerror('Error', 'List on liiga lühike!')
        else:
            self.view.textbox_shuffle.delete('1.0', 'end')
            self.model.shuffle_list()
            x = 0
            for name in self.model.names:
                self.view.textbox_shuffle.insert(INSERT, name + ' - ' + self.model.task[x] + '\n')
                self.model.shuffle.append(name + " - " + self.model.task[x])
                x += 1

    def click_btn_save(self):
        if len(self.model.shuffle) != 0:
            shuffle = filedialog.asksaveasfilename(
                filetypes=[("txt file", ".txt")],
                defaultextension=".txt",
                initialdir='D:\\my_data\\my_html\\')
            # print(shuffle)
            if shuffle != '':
                """ File exists"""
                with open(shuffle, "a", encoding="utf-8") as f:
                    for save in self.model.shuffle:
                        f.write(save + "\n")

    def click_btn_clear(self):
        self.view.textbox_names.delete('1.0', 'end')
        self.view.textbox_task.delete('1.0', 'end')
        self.view.textbox_shuffle.delete('1.0', 'end')

