from tkinter import filedialog

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
        print(names)

    def click_btn_task(self):
        task = filedialog.askopenfilename(filetypes=[("txt file", ".txt")])
        self.model.open_file_task(task)
        print(task)

    def click_btn_shuffle(self):
        self.view.btn_shuffle['state'] = 'disabled'

    def click_btn_save(self):
        self.view.btn_names['state'] = 'normal'
        self.view.btn_task['state'] = 'normal'
        self.view.btn_shuffle['state'] = 'normal'
        self.view.btn_save['state'] = 'disabled'
        self.view.btn_clear['state'] = 'normal'

    def click_btn_clear(self):
        self.view.btn_names['state'] = 'normal'
        self.view.btn_task['state'] = 'normal'
        self.view.btn_shuffle['state'] = 'normal'
        self.view.btn_save['state'] = 'normal'
        self.view.btn_clear['state'] = 'disabled'
