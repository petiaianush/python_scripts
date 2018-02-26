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


if __name__ == '__main__':
    Conf1C()