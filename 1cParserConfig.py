import os

class Conf1C():
    def __init__(self):
        Conf1C.check1C(self)


    def check1C(self):
        self.pathToFilie = 'C:\\Program Files (x86)\\1cv8\\conf\\conf.cfg'
        check1C = os.path.exists(self.pathToFilie)
        if check1C == True:
            print('We have a work')
            Conf1C.writeToFile(self)
        else:
            print('On this machines not exist 1C')

    def writeToFile(self):
        file = open(self.pathToFilie, "r")
        find = 'DisableUnsafeActionProtection = .*'
        exist = 0
        print('reading -->', file)
        for f in file.readlines():
            print(f)
            if f == find:
                exist = 1
                break
            else:
                print('we need make some changes')
        if exist == 0:
            file = open(self.pathToFilie, "a")
            file.write('\nDisableUnsafeActionProtection = .*')
        file.close()



class Checker:
    @staticmethod
    def exists(path):
        return os.path.exists(path)

    @staticmethod
    def appendIfNotContains(path, content):
        fd = open(path, "r")
        lines = fd.readlines()
        contains = True
        try:
            lines.index(content)
        except ValueError:
            contains = False

        if (not contains):
            fd = open(path, "a")
            fd.write(content)
        fd.close()

if __name__ == '__main__':
    path = 'C:\\Program Files (x86)\\1cv8\\conf\\conf.cfg'
    magicalString = 'DisableUnsafeActionProtection = .*'
    if (Checker.exists(path)):
        Checker.appendIfNotContains(path, magicalString)

#    Conf1C()