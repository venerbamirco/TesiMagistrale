package com.progetto.tesi.ptracer;

import androidx.appcompat.app.AppCompatActivity;
import androidx.core.content.ContextCompat;

import com.progetto.tesi.socket.Client;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

public class Ptracer extends Thread {

    /*reference for the appcompat activity*/
    private AppCompatActivity appCompatActivity;

    /*process of ptracer*/
    private Process process;

    /*executable name*/
    private String executableName;

    /*flags for the ptracer execution*/
    private String flagsExecution;

    /*pid for actual process*/
    private int pid;

    /*variable to manage the client connection of android*/
    private Client clientAndroid;

    /*variable to manage the client connection of ptracer*/
    private Client clientPtracer;

    /*public constructor*/
    public Ptracer ( AppCompatActivity appCompatActivity , Client clientAndroid , Client clientPtracer ) {

        /*initialize all usefully variables*/
        this.initializeAllVariables ( appCompatActivity , clientAndroid , clientPtracer );

    }

    /*function used to initialize all necessary variables*/
    private void initializeAllVariables ( AppCompatActivity appCompatActivity , Client clientAndroid , Client clientPtracer ) {

        /*save the reference for the main activity*/
        this.appCompatActivity = appCompatActivity;

        /*save the reference for the client of android*/
        this.clientAndroid = clientAndroid;

        /*save the reference for the client of ptracer*/
        this.clientPtracer = clientPtracer;

        /*save the pid of the application*/
        this.pid = android.os.Process.myPid ( );

        /*set all parameters for the execution*/
        this.executableName = " ./ptracer ";
        this.flagsExecution = " --follow-threads true --follow-children true --decoders false --backtrace false --pid " + this.pid + " ";

        /*start ptracer*/
        this.start ( );

    }

    @Override
    public void run ( ) {

        /*try to do the following*/
        try {

            /*create the file for ptracer logs*/
            File output = new File ( ContextCompat.getExternalFilesDirs ( this.appCompatActivity.getApplicationContext ( ) , "ptracer" )[ 0 ] , "/traces.txt" );

            /*execute the process of ptracer redirecting the output to the previous file*/
            this.process = Runtime.getRuntime ( ).exec ( new String[] { "/bin/sh" , "-c" , this.executableName + this.flagsExecution + " &>" + output.getAbsolutePath ( ) } , null , new File ( this.appCompatActivity.getApplicationInfo ( ).nativeLibraryDir ) );

            /*send that ptracer is started*/
            this.clientAndroid.addElementToBeSent ( "Ptracer: #started#" );

            /*create the stream to read from the previous file*/
            BufferedReader objReader = new BufferedReader ( new FileReader ( output ) );

            /*create a temporary string*/
            String strCurrentLine = "";

            /*while true*/
            while ( true ) {

                /*read actual line*/
                strCurrentLine = objReader.readLine ( );

                /*if it is a valid string*/
                if ( strCurrentLine != null ) {

                    System.out.println (strCurrentLine );

                    /*if not found ptracer*/
                    if ( strCurrentLine.contains ( "inaccessible" ) ) {

                        /*send that ptracer is not started*/
                        this.clientAndroid.addElementToBeSent ( "Ptracer: #error#" );

                        /*exit from the loop*/
                        break;

                    }

                    /*if actual string is valid*/
                    if ( this.filterPtracerLogs ( strCurrentLine ) ) {

                        /*send to the server the actual string*/
                        this.clientPtracer.sendDataToServer ( strCurrentLine + "\n" );
                    }

                }

            }

        } catch ( IOException e ) {

            /*send that ptracer is not started*/
            this.clientAndroid.addElementToBeSent ( "Ptracer: #error#" );

        }

    }

    /*function used to filter ptracer logs*/
    private boolean filterPtracerLogs ( String string ) {

        /*if the actual string is valid*/
        if ( string.contains ( "PID:" ) || string.contains ( "SPID:" ) || string.contains ( "Timestamp:" ) || string.contains ( "Syscall =" ) || string.contains ( "Return value:" ) || string.contains ( "------------------" ) ) {

            /*return that is a valid string*/
            return true;

        }

        /*otherwise return that is not a valid string*/
        return false;

    }

}