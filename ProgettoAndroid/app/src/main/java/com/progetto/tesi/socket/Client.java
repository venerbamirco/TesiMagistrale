package com.progetto.tesi.socket;

import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.util.LinkedList;

/*class to manage the tcp client socket to send all data to the server*/
public class Client extends Thread {

    /*variable used to send this string using the socket*/
    public LinkedList < String > dataToBeSent;

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
    /*variable used for receive data from socket*/
    private byte[] dataToBeReceived;

    /*constructor to initialize the client socket*/
    public Client ( ) {

        /*do nothing because the creation of socket in android must be done into a thread*/

        /*create the queue for the messages using the socket*/
        this.dataToBeSent = new LinkedList < String > ( );

        this.dataToBeReceived = new byte[ 100 ];

    }

    /*manage the thread for the socket connection*/
    @Override
    public void run ( ) {

        /*initialize all necessary variables*/
        this.initializeAllVariables ( );

        //System.out.println (this.dataToBeSent.size () );

        while ( true ) {
            if ( this.dataToBeSent.size ( ) > 0 ) {
                /*send data to the server*/
                this.sendDataToServer ( this.dataToBeSent.pop ( ) );

                /*try {
                    this.dataInputStream.read ( this.dataToBeReceived );

                    System.out.println ( "Ricevuto: " + new String ( this.dataToBeReceived ).substring(0, 2) );
                } catch ( IOException e ) {
                    e.printStackTrace ( );
                }*/

            }


        }


    }

    /*function used to initialize all necessary variables*/
    private void initializeAllVariables ( ) {



        /*create the socket*/
        this.createSocket ( );

        /*create the input and output streams*/
        this.createStreams ( );

    }

    /*function used to create the socket*/
    private void createSocket ( ) {
        try {
            /*create the socket to connect to the server*/
            this.socket = new Socket ( "192.168.1.10" , 1501 );
        } catch ( IOException e ) {
            System.out.println ( e.getMessage ( ) );
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
        if ( dataToSend != null && dataToSend != "" ) {
            try {
                /*send data to the server*/
                this.dataOutputStream.writeBytes ( dataToSend );
                /*flush data*/
                this.dataOutputStream.flush ( );
            } catch ( IOException e ) {
                System.out.println ( "failed to send" );
                e.printStackTrace ( );
            }
        }

    }

    public void addElementToBeSent ( String dataToBeSent ) {
        this.dataToBeSent.push ( dataToBeSent );
    }


}
