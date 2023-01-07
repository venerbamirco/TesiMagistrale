from threading import Thread, Lock

from manageFile.manageFile import ManageFile
from manageSocket.androidLogs import AndroidLogs
from manageSocket.ptracerLogs import PtracerLogs
from settings.settings import Settings

lock = Lock()

# class to manage the log of the web server
class MainClass:
    
    # constructor for this class
    def __init__(self):
        self.__thread1 = Thread(target=self.__threadOne)
        self.__thread2 = Thread(target=self.__threadTwo)
        self.__thread1.start()
        self.__thread2.start()
    
    def __print(self, val):
        lock.acquire()
        print("Thread " + str(val))
        lock.release()
    
    def __threadOne(self):
        while 1:
            self.__print(1)
    
    def __threadTwo(self):
        while 1:
            self.__print(2)

# main method to start the web server
if __name__ == "__main__":
    #
    # create the object to manage the web server
    # mc = MainClass()
    
    # create the object for settings to get all constant values
    settings = Settings()
    
    # manage the file for the ptracer logs
    ptracerLogs = ManageFile(settings.getPtracerLogs(), settings.getHowToOpenFiles())
    # open the file
    ptracerLogs.openFile()
    
    # manage the file for the android logs
    androidLogs = ManageFile(settings.getAndroidLogs(), settings.getHowToOpenFiles())
    # open the file
    androidLogs.openFile()
    
    # create the ptracer socket
    ptracerSocket = PtracerLogs("ptracer", settings.getHostname(), settings.getPtracerPort(), settings.getMaxNumberConnectedClients(), ptracerLogs, settings)
    
    # create the android socket
    androidSocket = AndroidLogs("android", settings.getHostname(), settings.getAndroidPort(), settings.getMaxNumberConnectedClients(), androidLogs, settings)
    
    # create and start a thread to manage ptracer logs
    threadPtracer = Thread(target=ptracerSocket.createConfigureStartSocket)
    threadPtracer.start()
    
    # create and start a thread to manage android logs
    threadAndroid = Thread(target=androidSocket.createConfigureStartSocket)
    threadAndroid.start()
