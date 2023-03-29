package com.progetto.tesi.socket;

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


    int i = 1;


    /*constructor to initialize the client socket*/
    public Client ( String address , int port ) {

        /*save the info of actual server socket*/
        this.addressServerSocket = address;
        this.portServerSocket = port;

        /*start the client*/
        this.start ( );

    }

    /*function used to initialize all necessary variables*/
    private void initializeAllVariables ( ) {

        /*create the queue for the messages using the socket*/
        this.dataToBeSent = new LinkedList < String > ( );

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

            /*manage exception if no element in the list*/
            try {

                /*extract the actual element to send to the server*/
                this.singleDataToBeSent = this.dataToBeSent.pop ( );

                /*send data to the server*/
                this.sendDataToServer ( this.singleDataToBeSent );

            } catch ( Exception e ) {

                /*do nothing for the moment*/

            }

        }

    }

    /*function used to create the socket*/
    private void createSocket ( ) {

        try {

            /*create the socket to connect to the server*/
            this.socket = new Socket ( this.addressServerSocket , this.portServerSocket );

        } catch ( IOException e ) {

            /*do nothing for the moment*/

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

            /*do nothing for the moment*/

        }
    }

    /*function used to send data to the server*/
    public void sendDataToServer ( String dataToSend ) {

        /*if there is a valid string to be sent*/
        if ( dataToSend != null && dataToSend != "" ) {

            try {

                /*if socket and its channel are valid*/
                if ( this.dataOutputStream != null ) {

                    /*send data to the server*/
                    this.dataOutputStream.writeBytes ( dataToSend );

                    /*force data to be sent*/
                    this.dataOutputStream.flush ( );

                }

            } catch ( IOException e ) {

                /*do nothing for the moment*/

            }
        }

    }

    /*function used to add the current string to the output list to be sent*/
    public void addElementToBeSent ( String dataToBeSent ) {

        /*add current string to the linkedlist with its timestamp*/
        this.dataToBeSent.add ( Instant.now ( ).toEpochMilli ( ) + "@" + dataToBeSent + "\n" );

    }


}
