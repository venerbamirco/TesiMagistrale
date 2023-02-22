package com.progetto.training.developeroptions;

import android.provider.Settings;

import androidx.appcompat.app.AppCompatActivity;

import com.progetto.training.socket.Client;

public class DeveloperOptions extends Thread {

    /*variable for the reference for the appcompat activity*/
    private AppCompatActivity appCompatActivity;

    /*variables to store if the adb and developer options are enabled*/
    private boolean adbActivated;
    private boolean developerOptionsActivated;

    /*old variables to store if the adb and developer options are enabled*/
    private boolean oldAdbActivated;
    private boolean oldDeveloperOptionsActivated;

    /*variable used to store the number of misurations*/
    private int misurations;

    /*variable used to save the reference to the client socket*/
    private Client client;

    /*constructor to initialize the developer option detection mechanism*/
    public DeveloperOptions ( AppCompatActivity appCompatActivity , Client client ) {

        /*initialize all necessary variables*/
        this.initializeAllNecessaryVariables ( appCompatActivity , client );

        /*start actual thread*/
        this.start ( );

    }

    /*function to initialize all necessary variables*/
    private void initializeAllNecessaryVariables ( AppCompatActivity appCompatActivity , Client client ) {

        /*save the reference for the main activity*/
        this.appCompatActivity = appCompatActivity;

        /*save the reference to the client socket*/
        this.client = client;

        /*at beginning number of misurations equal to 0*/
        this.misurations = 0;

    }

    @Override
    public void run ( ) {

        /*always*/
        while ( true ) {

            try {

                /*get actual values for adb and developer options if they are activated*/
                this.adbActivated = Settings.Global.getInt ( this.appCompatActivity.getApplicationContext ( ).getContentResolver ( ) , Settings.Global.ADB_ENABLED ) > 0;
                this.developerOptionsActivated = Settings.Global.getInt ( this.appCompatActivity.getApplicationContext ( ).getContentResolver ( ) , Settings.Global.DEVELOPMENT_SETTINGS_ENABLED ) > 0;

            } catch ( Settings.SettingNotFoundException e ) {
                e.printStackTrace ( );
            }

            /*if first misuration*/
            if ( this.misurations == 0 ) {

                /*print all informations*/
                this.printAllDetails ( );

            }

            /*if not the first misuration*/
            else {

                /*print only if there is at least one change*/
                if ( this.oldAdbActivated != this.adbActivated || this.oldDeveloperOptionsActivated != this.developerOptionsActivated ) {

                    /*print all informations*/
                    this.printAllDetails ( );

                }

            }

            /*save actual misurations*/
            this.saveActualValues ( );

            /*increment number of misurations*/
            this.misurations++;

        }

    }

    /*function used to print all details*/
    private void printAllDetails ( ) {

        /*send all data*/
        this.client.addElementToBeSent ( "DeveloperOptions: adb: " + this.adbActivated + " devops: " + this.developerOptionsActivated );

    }

    /*function used to save actual values*/
    private void saveActualValues ( ) {

        /*save actual variables in old variables of adb and developer options activated*/
        this.oldAdbActivated = this.adbActivated;
        this.oldDeveloperOptionsActivated = this.developerOptionsActivated;

    }


}
