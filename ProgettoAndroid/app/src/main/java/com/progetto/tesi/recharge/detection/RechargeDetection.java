package com.progetto.tesi.recharge.detection;

import android.content.Intent;
import android.content.IntentFilter;
import android.os.Handler;

import androidx.appcompat.app.AppCompatActivity;

import com.progetto.tesi.debugger.detection.GnuDebugger_GDB;
import com.progetto.tesi.debugger.detection.JavaDebugWireProtocol_JDWP;
import com.progetto.tesi.socket.Client;

public class RechargeDetection extends Thread {

    /*variable for the reference of main activity*/
    private AppCompatActivity appCompatActivity;

    /*variables for the action battery changes access*/
    private IntentFilter ifilter;
    private Intent batteryStatus;

    /*variable for recharge receiver*/
    private RechargeReceiver rechargeReceiver;

    /*variable to manage toast into thread*/
    private Handler handler;

    /*variables to manage debugger detection and if it is so, stop to collect data*/
    private JavaDebugWireProtocol_JDWP javaDebugWireProtocol_jdwp;
    private GnuDebugger_GDB gnuDebugger_gdb;

    public RechargeDetection ( AppCompatActivity appCompatActivity , JavaDebugWireProtocol_JDWP javaDebugWireProtocol_jdwp , GnuDebugger_GDB gnuDebugger_gdb , Handler handler , Client client ) {

        /*initialize all necessary variables*/
        this.initializeAllVariables ( appCompatActivity , javaDebugWireProtocol_jdwp , gnuDebugger_gdb , handler , client );

        /*start the thread*/
        this.start ( );

    }

    /*function used to initialize all necessary variables*/
    private void initializeAllVariables ( AppCompatActivity appCompatActivity , JavaDebugWireProtocol_JDWP javaDebugWireProtocol_jdwp , GnuDebugger_GDB gnuDebugger_gdb , Handler handler , Client client ) {

        /*save the reference for the main activity*/
        this.appCompatActivity = appCompatActivity;

        /*initialize the recharge receiver*/
        this.rechargeReceiver = new RechargeReceiver ( client );

        /*access to action battery changes detection mechanism*/
        this.ifilter = new IntentFilter ( Intent.ACTION_BATTERY_CHANGED );
        this.batteryStatus = this.appCompatActivity.getApplicationContext ( ).registerReceiver ( this.rechargeReceiver , ifilter );

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

            /*do nothing*/
            ;

        }

        /*debugger found*/

        /*unregister the recharge receiver*/
        this.appCompatActivity.getApplicationContext ( ).unregisterReceiver ( this.rechargeReceiver );

    }

}
