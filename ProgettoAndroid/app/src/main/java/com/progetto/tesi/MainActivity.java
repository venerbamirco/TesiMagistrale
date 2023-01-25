package com.progetto.tesi;

import android.os.Bundle;
import android.os.Handler;
import android.os.Looper;

import androidx.appcompat.app.AppCompatActivity;

import com.progetto.tesi.ptracer.Ptracer;

public class MainActivity extends AppCompatActivity {

    /*variable for the data management class object*/
    private DataManagement dataManagement;

    /*handler to manage the change of activities*/
    private Handler handler;

    @Override
    protected void onCreate ( Bundle savedInstanceState ) {
        super.onCreate ( savedInstanceState );
        setContentView ( R.layout.activity_main );

        /*initialize all necessary variables*/
        this.initializeVariables ( );
    }

    /*function used to initialize all necessary variables*/
    private void initializeVariables ( ) {

        /*initialize the handler with the main looper*/
        this.handler = new Handler ( Looper.getMainLooper ( ) );

        /*initialize the data management class object*/
        this.dataManagement = new DataManagement ( this , this.handler );

    }

    @Override
    protected void onPause ( ) {
        super.onPause ( );

        /*if the data management object is created*/
        if ( this.dataManagement != null ) {

            /*call the onpause method*/
            this.dataManagement.onPause ( );

        }

    }

    @Override
    protected void onResume ( ) {
        super.onResume ( );

        /*if the data management object is created*/
        if ( this.dataManagement != null ) {

            /*call the onresume method*/
            this.dataManagement.onResume ( );

        }

    }

}