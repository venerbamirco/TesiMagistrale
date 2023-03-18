package com.progetto.training.recharge;

import android.content.Intent;
import android.content.IntentFilter;
import android.os.Handler;

import androidx.appcompat.app.AppCompatActivity;

import com.progetto.training.debugger.GnuDebugger_GDB;
import com.progetto.training.debugger.JavaDebugWireProtocol_JDWP;
import com.progetto.training.socket.Client;

public class RechargeDetection {

    /*variable for the reference of main activity*/
    private AppCompatActivity appCompatActivity;

    /*variables for the action battery changes access*/
    private IntentFilter ifilter;

    /*variable for recharge receiver*/
    private RechargeReceiver rechargeReceiver;

    public RechargeDetection ( AppCompatActivity appCompatActivity , Client client ) {

        /*initialize all necessary variables*/
        this.initializeAllVariables ( appCompatActivity , client );

    }

    /*function used to initialize all necessary variables*/
    private void initializeAllVariables ( AppCompatActivity appCompatActivity , Client client ) {

        /*save the reference for the main activity*/
        this.appCompatActivity = appCompatActivity;

        /*initialize the recharge receiver*/
        this.rechargeReceiver = new RechargeReceiver ( client );

        /*access to action battery changes detection mechanism*/
        this.ifilter = new IntentFilter ( Intent.ACTION_BATTERY_CHANGED );

        /*register the listener*/
        this.registerListener ( );

    }

    /*function used to unregister the listener*/
    public void unregisterListener ( ) {

        /*unregister the recharge receiver*/
        this.appCompatActivity.getApplicationContext ( ).unregisterReceiver ( this.rechargeReceiver );

    }

    /*function used to register the listener*/
    public void registerListener ( ) {

        /*unregister the recharge receiver*/
        this.appCompatActivity.getApplicationContext ( ).registerReceiver ( this.rechargeReceiver , this.ifilter );

    }

}
