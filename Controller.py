from tkinter import filedialog, INSERT

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
        self.model.open_file_names(names)
        # print(names)
        if len(self.model.names) > 0:
            for names in self.model.names:
                self.view.textbox_names.insert(INSERT, names + '\n')

    def click_btn_task(self):
        task = filedialog.askopenfilename(filetypes=[("txt file", ".txt")])
        self.model.open_file_task(task)
        # print(task)
        if len(self.model.task) > 0:
            for task in self.model.task:
                self.view.textbox_task.insert(INSERT, task + '\n')

    def click_btn_shuffle(self):
        self.view.btn_shuffle['state'] = 'disabled'

    def click_btn_save(self):
        self.view.btn_save['state'] = 'disabled'

    def click_btn_clear(self):
        self.view.btn_clear['state'] = 'disabled'
