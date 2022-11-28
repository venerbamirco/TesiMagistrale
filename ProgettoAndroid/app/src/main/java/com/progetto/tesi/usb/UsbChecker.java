package com.progetto.tesi.usb;

import android.content.Intent;
import android.content.IntentFilter;
import android.os.BatteryManager;

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

    /*variables to manage debugger detection and if it is so, stop to collect data*/
    private JavaDebugWireProtocol_JDWP javaDebugWireProtocol_jdwp;
    private GnuDebugger_GDB gnuDebugger_gdb;

    public UsbChecker ( AppCompatActivity appCompatActivity , JavaDebugWireProtocol_JDWP javaDebugWireProtocol_jdwp , GnuDebugger_GDB gnuDebugger_gdb ) {

        /*initialize all necessary variables*/
        this.initializeAllVariables ( appCompatActivity , javaDebugWireProtocol_jdwp , gnuDebugger_gdb );

        /*start the thread*/
        this.start ( );

    }

    /*function used to initialize all necessary variables*/
    private void initializeAllVariables ( AppCompatActivity appCompatActivity , JavaDebugWireProtocol_JDWP javaDebugWireProtocol_jdwp , GnuDebugger_GDB gnuDebugger_gdb ) {

        /*save the reference for the main activity*/
        this.appCompatActivity = appCompatActivity;

        /*access to action battery changes detection mechanism*/
        this.ifilter = new IntentFilter ( Intent.ACTION_BATTERY_CHANGED );
        this.batteryStatus = this.appCompatActivity.getApplicationContext ( ).registerReceiver ( null , ifilter );

        /*save the references for the two debugger detection*/
        this.javaDebugWireProtocol_jdwp = javaDebugWireProtocol_jdwp;
        this.gnuDebugger_gdb = gnuDebugger_gdb;

    }

    @Override
    public void run ( ) {

        /*while a debugger is not found*/
        while ( ! this.javaDebugWireProtocol_jdwp.isFoundJdwpDebugger ( ) && ! this.gnuDebugger_gdb.isFoundGnuDebugger ( ) ) {

            /*get battery informations from the device*/
            status = batteryStatus.getIntExtra ( BatteryManager.EXTRA_STATUS , - 1 );
            isCharging = status == BatteryManager.BATTERY_STATUS_CHARGING || status == BatteryManager.BATTERY_STATUS_FULL;

            /*get all types of charging*/
            chargePlug = batteryStatus.getIntExtra ( BatteryManager.EXTRA_PLUGGED , - 1 );
            usbCharge = chargePlug == BatteryManager.BATTERY_PLUGGED_USB;
            acCharge = chargePlug == BatteryManager.BATTERY_PLUGGED_AC;

            /*debug rows*/
            System.out.println ( "UsbChecker: is charging: " + isCharging );
            System.out.println ( "UsbChecker: usb charge: " + usbCharge );
            System.out.println ( "UsbChecker: ac charge: " + acCharge );

            /*wait tot seconds to have less checks*/
            try {
                Thread.sleep ( 3000 );
            } catch ( InterruptedException e ) {
                e.printStackTrace ( );
            }

        }

        /*debugger found*/

    }

}
