from threading import Thread

from algorithm.dataStructure.other.file import File
from algorithm.manager.manager import Manager
from algorithm.settings.settings import Settings
from algorithm.tcpSocket.android import Android
from algorithm.tcpSocket.ptracer import Ptracer

# main method to start the web server
if __name__ == "__main__" :
    #
    # create settings obj
    settings: Settings = Settings ( )
    #
    # create the manager algorithm
    managerAlgorithm = Manager ( )
    #
    # create and open the other for the ptracer yeslogs
    ptracerLogs = File ( settings.getPtracerLogs ( ) , Settings.howToOpenFiles )
    #
    # create and open the other for the android logs
    androidLogs = File ( settings.getAndroidLogs ( ) , Settings.howToOpenFiles )
    #
    # create the ptracer tcpSocket
    ptracerSocket = Ptracer ( "ptracer" , Settings.hostname , Settings.portSocketPtracer , Settings.maximumNumberConnectedClients , ptracerLogs , managerAlgorithm )
    #
    # create the android tcpSocket
    androidSocket = Android ( "android" , Settings.hostname , Settings.portSocketAndroid , Settings.maximumNumberConnectedClients , androidLogs , managerAlgorithm )
    #
    # create and start a thread to manage ptracer socket
    threadPtracer = Thread ( target = ptracerSocket.createConfigureStartSocket )
    threadPtracer.start ( )
    #
    # create and start a thread to manage android socket
    threadAndroid = Thread ( target = androidSocket.createConfigureStartSocket )
    threadAndroid.start ( )
    #
    # save all the logs structure
    managerAlgorithm.saveLogsEachManager ( )
