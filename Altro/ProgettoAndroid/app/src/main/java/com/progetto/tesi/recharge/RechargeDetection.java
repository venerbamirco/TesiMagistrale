package com.progetto.tesi.recharge;

import android.content.Intent;
import android.content.IntentFilter;
import android.os.Handler;

import androidx.appcompat.app.AppCompatActivity;

import com.progetto.tesi.debugger.GnuDebugger_GDB;
import com.progetto.tesi.debugger.JavaDebugWireProtocol_JDWP;
import com.progetto.tesi.socket.Client;

public class RechargeDetection {

    /*variable for the reference of main activity*/
    private AppCompatActivity appCompatActivity;

    /*variables for the action battery changes access*/
    private IntentFilter ifilter;
    private Intent batteryStatus;

    /*variable for recharge receiver*/
    private RechargeReceiver rechargeReceiver;

    /*variable to manage toast into thread*/
    private Handler handler;

    public RechargeDetection ( AppCompatActivity appCompatActivity , Handler handler , Client client ) {

        /*initialize all necessary variables*/
        this.initializeAllVariables ( appCompatActivity , handler , client );

    }

    /*function used to initialize all necessary variables*/
    private void initializeAllVariables ( AppCompatActivity appCompatActivity , Handler handler , Client client ) {

        /*save the reference for the main activity*/
        this.appCompatActivity = appCompatActivity;

        /*initialize the recharge receiver*/
        this.rechargeReceiver = new RechargeReceiver ( client );

        /*access to action battery changes detection mechanism*/
        this.ifilter = new IntentFilter ( Intent.ACTION_BATTERY_CHANGED );
        this.batteryStatus = this.appCompatActivity.getApplicationContext ( ).registerReceiver ( this.rechargeReceiver , this.ifilter );

        /*save the reference of handler*/
        this.handler = handler;

    }

    public void unregisterListener ( ) {

        /*unregister the recharge receiver*/
        this.appCompatActivity.getApplicationContext ( ).unregisterReceiver ( this.rechargeReceiver );

    }

    public void registerListener ( ) {

        /*unregister the recharge receiver*/
        this.appCompatActivity.getApplicationContext ( ).registerReceiver ( this.rechargeReceiver , this.ifilter );

    }

}
