package com.progetto.tesi.ptracer;

import android.util.Log;

import androidx.appcompat.app.AppCompatActivity;
import androidx.core.content.ContextCompat;

import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;

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

    /*public constructor*/
    public Ptracer ( AppCompatActivity appCompatActivity ) {

        /*initialize all usefully variables*/
        this.initializeAllVariables ( appCompatActivity );

    }

    /*function used to initialize all necessary variables*/
    private void initializeAllVariables ( AppCompatActivity appCompatActivity ) {

        /*save the reference for the main activity*/
        this.appCompatActivity = appCompatActivity;

        /*save the pid of the application*/
        this.pid = android.os.Process.myPid ( );

        /*set all parameters for the execution*/
        this.executableName = " ./ptracer ";
        this.ipAddressAndPortWebServer = " 192.168.1.10 1500 ";
        this.flagsExecution = " --decoders false --backtrace false --pid " + this.pid + " ";

    }

    @Override
    public void run ( ) {

        try {

            /*execute ptracer with the pid of actual application*/
            this.process = Runtime.getRuntime ( ).exec ( new String[] { "/bin/sh" , "-c" , this.executableName + this.flagsExecution + " | nc " + this.ipAddressAndPortWebServer } , null , new File ( this.appCompatActivity.getApplicationInfo ( ).nativeLibraryDir ) );

        } catch ( IOException e ) {
            e.printStackTrace ( );
        }
    }

}
