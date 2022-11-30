package com.progetto.tesi.developeroptions.detection;

import android.provider.Settings;

import androidx.appcompat.app.AppCompatActivity;

import com.progetto.tesi.debugger.detection.GnuDebugger_GDB;
import com.progetto.tesi.debugger.detection.JavaDebugWireProtocol_JDWP;

public class DeveloperOptions extends Thread {

    /*variable for the reference for the appcompat activity*/
    private AppCompatActivity appCompatActivity;

    /*variables to store if the adb and developer options are enabled*/
    private boolean adbActivated;
    private boolean developerOptionsActivated;

    /*old variables to store if the adb and developer options are enabled*/
    private boolean oldAdbActivated;
    private boolean oldDeveloperOptionsActivated;

    /*variable used to store the number of misurations*/
    private int misurations;

    /*variables to manage debugger detection and if it is so, stop to check*/
    private JavaDebugWireProtocol_JDWP javaDebugWireProtocol_jdwp;
    private GnuDebugger_GDB gnuDebugger_gdb;

    /*constructor to initialize the developer option detection mechanism*/
    public DeveloperOptions ( AppCompatActivity appCompatActivity , JavaDebugWireProtocol_JDWP javaDebugWireProtocol_jdwp , GnuDebugger_GDB gnuDebugger_gdb ) {

        /*initialize all necessary variables*/
        this.initializeAllNecessaryVariables ( appCompatActivity , javaDebugWireProtocol_jdwp , gnuDebugger_gdb );

        /*start actual thread*/
        this.start ( );

    }

    /*function to initialize all necessary variables*/
    private void initializeAllNecessaryVariables ( AppCompatActivity appCompatActivity , JavaDebugWireProtocol_JDWP javaDebugWireProtocol_jdwp , GnuDebugger_GDB gnuDebugger_gdb ) {

        /*save the reference for the main activity*/
        this.appCompatActivity = appCompatActivity;

        /*at beginning number of misurations equal to 0*/
        this.misurations = 0;

        /*get the references of the two types of debuggers*/
        this.javaDebugWireProtocol_jdwp = javaDebugWireProtocol_jdwp;
        this.gnuDebugger_gdb = gnuDebugger_gdb;

    }

    @Override
    public void run ( ) {

        /*until a debugger is not found*/
        while ( ! this.javaDebugWireProtocol_jdwp.isFoundJdwpDebugger ( ) && ! this.gnuDebugger_gdb.isFoundGnuDebugger ( ) ) {

            /*get actual values for adb and developer options if they are activated*/
            try {
                this.adbActivated = Settings.Global.getInt ( this.appCompatActivity.getApplicationContext ( ).getContentResolver ( ) , Settings.Global.ADB_ENABLED ) > 0;
                this.developerOptionsActivated = Settings.Global.getInt ( this.appCompatActivity.getApplicationContext ( ).getContentResolver ( ) , Settings.Global.DEVELOPMENT_SETTINGS_ENABLED ) > 0;
            } catch ( Settings.SettingNotFoundException e ) {
                e.printStackTrace ( );
            }

            /*if first misuration*/
            if ( this.misurations == 0 ) {

                /*print all informations*/
                this.printAllDetails ( );

            }

            /*if not the first misuration*/
            else {

                /*print only if there is at least one change*/
                if ( this.oldAdbActivated != this.adbActivated || this.oldDeveloperOptionsActivated != this.developerOptionsActivated ) {

                    /*print all informations*/
                    this.printAllDetails ( );

                }

            }

            /*save actual misurations*/
            this.saveActualValues ( );

            /*increment number of misurations*/
            this.misurations++;

        }

        /*a debugger is found*/

    }

    /*function used to print all details*/
    private void printAllDetails ( ) {

        /*debug row*/
        System.out.println ( "DeveloperOptions: adb: " + this.adbActivated + " devops: " + this.developerOptionsActivated );

    }

    /*function used to save actual values*/
    private void saveActualValues ( ) {

        /*save actual variables in old variables of adb and developer options activated*/
        this.oldAdbActivated = this.adbActivated;
        this.oldDeveloperOptionsActivated = this.developerOptionsActivated;

    }


}
