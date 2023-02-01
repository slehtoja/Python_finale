from tkinter import *


class View(Tk):

    def __init__(self, controller, model):
        super().__init__()
        self.default_style = None
        self.controller = controller
        self.model = model

        # Window properties
        self.geometry('600x400')
        self.title('Python Finale')
        self.center(self)

        # Create three frames
        self.frame_top, self.frame_bottom = self.create_two_frames()

        # Create all buttons
        self.btn_name, self.btn_task, self.btn_shuffle, self.btn_save, self.btn_clear = self.create_all_buttons()

    def main(self):
        self.mainloop()

    @staticmethod
    def center(win):
        """
        https://stackoverflow.com/questions/3352918/
        centers a tkinter window
        :param win: the main window or Toplevel window to center
        """
        win.update_idletasks()
        width = win.winfo_width()
        frm_width = win.winfo_rootx() - win.winfo_x()
        win_width = width + 2 * frm_width
        height = win.winfo_height()
        titlebar_height = win.winfo_rooty() - win.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = win.winfo_screenwidth() // 2 - win_width // 2
        y = win.winfo_screenheight() // 2 - win_height // 2
        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        win.deiconify()

    def create_two_frames(self):
        frame_top = Frame(self, bg='#0096FF', height=50)  # blue
        frame_bottom = Frame(self)  # yellow

        frame_top.pack(fill='both')
        frame_bottom.pack(expand=True, fill='both')

        return frame_top, frame_bottom  # method return two objects

    def create_all_buttons(self):
        # Create button name
        btn_name = Button(self.frame_top, text='Name', font=self.default_style,
                          command=self.controller.click_btn_name)
        # Create button job
        btn_task = Button(self.frame_top, text='Task', font=self.default_style,
                          command=self.controller.click_btn_job)
        # Create button shuffle
        btn_shuffle = Button(self.frame_top, text='Shuffle', font=self.default_style,
                             command=self.controller.click_btn_shuffle)
        # Create button save
        btn_save = Button(self.frame_top, text='Save', font=self.default_style,
                          command=self.controller.click_btn_save)
        # Create button clear
        btn_clear = Button(self.frame_top, text='clear', font=self.default_style,
                          command=self.controller.click_btn_clear)

        btn_name.grid(row=0, column=0, padx=5, pady=2, sticky=EW)
        btn_task.grid(row=0, column=2, padx=5, pady=2, sticky=EW)
        btn_shuffle.grid(row=0, column=4, padx=5, pady=2, sticky=EW)
        btn_save.grid(row=0, column=6, padx=5, pady=2, sticky=EW)
        btn_clear.grid(row=0, column=8, padx=5, pady=2, sticky=EW)

        return btn_name, btn_task, btn_shuffle, btn_save, btn_clear
