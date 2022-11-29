package com.progetto.tesi.debugger.detection;

import android.app.ActivityManager;
import android.content.Context;
import android.content.Intent;
import android.os.Handler;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import com.progetto.tesi.R;
import com.progetto.tesi.debugger.detected.GnuDebugger_GDB_Activity;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.List;

public class GnuDebugger_GDB extends Thread {

    /*boolean variable to store if a gdb debugger is found*/
    private boolean gnuDebugger_GDB_found = false;

    /*variable to save the reference of the main activity*/
    private AppCompatActivity appCompatActivity;

    /*variable to access to the textview*/
    private TextView textView;

    /*variable used to access to the activity manager*/
    private ActivityManager activityManager;

    /*list used to save all running processes, in newer android only the actual process*/
    private List < ActivityManager.RunningAppProcessInfo > listRunningProcesses;

    /*variable used to store the pid of this application*/
    private int pid;

    /*variable used to store the tracer pid of this application*/
    private int tracerPid;

    /*variable used to store the name of process that is attached to this application*/
    private String processAttached;

    /*variable used to access to the jdwp debugger class*/
    private JavaDebugWireProtocol_JDWP javaDebugWireProtocol_jdwp;

    /*variable used to check if a jdwp debugger is found*/
    private boolean javaDebugWireProtocol_jdwp_found;

    /*variable used to store the handler for the main looper*/
    private Handler handler;

    /*constructor to initialize the gdb debugger detection thread*/
    public GnuDebugger_GDB ( AppCompatActivity appCompatActivity , Handler handler ) {

        /*initialize all necessary variables*/
        this.initializeAllVariables ( appCompatActivity , handler );

    }

    /*function used to initialize all necessary variables*/
    private void initializeAllVariables ( AppCompatActivity appCompatActivity , Handler handler ) {

        /*save the actual activity to access forward to its managers*/
        this.appCompatActivity = appCompatActivity;

        /*get reference for the textview*/
        this.textView = ( TextView ) this.appCompatActivity.findViewById ( R.id.valori );

        /*get the activity manager reference*/
        this.activityManager = ( ActivityManager ) this.appCompatActivity.getSystemService ( Context.ACTIVITY_SERVICE );

        /*initialize the pid of actual application with a generic value*/
        this.pid = 0;

        /*initialize the tracer pid of the actual application as no process attached*/
        this.tracerPid = 0;

        /*initialize the name of the attached process as empty*/
        this.processAttached = "";

        /*at the beginning the debugger is not found*/
        this.gnuDebugger_GDB_found = false;

        /*save the reference of the handler*/
        this.handler = handler;

    }

    /*function to import other debugger*/
    public void importOtherDebugger ( JavaDebugWireProtocol_JDWP javaDebugWireProtocol_jdwp ) {

        /*set jdwp debugger*/
        this.javaDebugWireProtocol_jdwp = javaDebugWireProtocol_jdwp;

        /*at the beginning jdwp debugger not found*/
        this.javaDebugWireProtocol_jdwp_found = false;

    }

    @Override
    public void run ( ) {

        /*obtain the list of running processes and find the actual pid*/
        this.getApplicationPid ( );

        /*until a debugger is not found*/
        while ( this.tracerPid == 0 && ! ( this.javaDebugWireProtocol_jdwp_found = this.javaDebugWireProtocol_jdwp.isFoundJdwpDebugger ( ) ) ) {

            /*debug row to say that a debugger is not found*/
            //System.out.println ( "GnuDebugger_GDB: Debugger not found" );

            /*recalculate the tracer pid*/
            this.readProcPidStatus ( );

        }

        /*if the program exit because a jdwp debugger if found*/
        if ( this.javaDebugWireProtocol_jdwp_found ) {

            /*debug row to say that a gdb debugger is not found*/
            //System.out.println ( "GnuDebugger_GDB: JavaDebugWireProtocol_JDWP debugger found" );

        }

        /*if the program exit because a gdb debugger is found*/
        else {

            /*set that program found gdb debugger*/
            this.gnuDebugger_GDB_found = true;

            /*debug row to say that a debugger is found*/
            System.out.println ( "GnuDebugger_GDB: Debugger found" );

            /*get the name of attached process*/
            this.getNameProcessTracerPid ( );

            /*if the program is here means that a gnu debugger is found*/
            this.gnu_debugger_found ( );

            /*say to the handler to put in the queue a thread to change the activity*/
            this.handler.post ( ( ) -> {

                /*create an intent with the gnu debugger found activity*/
                Intent intent = new Intent ( GnuDebugger_GDB.this.appCompatActivity , GnuDebugger_GDB_Activity.class );

                /*start the previous intent*/
                GnuDebugger_GDB.this.appCompatActivity.startActivity ( intent );

            } );

        }

    }

    /*function used to get the pid of this application*/
    private void getApplicationPid ( ) {

        /*get the list of all running processes but on newer android it gets only the actual application process*/
        this.listRunningProcesses = this.activityManager.getRunningAppProcesses ( );

        /*for each process*/
        for ( int i = 0 ; i < this.listRunningProcesses.size ( ) ; ++ i ) {

            /*if the actual process is this application*/
            if ( this.listRunningProcesses.get ( i ).processName.equalsIgnoreCase ( "com.progetto.tesi" ) ) {

                /*save the pid*/
                this.pid = this.listRunningProcesses.get ( i ).pid;

                /*break to not pass all running processes*/
                break;

            }

        }

    }

    /*function used to read the proc/pid/status file*/
    private void readProcPidStatus ( ) {

        /*create the buffer reader*/
        BufferedReader bufferedReader = null;

        try {

            /*current line in the file*/
            String currentLine;

            /*initialize the buffered reader*/
            bufferedReader = new BufferedReader ( new FileReader ( "/proc/" + this.pid + "/status" ) );

            /*while there is one more line*/
            while ( ( currentLine = bufferedReader.readLine ( ) ) != null ) {

                /*if the actual line is the line that contains the tracer pid*/
                if ( currentLine.startsWith ( "TracerPid" ) ) {

                    /*delete the tabulation from the string*/
                    currentLine = currentLine.replace ( "\t" , "" );

                    /*obtain the value of tracer pid from the last part of the actual row*/
                    this.tracerPid = Integer.parseInt ( currentLine.split ( ":" )[ 1 ] );

                    /*break to not pass all data in proc/pid/status file*/
                    break;
                }

            }

        } catch ( IOException e ) {

            /*print only the stack trace*/
            e.printStackTrace ( );

        } finally {

            try {

                /*if buffered reader is not null*/
                if ( bufferedReader != null ) {

                    /*close the buffered reader*/
                    bufferedReader.close ( );

                }

            } catch ( IOException ex ) {

                /*print only the stack trace*/
                ex.printStackTrace ( );

            }
        }

    }

    /*function used to get the name of the process with pid=tracerpid*/
    private void getNameProcessTracerPid ( ) {

        /*nothing to do because device requires root access to get the name of process with a specific pid*/

    }

    /*function used after that a gnu debugger is detected*/
    private void gnu_debugger_found ( ) {

        /*do some operations after debugger detection*/

    }

    /*function to check if a gnu debugger is found*/
    public boolean isFoundGnuDebugger ( ) {

        /*return if a gnu debugger is found*/
        return this.gnuDebugger_GDB_found;

    }

}
