"""from threading import Thread

from algorithm.manager.manager import Manager
from dataStructure.other.file import File
from dataStructure.tcpSocket.android import Android
from dataStructure.tcpSocket.ptracer import Ptracer
from settings.settings import Setting"""
from algorithm.training.recover import Recover

# main method to start the web server
if __name__ == "__main__" :
    #
    # object used to load all training data
    recover: Recover = Recover ( )
    
    """#
    # create the object for settings to get all constant values
    settings = Settings ( )
    #
    # create the manager algorithm
    managerAlgorithm = Manager ( settings )
    #
    # create and open the other for the ptracer logs
    ptracerLogs = File ( settings.getPtracerLogs ( ) , settings.howToOpenFiles )
    #
    # create and open the other for the android logs
    androidLogs = File ( settings.getAndroidLogs ( ) , settings.howToOpenFiles )
    #
    # create the ptracer tcpSocket
    ptracerSocket = Ptracer ( "ptracer" , settings.hostname , settings.portSocketPtracer , settings.maximumNumberConnectedClients , ptracerLogs , settings , managerAlgorithm )
    #
    # create the android tcpSocket
    androidSocket = Android ( "android" , settings.hostname , settings.portSocketAndroid , settings.maximumNumberConnectedClients , androidLogs , settings , managerAlgorithm )
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
    managerAlgorithm.saveLogsEachManager ( )"""
