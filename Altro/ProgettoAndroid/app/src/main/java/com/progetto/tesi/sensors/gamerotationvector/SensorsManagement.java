package com.progetto.tesi.sensors.gamerotationvector;

import android.content.Context;
import android.hardware.Sensor;
import android.hardware.SensorManager;
import android.widget.Button;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import com.progetto.tesi.R;
import com.progetto.tesi.debugger.GnuDebugger_GDB;
import com.progetto.tesi.debugger.JavaDebugWireProtocol_JDWP;
import com.progetto.tesi.socket.Client;

public class SensorsManagement {

    /*variables for the references to the activity and its element*/
    private AppCompatActivity appCompatActivity;
    private Button button;
    private TextView textView;

    /*variable for the sensor listener*/
    private SensorListener sensorListener;

    /*variable for the sensor manager*/
    private SensorManager sensorManager;

    /*variable for the unique used sensor*/
    private Sensor sensor;

    /*variable for the reference of the client*/
    private Client client;

    /*constructor to run the sensor management mechanism*/
    public SensorsManagement ( AppCompatActivity appCompatActivity , Client client ) {

        /*initialize all variables*/
        this.initializeAllVariables ( appCompatActivity , client );

        /*initialize sensors when the user open the app*/
        this.waitNumberSeconds ( );

    }

    /*function used to initialize all necessary variables*/
    private void initializeAllVariables ( AppCompatActivity appCompatActivity , Client client ) {

        /*save the actual activity to access forward to the layout object*/
        this.appCompatActivity = appCompatActivity;

        /*save the reference of the client*/
        this.client = client;

        /*get the references of all necessary object in the activity layout*/
        this.button = ( Button ) this.appCompatActivity.findViewById ( R.id.calibra );
        this.textView = ( TextView ) this.appCompatActivity.findViewById ( R.id.valori );

        /*obtain the sensor manager to access forward to each necessary sensor*/
        this.sensorManager = ( SensorManager ) this.appCompatActivity.getSystemService ( Context.SENSOR_SERVICE );

        /*obtain the game rotation vector sensor*/
        this.sensor = this.sensorManager.getDefaultSensor ( Sensor.TYPE_GAME_ROTATION_VECTOR );

        /*initialize and register the sensor listener*/
        this.sensorListener = new SensorListener ( this.appCompatActivity , client );
        this.registerListener ( );

        /*set the event for the calibrate button click*/
        this.button.setOnClickListener ( v -> SensorsManagement.this.sensorListener.calibrateSensors ( ) );

    }

    /*function used to wait tot milliseconds before start register sensor data*/
    private void waitNumberSeconds ( ) {

        /*create and start a thread to do initial sensors calibration*/
        new Thread ( ( ) -> {

            try {

                /*wait tot milliseconds (time that user opens the app and take a correct position for the smartphone in the hand*/
                Thread.sleep ( 2000 );

            } catch ( InterruptedException e ) {
                e.printStackTrace ( );
            }

            /*now we calibrate the sensor*/
            SensorsManagement.this.sensorListener.calibrateSensors ( );

            /*then we can say that the first calibration is success*/
            SensorsManagement.this.sensorListener.setFirstCalibrationDone ( );

        } ).start ( );
    }

    /*function used to unregister a listener*/
    public void unregisterListener ( ) {

        /*if the sensor manager is valid*/
        if ( this.sensorManager != null ) {

            /*unregister the listener*/
            this.sensorManager.unregisterListener ( this.sensorListener );

        }

    }

    /*function used to register a lister*/
    public void registerListener ( ) {

        /*if the sensor manager is valid*/
        if ( this.sensorManager != null ) {

            /*register the listener*/
            this.sensorManager.registerListener ( this.sensorListener , this.sensor , SensorManager.SENSOR_DELAY_NORMAL );

        }
    }

}