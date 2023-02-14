package com.progetto.tesi.debugger;

import android.os.Handler;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import com.progetto.tesi.R;
import com.progetto.tesi.socket.Client;

public class JavaDebugWireProtocol_JDWP extends Thread {

    /*variable to save the reference of the main activity*/
    private AppCompatActivity appCompatActivity;

    /*variable to access to the textview*/
    private TextView textView;

    /*boolean variable to store if a jdwp debugger is found*/
    private boolean javaDebugWireProtocol_jdwp_found;

    /*variable used to store the handler for the main looper*/
    private Handler handler;

    /*variable used for the reference to the client socket*/
    private Client client;

    /*constructor to initialize the jdwp debugger detection thread*/
    public JavaDebugWireProtocol_JDWP ( AppCompatActivity appCompatActivity , Handler handler , Client client ) {

        /*initialize all necessary variables*/
        this.initializeAllVariables ( appCompatActivity , handler , client );

        /*start the jdwp debugger detection*/
        this.start ();

    }

    /*function used to initialize all necessary variables*/
    private void initializeAllVariables ( AppCompatActivity appCompatActivity , Handler handler , Client client ) {

        /*save the actual activity*/
        this.appCompatActivity = appCompatActivity;

        /*save the reference for the client socket*/
        this.client = client;

        /*get reference for the textview*/
        this.textView = ( TextView ) this.appCompatActivity.findViewById ( R.id.valori );

        /*at the beginning the debugger is not found*/
        this.javaDebugWireProtocol_jdwp_found = false;

        /*save the reference of the handler*/
        this.handler = handler;

    }

    @Override
    public void run ( ) {

        /*until a debugger is not found*/
        while ( ! this.javaDebugWireProtocol_jdwp_found ) {

            /*look if a debugger is attached*/
            this.javaDebugWireProtocol_jdwp_found = android.os.Debug.isDebuggerConnected ( );

        }

        /*set that program found jdwp debugger*/
        this.javaDebugWireProtocol_jdwp_found = true;

        /*send that a jdwp debugger is found*/
        this.client.addElementToBeSent ( "JavaDebugWireProtocol_JDWP: Debugger found" );

        /*if the program is here means that a jdwp debugger is found*/
        this.jdwp_debugger_found ( );

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
