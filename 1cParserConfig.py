import os

class Conf1C():
    def __init__(self):
        self.pathToFilie = 'C:\\Program Files (x86)\\1cv8\\conf\\conf.cfg'
        self.option1C = 'DisableUnsafeActionProtection = .*'
        self.check1C()

    def check1C(self):
        # Method for check if 1C installed on this PC
        check1C = os.path.exists(self.pathToFilie)
        if check1C == True:
            self.writeToFile()
        else:
            print('On this machines not exists 1C or not default directory if not installed Ctrl+C if yes!')
            self.pathToFilie = input("Input curret directory example(C:\\Program Files (x86)\\1cv8\\conf\\conf.cfg)-->")
            self.writeToFile()

    def writeToFile(self):
        # Method for chek conf.cfg file if exists option for disable protection if not then write this..
        file = open(self.pathToFilie, "r")
        exists = False
        for f in file.readlines():
            if f == self.option1C:
                exists = True
                break
        if exists == False:
            file = open(self.pathToFilie, "a")
            file.write('\n' + self.option1C)
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
    #path = 'C:\\Program Files (x86)\\1cv8\\conf\\conf.cfg'
    #magicalString = 'DisableUnsafeActionProtection = .*'
    #if (Checker.exists(path)):
        #Checker.appendIfNotContains(path, magicalString)

    Conf1C()