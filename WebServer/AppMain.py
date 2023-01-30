from threading import Thread

from file.file import File
from settings.settings import Settings
from tcpSocket.android import Android
from tcpSocket.ptracer import Ptracer

# main method to start the web server
if __name__ == "__main__" :
    #
    # create the object for settings to get all constant values
    settings = Settings ( )
    #
    # create and open the file for the ptracer logs
    ptracerLogs = File ( settings.getPtracerLogs ( ) , settings.howToOpenFiles )
    #
    # create and open the file for the android logs
    androidLogs = File ( settings.getAndroidLogs ( ) , settings.howToOpenFiles )
    #
    # create the ptracer tcpSocket
    ptracerSocket = Ptracer ( "ptracer" , settings.hostname , settings.portSocketPtracer , settings.maximumNumberConnectedClients , ptracerLogs , settings )
    #
    # create the android tcpSocket
    androidSocket = Android ( "android" , settings.hostname , settings.portSocketAndroid , settings.maximumNumberConnectedClients , androidLogs , settings )
    #
    # create and start a thread to manage ptracer socket
    threadPtracer = Thread ( target = ptracerSocket.createConfigureStartSocket )
    threadPtracer.start ( )
    #
    # create and start a thread to manage android socket
    threadAndroid = Thread ( target = androidSocket.createConfigureStartSocket )
    threadAndroid.start ( )
