package com.progetto.tesi.usb;

import android.content.Intent;
import android.content.IntentFilter;
import android.os.BatteryManager;
import android.os.Handler;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import com.progetto.tesi.debugger.detection.GnuDebugger_GDB;
import com.progetto.tesi.debugger.detection.JavaDebugWireProtocol_JDWP;

public class UsbChecker extends Thread {

    /*variable for the reference of main activity*/
    private AppCompatActivity appCompatActivity;

    /*variables for the action battery changes access*/
    private IntentFilter ifilter;
    private Intent batteryStatus;

    /*definition of useful variables for battery informations*/
    private int status;
    private int chargePlug;

    /*definitions of useful variables for all types of charging*/
    private boolean isCharging;
    private boolean usbCharge;
    private boolean acCharge;

    /*variables to store old values of all types of charging*/
    private boolean oldIsCharging;
    private boolean oldUsbCharge;
    private boolean oldAcCharge;

    /*variable for counter number of misurations*/
    private int misurations;

    /*variable to manage toast into thread*/
    private Handler handler;

    /*variables to manage debugger detection and if it is so, stop to collect data*/
    private JavaDebugWireProtocol_JDWP javaDebugWireProtocol_jdwp;
    private GnuDebugger_GDB gnuDebugger_gdb;

    public UsbChecker ( AppCompatActivity appCompatActivity , JavaDebugWireProtocol_JDWP javaDebugWireProtocol_jdwp , GnuDebugger_GDB gnuDebugger_gdb , Handler handler ) {

        /*initialize all necessary variables*/
        this.initializeAllVariables ( appCompatActivity , javaDebugWireProtocol_jdwp , gnuDebugger_gdb , handler );

        /*start the thread*/
        this.start ( );

    }

    /*function used to initialize all necessary variables*/
    private void initializeAllVariables ( AppCompatActivity appCompatActivity , JavaDebugWireProtocol_JDWP javaDebugWireProtocol_jdwp , GnuDebugger_GDB gnuDebugger_gdb , Handler handler ) {

        /*save the reference for the main activity*/
        this.appCompatActivity = appCompatActivity;

        /*access to action battery changes detection mechanism*/
        this.ifilter = new IntentFilter ( Intent.ACTION_BATTERY_CHANGED );
        this.batteryStatus = this.appCompatActivity.getApplicationContext ( ).registerReceiver ( new UsbReceiver () , ifilter );

        /*at the beginning 0 misurations*/
        this.misurations = 0;

        /*save the references for the two debugger detection*/
        this.javaDebugWireProtocol_jdwp = javaDebugWireProtocol_jdwp;
        this.gnuDebugger_gdb = gnuDebugger_gdb;

        /*save the reference of handler*/
        this.handler = handler;

    }

    @Override
    public void run ( ) {

        /*while a debugger is not found*/
        while ( ! this.javaDebugWireProtocol_jdwp.isFoundJdwpDebugger ( ) && ! this.gnuDebugger_gdb.isFoundGnuDebugger ( ) ) {



            /*save actual values in old variables*/
            this.oldAcCharge = this.acCharge;
            this.oldUsbCharge = this.usbCharge;
            this.oldIsCharging = this.isCharging;

            /*increment number of misurations of checks*/
            this.misurations++;

        }

        /*debugger found*/

    }

}
