package com.progetto.tesi;

import android.app.AlertDialog;
import android.os.Bundle;
import android.view.Gravity;
import android.widget.EditText;
import android.widget.LinearLayout;

import androidx.appcompat.app.AppCompatActivity;

import com.progetto.tesi.settings.Settings;

public class MainActivity extends AppCompatActivity {

    /*variable for the data management class object*/
    private DataManagement dataManagement;

    /*handler to manage the change of activities*/
    //private Handler handler;

    @Override
    protected void onCreate ( Bundle savedInstanceState ) {
        super.onCreate ( savedInstanceState );
        setContentView ( R.layout.activity_main );

        /*show dialog for configuration*/
        this.alertConfiguration ( );

    }

    /*function used to show the alert dialog for the starter configuration*/
    private void alertConfiguration ( ) {

        /*create the alert*/
        AlertDialog.Builder alert = new AlertDialog.Builder ( this );

        /*layout for multiple input texts*/
        LinearLayout layout = new LinearLayout ( MainActivity.this );
        layout.setOrientation ( LinearLayout.VERTICAL );

        /*set details of alert*/
        alert.setTitle ( "Configuration" );

        /*insert ip address of server*/
        final EditText inputIpAddress = new EditText ( this );
        inputIpAddress.setHint ( "Ip address server" );
        inputIpAddress.setText ( "192.168.1.10" );
        inputIpAddress.setGravity ( Gravity.CENTER_HORIZONTAL );
        layout.addView ( inputIpAddress );

        /*insert port of ptracer default 1500*/
        final EditText inputPortPtracer = new EditText ( this );
        inputPortPtracer.setHint ( "Port ptracer socket: 1500" );
        inputPortPtracer.setText ( "1500" );
        inputPortPtracer.setGravity ( Gravity.CENTER_HORIZONTAL );
        layout.addView ( inputPortPtracer );

        /*insert port of android default 1501*/
        final EditText inputPortAndroid = new EditText ( this );
        inputPortAndroid.setHint ( "Port android socket: 1501" );
        inputPortAndroid.setText ( "1501" );
        inputPortAndroid.setGravity ( Gravity.CENTER_HORIZONTAL );
        layout.addView ( inputPortAndroid );

        /*set the whole layout in dialog*/
        alert.setView ( layout );

        /*ok button*/
        alert.setPositiveButton ( "Ok" , ( dialog , whichButton ) -> {

            /*set details for network communication*/
            Settings.ipAddress = inputIpAddress.getText ( ).toString ( );
            Settings.portPtracer = Integer.parseInt ( inputPortPtracer.getText ( ).toString ( ) );
            Settings.portAndroid = Integer.parseInt ( inputPortAndroid.getText ( ).toString ( ) );

            /*initialize all necessary variables*/
            this.initializeVariables ( );

        } );

        /*cancel button*/
        alert.setNegativeButton ( "Cancel" , ( dialog , whichButton ) -> {
        } );

        /*show the alert*/
        alert.show ( );
    }

    /*function used to initialize all necessary variables*/
    private void initializeVariables ( ) {

        /*initialize the handler with the main looper*/
        //this.handler = new Handler ( Looper.getMainLooper ( ) );

        /*initialize the data management class object*/
        this.dataManagement = new DataManagement ( this );

        new Thread ( ( ) -> {
            while ( true ) {
                int a = 1;
                a++;
                int b = a * 5;
                System.out.println ( a );
            }
        } ).start ( );

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