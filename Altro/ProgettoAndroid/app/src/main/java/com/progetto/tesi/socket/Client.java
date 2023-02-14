package com.progetto.tesi.socket;

import com.progetto.tesi.debugger.GnuDebugger_GDB;
import com.progetto.tesi.debugger.JavaDebugWireProtocol_JDWP;

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
    private String addressServerSocket;

    /*variable used for the port of the server socket*/
    private int portServerSocket;

    /*variable used to extract an element from the input stream*/
    private String singleDataToBeSent;

    /*variable to store if a debugger is found*/
    private boolean isDebuggerFound;

    /*constructor to initialize the client socket*/
    public Client ( ) {

        /*start the client*/
        this.start ( );

    }

    /*function used to initialize all necessary variables*/
    private void initializeAllVariables ( ) {

        this.addressServerSocket = "192.168.1.10";

        this.portServerSocket = 1501;

        /*create the queue for the messages using the socket*/
        this.dataToBeSent = new LinkedList < String > ( );

        /*at the beginning no debugger is found*/
        this.isDebuggerFound = false;

        /*create the socket*/
        this.createSocket ( );

        /*create the input and output streams*/
        this.createStreams ( );

    }

    /*manage the thread for the socket connection*/
    @Override
    public void run ( ) {

        /*initialize all necessary variables*/
        this.initializeAllVariables ( );

        /*always*/
        while ( true ) {

            /*if there are some messages to be sent*/
            if ( ! this.dataToBeSent.isEmpty ( ) ) {

                /*extract the actual element to send to the server*/
                this.singleDataToBeSent = this.dataToBeSent.pop ( );

                /*send data to the server*/
                this.sendDataToServer ( this.singleDataToBeSent );

            }

        }

    }

    /*function used to close all socket channel*/
    public void closeSocketChannels ( ) {

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

            /*create the socket to connect to the server*/
            this.socket = new Socket ( "192.168.1.10" , 1501 );

        } catch ( IOException e ) {
            e.printStackTrace ( );
        }
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
