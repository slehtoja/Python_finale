

class Model:

    def __init__(self):
        self.names = []
        self.task = []
        self.shuffle = []

    def open_file_names(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            all_lines = f.readlines()
            for line in all_lines:
                self.names.append(line)
            # print(self.names)

    def open_file_task(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            all_lines = f.readlines()
            for line in all_lines:
                self.task.append(line)
            # print(self.task)



