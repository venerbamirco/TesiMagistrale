package com.progetto.tesi.socket;

import com.progetto.tesi.debugger.detection.GnuDebugger_GDB;
import com.progetto.tesi.debugger.detection.JavaDebugWireProtocol_JDWP;

import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.time.Instant;
import java.util.LinkedList;

/*class to manage the tcp client socket to send all data to the server*/
public class Client extends Thread {

    /*variable used to send this string using the socket*/
    private LinkedList < String > dataToBeSent;

    /*variable used for the socket definition*/
    private Socket socket;

    /*variable used for the input stream*/
    private DataInputStream dataInputStream;

    /*variable used for the output stream*/
    private DataOutputStream dataOutputStream;

    /*variable used for address of the server socket*/
    private String addressServerSocket = "192.168.1.10";

    /*variable used for the port of the server socket*/
    private int portServerSocket = 1501;

    /*variable used to extract an element from the input stream*/
    private String singleDataToBeSent;

    /*variable to check the jdwp debugger detection*/
    private JavaDebugWireProtocol_JDWP javaDebugWireProtocol_jdwp;

    /*variable to check the gdb debugger detection*/
    private GnuDebugger_GDB gnuDebugger_gdb;

    /*variable to store if a debugger is found*/
    private boolean isDebuggerFound;

    /*constructor to initialize the client socket*/
    public Client ( ) {

    }

    /*function used to initialize all necessary variables*/
    private void initializeAllVariables ( ) {

        /*create the queue for the messages using the socket*/
        this.dataToBeSent = new LinkedList < String > ( );

        /*at the beginning no debugger is found*/
        this.isDebuggerFound = false;

        /*create the socket*/
        this.createSocket ( );

        /*create the input and output streams*/
        this.createStreams ( );

    }

    /*function used to import the variables to check if there is a debugger*/
    public void importReferenceDebuggerDetection ( GnuDebugger_GDB gnuDebugger_gdb , JavaDebugWireProtocol_JDWP javaDebugWireProtocol_jdwp ) {

        /*save the reference for the two debuggers*/
        this.gnuDebugger_gdb = gnuDebugger_gdb;
        this.javaDebugWireProtocol_jdwp = javaDebugWireProtocol_jdwp;

    }

    /*manage the thread for the socket connection*/
    @Override
    public void run ( ) {

        /*initialize all necessary variables*/
        this.initializeAllVariables ( );

        /*quando iniviio le stringhe settare a true un flag per ciascun debugger*/
        //while ( ( this.gnuDebugger_gdb == null || ! this.gnuDebugger_gdb.isFoundGnuDebugger ( ) ) && ( this.javaDebugWireProtocol_jdwp == null || ! this.javaDebugWireProtocol_jdwp.isFoundJdwpDebugger ( ) ) ) {
        while ( true ) {

            /*check for a gdb debugger*/
            if ( this.gnuDebugger_gdb != null && this.gnuDebugger_gdb.isFoundGnuDebugger ( ) ) {

                /*a debugger is found*/
                this.isDebuggerFound = true;

            }

            /*check for a jdwp debugger*/
            else if ( this.javaDebugWireProtocol_jdwp != null && this.javaDebugWireProtocol_jdwp.isFoundJdwpDebugger ( ) ) {

                /*a debugger is found*/
                this.isDebuggerFound = true;

            }

            /*if a debugger is found*/
            if ( this.isDebuggerFound ) {

                /*while there are messages to be sent*/
                while ( ! this.dataToBeSent.isEmpty ( ) ) {

                    /*extract the actual element to send to the server*/
                    this.singleDataToBeSent = this.dataToBeSent.pop ( );

                    /*send data to the server*/
                    this.sendDataToServer ( this.singleDataToBeSent );

                }

                /*when the thread finish, close all socket channels*/
                this.closeSocketChannels ( );

            }

            /*if a debugger is not found*/
            else {

                /*if there are some messages to be sent*/
                if ( ! this.dataToBeSent.isEmpty ( ) ) {

                    /*extract the actual element to send to the server*/
                    this.singleDataToBeSent = this.dataToBeSent.pop ( );

                    /*send data to the server*/
                    this.sendDataToServer ( this.singleDataToBeSent );

                }

            }


        }


    }

    /*function used to close all socket channel*/
    private void closeSocketChannels ( ) {

        try {
            /*close input channel*/
            this.dataInputStream.close ( );

            /*close output channel*/
            this.dataOutputStream.close ( );

            /*close socket channel*/
            this.socket.close ( );

        } catch ( IOException e ) {
            e.printStackTrace ( );
        }

    }

    /*function used to create the socket*/
    private void createSocket ( ) {
        try {
            System.out.println ("entrato" );
            /*create the socket to connect to the server*/
            this.socket = new Socket ( "192.168.1.10" , 1501 );
            System.out.println ("entrato1" );

        } catch ( IOException e ) {
            System.out.println ("entrato2" );
            System.out.println ( e.getMessage ( ) );
            e.printStackTrace ( );
        }
        System.out.println ("entrato3" );
    }

    /*function used to create the two streams*/
    private void createStreams ( ) {
        try {

            /*create the input stream*/
            this.dataInputStream = new DataInputStream ( new BufferedInputStream ( this.socket.getInputStream ( ) ) );

            /*create the output stream*/
            this.dataOutputStream = new DataOutputStream ( new BufferedOutputStream ( this.socket.getOutputStream ( ) ) );

        } catch ( IOException e ) {
            e.printStackTrace ( );
        }
    }

    /*function used to send data to the server*/
    private void sendDataToServer ( String dataToSend ) {

        /*if there is a valid string to be sent*/
        if ( dataToSend != null && dataToSend != "" ) {

            try {

                /*send data to the server*/
                this.dataOutputStream.writeBytes ( dataToSend );

                /*force data to be sent*/
                this.dataOutputStream.flush ( );

            } catch ( IOException e ) {
                e.printStackTrace ( );
            }
        }

    }

    /*function used to add the current string to the output list to be sent*/
    public void addElementToBeSent ( String dataToBeSent ) {

        /*add current string to the linkedlist with its timestamp*/
        this.dataToBeSent.push ( Instant.now ( ).toEpochMilli ( ) + " " + dataToBeSent + "\n" );

    }


}
