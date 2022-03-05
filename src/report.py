
class Report(object):
    def __init__(self):
        self.content = ""

    def write_file(self, file_name):
        f = open(file_name, "w")
        f.write(self.content)
        f.close()

