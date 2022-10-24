package com.progetto.tesi.debugger.detection_done;

public class JavaDebugWireProtocol_JDWP extends Thread {

    /*boolean variable to store if a jdwp debugger is found*/
    private boolean foundJdwpDebugger = false;

    /*constructor to initialize and start the jdwp debugger detection thread*/
    public JavaDebugWireProtocol_JDWP ( ) {

        /*initialize all necessary variables*/
        this.initializeAllVariables ( );

        /*start the thread*/
        this.start ( );

    }

    /*function used to initialize all necessary variables*/
    private void initializeAllVariables ( ) {

        /*at the beginning the debugger is not found*/
        this.foundJdwpDebugger = false;

    }

    @Override
    public void run ( ) {

        /*until a debugger is not found*/
        while ( ! this.foundJdwpDebugger ) {

            /*debug row to say that a debugger is not found*/
            System.out.println ( "JavaDebugWireProtocol_JDWP: Debugger not found" );

            /*look if a debugger is attached*/
            this.foundJdwpDebugger = android.os.Debug.isDebuggerConnected ( );

            /*one analysis each 5 seconds*/
            try {
                this.sleep ( 5000 );
            } catch ( InterruptedException e ) {
                e.printStackTrace ( );
            }

        }

        /*debug row to say that a debugger is found*/
        System.out.println ( "JavaDebugWireProtocol_JDWP: Debugger found" );

        /*if the program is here means that a jdwp debugger is found*/
        this.jdwp_debugger_found ( );

    }

    /*function used after that a jdwp debugger is detected*/
    private void jdwp_debugger_found ( ) {

        /*do some operations after debugger detection*/

    }
}
