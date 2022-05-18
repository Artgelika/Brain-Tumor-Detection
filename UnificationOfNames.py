import os
import Paths

path_yes = Paths.dataset_yes
path_no = Paths.dataset_no

folder_no = os.listdir(path_no)
folder_yes = os.listdir(path_yes)


class ChangeNames:
    def __init__(self, path, filename, letterOfType):
        self.path = path
        self.filename = filename
        self.letterOfType = letterOfType

    def rename(self):
        try:
            os.rename(os.path.join(self.path, self.filename),
                      os.path.join(self.path, str(self.letterOfType) + str(next(iterator)) + ".png"))
        except:
            pass


order = [x for x in range(1, len(folder_no)+1)]
iterator = iter(order)

for filename in folder_no:
    ChangeNames(path_no, filename, "N").rename()

order2 = [x for x in range(1, len(folder_yes)+1)]
iterator = iter(order2)

for filename in folder_yes:
    ChangeNames(path_yes, filename, "Y").rename()
