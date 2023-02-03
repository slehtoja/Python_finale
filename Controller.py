from Model import Model
from View import View


class Controller:

    def __init__(self):
        self.model = Model()
        self.view = View(self, self.model)

    def main(self):
        self.view.main()

    def click_btn_name(self):
        self.view.btn_name['state'] = 'disabled'
        self.view.btn_task['state'] = 'normal'
        self.view.btn_shuffle['state'] = 'normal'
        self.view.btn_save['state'] = 'normal'
        self.view.btn_clear['state'] = 'normal'

    def click_btn_job(self):
        self.view.btn_name['state'] = 'normal'
        self.view.btn_task['state'] = 'disabled'
        self.view.btn_shuffle['state'] = 'normal'
        self.view.btn_save['state'] = 'normal'
        self.view.btn_clear['state'] = 'normal'

    def click_btn_shuffle(self):
        self.view.btn_name['state'] = 'normal'
        self.view.btn_task['state'] = 'normal'
        self.view.btn_shuffle['state'] = 'disabled'
        self.view.btn_save['state'] = 'normal'
        self.view.btn_clear['state'] = 'normal'

    def click_btn_save(self):
        self.view.btn_name['state'] = 'normal'
        self.view.btn_task['state'] = 'normal'
        self.view.btn_shuffle['state'] = 'normal'
        self.view.btn_save['state'] = 'disabled'
        self.view.btn_clear['state'] = 'normal'

    def click_btn_clear(self):
        self.view.btn_name['state'] = 'normal'
        self.view.btn_task['state'] = 'normal'
        self.view.btn_shuffle['state'] = 'normal'
        self.view.btn_save['state'] = 'normal'
        self.view.btn_clear['state'] = 'disabled'
