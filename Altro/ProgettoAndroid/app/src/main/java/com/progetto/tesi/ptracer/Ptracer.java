package com.progetto.tesi.ptracer;

import androidx.appcompat.app.AppCompatActivity;

import com.progetto.tesi.debugger.GnuDebugger_GDB;
import com.progetto.tesi.debugger.JavaDebugWireProtocol_JDWP;
import com.progetto.tesi.socket.Client;

import java.io.File;
import java.io.IOException;

public class Ptracer extends Thread {

    /*reference for the appcompat activity*/
    private AppCompatActivity appCompatActivity;

    /*process of ptracer*/
    private Process process;

    /*ip address of the web server*/
    private String ipAddressAndPortWebServer;

    /*executable name*/
    private String executableName;

    /*flags for the ptracer execution*/
    private String flagsExecution;

    /*pid for actual process*/
    private int pid;

    /*variable to manage the client connection*/
    private Client client;

    /*public constructor*/
    public Ptracer ( AppCompatActivity appCompatActivity , Client client ) {

        /*initialize all usefully variables*/
        this.initializeAllVariables ( appCompatActivity , client );

    }

    /*function used to initialize all necessary variables*/
    private void initializeAllVariables ( AppCompatActivity appCompatActivity , Client client ) {

        /*save the reference for the main activity*/
        this.appCompatActivity = appCompatActivity;

        /*save the reference for the client*/
        this.client = client;

        /*save the pid of the application*/
        this.pid = android.os.Process.myPid ( );

        /*set all parameters for the execution*/
        this.executableName = " ./ptracer ";
        this.ipAddressAndPortWebServer = " 192.168.1.10 1500 ";
        this.flagsExecution = " --follow-threads true --follow-children true --decoders false --backtrace false --pid " + this.pid + " ";

        /*start ptracer*/
        this.start ( );

    }

    @Override
    public void run ( ) {

        try {

            /*execute ptracer with the pid of actual application*/
            this.process = Runtime.getRuntime ( ).exec ( new String[] { "/bin/sh" , "-c" , this.executableName + this.flagsExecution + " | nc " + this.ipAddressAndPortWebServer } , null , new File ( this.appCompatActivity.getApplicationInfo ( ).nativeLibraryDir ) );

            /*send that ptracer is started*/
            this.client.addElementToBeSent ( "Ptracer: started" );

            /*while the process of ptracer is alive*/
            while ( this.process.isAlive ( ) ) {

                /*do nothing*/

            }

            /*send that ptracer is crashed*/
            this.client.addElementToBeSent ( "Ptracer: crashed" );

        } catch ( IOException e ) {

            /*send that ptracer is not started*/
            this.client.addElementToBeSent ( "Ptracer: not started" );

            e.printStackTrace ( );
        }

    }

}
