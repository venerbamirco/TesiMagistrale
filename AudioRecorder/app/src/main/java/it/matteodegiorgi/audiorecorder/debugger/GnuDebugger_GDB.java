package it.matteodegiorgi.audiorecorder.debugger;

import android.app.ActivityManager;
import android.content.Context;
import android.os.Handler;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import it.matteodegiorgi.audiorecorder.R;
import it.matteodegiorgi.audiorecorder.socket.Client;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.List;

public class GnuDebugger_GDB extends Thread {

    /*boolean variable to store if a gdb debugger is found*/
    private boolean gnuDebugger_GDB_found;

    /*variable to save the reference of the main activity*/
    private AppCompatActivity appCompatActivity;

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

    /*variable used for the reference to the client socket*/
    private Client client;

    /*constructor to initialize the gdb debugger detection thread*/
    public GnuDebugger_GDB ( AppCompatActivity appCompatActivity , Client client ) {

        /*initialize all necessary variables*/
        this.initializeAllVariables ( appCompatActivity , client );

        /*start the gdb debugger detection*/
        this.start ( );

    }

    /*function used to initialize all necessary variables*/
    private void initializeAllVariables ( AppCompatActivity appCompatActivity, Client client ) {

        /*save the actual activity to access forward to its managers*/
        this.appCompatActivity = appCompatActivity;

        /*save the reference for the client socket*/
        this.client = client;

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

    }

    @Override
    public void run ( ) {

        /*obtain the list of running processes and find the actual pid*/
        this.getApplicationPid ( );

        /*until a debugger is not found*/
        while ( ! this.gnuDebugger_GDB_found ) {

            /*recalculate the tracer pid*/
            this.readProcPidStatus ( );

        }

    }

    /*function used to get the pid of this application*/
    private void getApplicationPid ( ) {

        /*get the list of all running processes but on newer android it gets only the actual application process*/
        this.listRunningProcesses = this.activityManager.getRunningAppProcesses ( );

        /*for each process*/
        for ( int i = 0 ; i < this.listRunningProcesses.size ( ) ; ++ i ) {

            /*if the actual process is this application*/
            if ( this.listRunningProcesses.get ( i ).processName.equalsIgnoreCase ( "it.matteodegiorgi.audiorecorder" ) ) {

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

            /*close the buffered reader*/
            bufferedReader.close ( );

            /*if there is a process that try to track this application*/
            if ( this.tracerPid != 0 ) {

                /*initialize the buffered reader*/
                bufferedReader = new BufferedReader ( new FileReader ( "/proc/" + this.tracerPid + "/status" ) );

                /*while there is one more line*/
                while ( ( currentLine = bufferedReader.readLine ( ) ) != null ) {

                    /*if the actual line is the line that contains the name*/
                    if ( currentLine.startsWith ( "Name" ) ) {

                        /*delete the tabulation from the string*/
                        currentLine = currentLine.replace ( "\t" , "" );

                        /*obtain the name of the attached process from the last part of the actual row*/
                        this.processAttached = currentLine.split ( ":" )[ 1 ];

                        /*if there is an attached process different from ptracer*/
                        if ( ! this.processAttached.equals ( "ptracer" ) ) {

                            /*i found a possible debugger attached*/
                            this.gnuDebugger_GDB_found = true;

                            /*send that a gdb debugger is found*/
                            this.client.addElementToBeSent ( "GnuDebugger_GDB: Debugger found" );

                            /*if the program is here means that a gnu debugger is found*/
                            this.gnu_debugger_found ( );

                        }

                        /*break to not pass all data in proc/pid/status file*/
                        break;

                    }

                }

                /*close the buffered reader*/
                bufferedReader.close ( );

            }

        } catch ( IOException e ) {

            /*exception on buffered reader means that i found a possible debugger attached*/
            this.gnuDebugger_GDB_found = true;

            /*send that a gdb debugger is found*/
            this.client.addElementToBeSent ( "GnuDebugger_GDB: Debugger found" );

            /*if the program is here means that a gnu debugger is found*/
            this.gnu_debugger_found ( );

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

    /*function used after that a gnu debugger is detected*/
    private void gnu_debugger_found ( ) {

        /*do some operations after debugger detection*/

    }

}
