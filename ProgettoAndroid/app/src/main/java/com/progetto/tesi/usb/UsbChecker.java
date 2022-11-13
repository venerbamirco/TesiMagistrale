package com.progetto.tesi.usb;

import android.content.Intent;
import android.content.IntentFilter;

import androidx.appcompat.app.AppCompatActivity;

import com.progetto.tesi.debugger.detection.GnuDebugger_GDB;
import com.progetto.tesi.debugger.detection.JavaDebugWireProtocol_JDWP;

public class UsbChecker extends Thread {

    /*variable for the action battery changed*/
    private final IntentFilter ifilter = new IntentFilter ( Intent.ACTION_BATTERY_CHANGED );


    private final Intent batteryStatus = context.registerReceiver ( null , ifilter );

    /*variable for the reference of main activity*/
    private AppCompatActivity appCompatActivity;
    /*boolean variable to check if the device is charging*/
    private boolean deviceIsCharging;

    /*boolean variable to check if the device is transferring*/
    private boolean deviceIsTransferring;

    /*boolean variable to manage the stop button*/
    private boolean stopRecordingData;

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

        /*at the beginning the device is not charging*/
        this.deviceIsCharging = false;

        /*at the beginning the device is not transferring*/
        this.deviceIsTransferring = false;

        /*at the beginning we must record data*/
        this.stopRecordingData = false;

        /*save the references for the two debugger detection*/
        this.javaDebugWireProtocol_jdwp = javaDebugWireProtocol_jdwp;
        this.gnuDebugger_gdb = gnuDebugger_gdb;

    }

    @Override
    public void run ( ) {

        /*while a debugger is not found and the stop button is not pressed*/
        while ( ! this.javaDebugWireProtocol_jdwp.isFoundJdwpDebugger ( ) && ! this.gnuDebugger_gdb.isFoundGnuDebugger ( ) && ! this.stopRecordingData ) {

            /*we can check if there is */

        }

        /*stop recording data because or a debugger is found or the stop button is pressed*/

    }

    /*function used to set that the stop recording data button is pressed*/
    public void stopRecordingDataButtonPressed ( ) {

        /*stop recording data*/
        this.stopRecordingData = true;

    }

}
