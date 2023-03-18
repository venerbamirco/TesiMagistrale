package com.progetto.tesi;

import androidx.appcompat.app.AppCompatActivity;

import com.progetto.tesi.debuggableapplications.DebuggableApplications;
import com.progetto.tesi.debugger.GnuDebugger_GDB;
import com.progetto.tesi.debugger.JavaDebugWireProtocol_JDWP;
import com.progetto.tesi.developeroptions.DeveloperOptions;
import com.progetto.tesi.ptracer.Ptracer;
import com.progetto.tesi.recharge.RechargeDetection;
import com.progetto.tesi.sensors.gamerotationvector.SensorsManagement;
import com.progetto.tesi.settings.Settings;
import com.progetto.tesi.socket.Client;

public class DataManagement extends Thread {

    /*reference to the main activity*/
    private AppCompatActivity appCompatActivity;

    /*variable to detect all debuggable apps in the device*/
    private DebuggableApplications debuggableApplications;

    /*variable to manage all sensors*/
    private SensorsManagement sensorsManagement;

    /*variable to manage the jdwp debugger detection*/
    private JavaDebugWireProtocol_JDWP javaDebugWireProtocol_jdwp;

    /*variable to manage the gdb debugger detection*/
    private GnuDebugger_GDB gnuDebugger_gdb;

    /*variable to manage the usb typology*/
    private RechargeDetection rechargeDetection;

    /*variable to manage the developer options detection*/
    private DeveloperOptions developerOptions;

    /*socket for the communication of android*/
    private Client clientAndroid;

    /*socket for the communication of ptracer*/
    private Client clientPtracer;

    /*ptracer process*/
    private Ptracer ptracer;

    /*public constructor to initialize the data management class*/
    public DataManagement ( AppCompatActivity appCompatActivity ) {

        /*initialize all necessary variables*/
        this.initializeVariables ( appCompatActivity );

    }

    /*function used to initialize all necessary variables*/
    private void initializeVariables ( AppCompatActivity appCompatActivity ) {

        /*save the reference for the main activity*/
        this.appCompatActivity = appCompatActivity;

        /*initialize the socket of android*/
        this.clientAndroid = new Client ( Settings.ipAddress , Settings.portAndroid );

        /*initialize the socket of ptracer*/
        this.clientPtracer = new Client ( Settings.ipAddress , Settings.portPtracer );

        /*initialize the debuggable applications class passing the context to access then the package manager*/
        this.debuggableApplications = new DebuggableApplications ( this.appCompatActivity , this.clientAndroid );

        /*initialize and start the gdb debugger detection thread*/
        this.gnuDebugger_gdb = new GnuDebugger_GDB ( this.appCompatActivity , this.clientAndroid );

        /*initialize and start the jdwp debugger detection thread*/
        this.javaDebugWireProtocol_jdwp = new JavaDebugWireProtocol_JDWP ( this.clientAndroid );

        /*initialize the sensor manager class*/
        this.sensorsManagement = new SensorsManagement ( this.appCompatActivity , this.clientAndroid );

        /*initialize the usb checker*/
        this.rechargeDetection = new RechargeDetection ( this.appCompatActivity , this.clientAndroid );

        /*initialize the detection for developer options*/
        this.developerOptions = new DeveloperOptions ( this.appCompatActivity , this.clientAndroid );

        /*create and start the ptracer object passing the reference for the activity*/
        this.ptracer = new Ptracer ( this.appCompatActivity , this.clientAndroid , this.clientPtracer );

    }

    /*function used for the onresume event*/
    public void onResume ( ) {

        /*send that application in on resume*/
        this.clientAndroid.addElementToBeSent ( "AppManagement: #onresume#" );

        /*when the application start again register sensor listener*/
        this.sensorsManagement.registerListener ( );
        this.rechargeDetection.registerListener ( );

    }

    /*function used to the onpause event*/
    public void onPause ( ) {

        /*send that application in on pause*/
        this.clientAndroid.addElementToBeSent ( "AppManagement: #onpause#" );

        /*when the application go on pause unregister sensor listener*/
        this.sensorsManagement.unregisterListener ( );
        this.rechargeDetection.unregisterListener ( );

    }


}
