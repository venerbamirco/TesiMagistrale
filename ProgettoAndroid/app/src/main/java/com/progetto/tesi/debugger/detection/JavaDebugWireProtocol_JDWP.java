package com.progetto.tesi.debugger.detection;

import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import com.progetto.tesi.R;

public class JavaDebugWireProtocol_JDWP extends Thread {

    /*boolean variable to store if a jdwp debugger is found*/
    private boolean javaDebugWireProtocol_jdwp_found = false;

    /*variable used to access to the gnu debugger class*/
    private GnuDebugger_GDB gnuDebugger_gdb;

    /*variable used to check if a gnu debugger is found*/
    private boolean gnuDebugger_gdb_found;

    /*variable to save the reference of the main activity*/
    private AppCompatActivity appCompatActivity;

    /*variable to access to the textview*/
    private TextView textView;

    /*constructor to initialize and start the jdwp debugger detection thread*/
    public JavaDebugWireProtocol_JDWP ( AppCompatActivity appCompatActivity ) {

        /*initialize all necessary variables*/
        this.initializeAllVariables ( appCompatActivity );

    }

    /*function used to initialize all necessary variables*/
    private void initializeAllVariables ( AppCompatActivity appCompatActivity ) {

        /*save the actual activity*/
        this.appCompatActivity = appCompatActivity;

        /*get reference for the textview*/
        this.textView = ( TextView ) this.appCompatActivity.findViewById ( R.id.valori );

        /*at the beginning the debugger is not found*/
        this.javaDebugWireProtocol_jdwp_found = false;

    }

    /*function to import other debugger*/
    public void importOtherDebugger ( GnuDebugger_GDB gnuDebugger_gdb ) {

        /*set gnu debugger*/
        this.gnuDebugger_gdb = gnuDebugger_gdb;

        /*at the beginning gnu debugger not found*/
        this.gnuDebugger_gdb_found = false;

    }

    @Override
    public void run ( ) {

        /*until a debugger is not found*/
        while ( ! this.javaDebugWireProtocol_jdwp_found && ! ( this.gnuDebugger_gdb_found = this.gnuDebugger_gdb.isFoundGnuDebugger ( ) ) ) {

            /*debug row to say that a debugger is not found*/
            System.out.println ( "JavaDebugWireProtocol_JDWP: Debugger not found" );

            /*look if a debugger is attached*/
            this.javaDebugWireProtocol_jdwp_found = android.os.Debug.isDebuggerConnected ( );

        }

        /*if the program exit because a gnu debugger if found*/
        if ( this.gnuDebugger_gdb_found ) {

            /*debug row to say that a jdwp debugger is not found*/
            System.out.println ( "JavaDebugWireProtocol_JDWP: Debugger not found" );

        }

        /*if the program exit because a jdwp debugger is found*/
        else {

            /*set that program found jdwp debugger*/
            this.javaDebugWireProtocol_jdwp_found = true;

            /*set to the textview that a gnu debugger if found*/
            this.textView.setText ( "\n\nJava debug wire protocol (JDWP) debugger found" );

            /*debug row to say that a debugger is found*/
            System.out.println ( "JavaDebugWireProtocol_JDWP: Debugger found" );

            /*if the program is here means that a jdwp debugger is found*/
            this.jdwp_debugger_found ( );

        }

    }

    /*function used after that a jdwp debugger is detected*/
    private void jdwp_debugger_found ( ) {

        /*do some operations after debugger detection*/

    }

    /*function to check if a jdwp debugger is found*/
    public boolean isFoundJdwpDebugger ( ) {

        /*return if a jdwp debugger is found*/
        return this.javaDebugWireProtocol_jdwp_found;

    }
}
