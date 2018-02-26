import platform
import getpass
import time

class MyWork():
    def main():
        myhost = platform.uname()
        myName = getpass.getuser()
        today = time.clock()
        myNameConverted = " ".join([n.capitalize() for n in myName.split('.')])


        print(today)
        print("Dear" , myNameConverted, "Hello Work go to start on Your PC -->", myhost.node)


    if __name__ == '__main__':
        main()
