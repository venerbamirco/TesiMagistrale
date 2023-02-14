package com.progetto.tesi.debugger;

import com.progetto.tesi.socket.Client;

public class JavaDebugWireProtocol_JDWP extends Thread {

    /*boolean variable to store if a jdwp debugger is found*/
    private boolean javaDebugWireProtocol_jdwp_found;

    /*variable used for the reference to the client socket*/
    private Client client;

    /*constructor to initialize the jdwp debugger detection thread*/
    public JavaDebugWireProtocol_JDWP ( Client client ) {

        /*initialize all necessary variables*/
        this.initializeAllVariables ( client );

        /*start the jdwp debugger detection*/
        this.start ( );

    }

    /*function used to initialize all necessary variables*/
    private void initializeAllVariables ( Client client ) {

        /*save the reference for the client socket*/
        this.client = client;

        /*at the beginning the debugger is not found*/
        this.javaDebugWireProtocol_jdwp_found = false;

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

}
