package com.progetto.tesi.sensors.gamerotationvector;

import android.content.Context;
import android.hardware.Sensor;
import android.hardware.SensorManager;
import android.widget.Button;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import com.progetto.tesi.R;

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

    public SensorsManagement ( AppCompatActivity appCompatActivity ) {

        /*initialize all variables*/
        this.initializeAllVariables ( appCompatActivity );

        /*initialize sensors when the user open the app*/
        this.waitNumberSeconds ( );
    }

    /*function used to initialize all necessary variables*/
    private void initializeAllVariables ( AppCompatActivity appCompatActivity ) {

        /*save the actual activity to access forward to the layout object*/
        this.appCompatActivity = appCompatActivity;

        /*get the references of all necessary object in the activity layout*/
        this.button = ( Button ) this.appCompatActivity.findViewById ( R.id.calibra );
        this.textView = ( TextView ) this.appCompatActivity.findViewById ( R.id.valori );

        /*obtain the sensor manager to access forward to each necessary sensor*/
        this.sensorManager = ( SensorManager ) this.appCompatActivity.getSystemService ( Context.SENSOR_SERVICE );

        /*obtain the game rotation vector sensor*/
        this.sensor = this.sensorManager.getDefaultSensor ( Sensor.TYPE_GAME_ROTATION_VECTOR );

        /*initialize and register the sensor listener*/
        this.sensorListener = new SensorListener ( this.appCompatActivity );
        this.sensorManager.registerListener ( this.sensorListener , this.sensor , SensorManager.SENSOR_DELAY_FASTEST );

        /*set the event for the calibrate button click*/
        this.button.setOnClickListener ( v -> SensorsManagement.this.sensorListener.calibrateSensors ( ) );

    }

    /*function used to wait tot milliseconds before start register sensor data*/
    private void waitNumberSeconds ( ) {

        /*create a thread to do initial sensors calibration*/
        new Thread ( ( ) -> {

            /*wait 1 seconds (time that user open the app and take on correct position the smartphone in the hand*/
            try {
                Thread.sleep ( 1000 );
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
            this.sensorManager.registerListener ( this.sensorListener , this.sensor , SensorManager.SENSOR_DELAY_FASTEST );

        }
    }

}