package com.progetto.tesi.sensors.gamerotationvector;

import android.content.Context;
import android.hardware.Sensor;
import android.hardware.SensorManager;
import android.widget.Button;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import com.progetto.tesi.R;

public class GestioneSensori {

    /*variables for the references to the activity and its element*/
    private AppCompatActivity appCompatActivity = null;
    private Button button = null;
    private TextView textView = null;

    private SensorListener sensorListener = null;
    private SensorManager sensorManager = null;
    private Sensor sensor = null;

    public GestioneSensori ( AppCompatActivity appCompatActivity ) {

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
        this.button.setOnClickListener ( v -> GestioneSensori.this.sensorListener.calibrateSensors ( ) );

        /*initialize sensors when the user open the app*/
        this.waitNumberSeconds ( );
    }

    /*unnecessary function used to wait tot milliseconds before start register sensor data*/
    private void waitNumberSeconds ( ) {

        /*create a thread to do some actions*/
        new Thread ( ( ) -> {

            /*wait 1 seconds (time that user open the app and take on correct position the smartphone in the hand*/
            try {
                Thread.sleep ( 500 );
            } catch ( InterruptedException e ) {
                e.printStackTrace ( );
            }

            /*now we calibrate the sensor*/
            GestioneSensori.this.sensorListener.calibrateSensors ( );

            /*then we can say that calibration is success*/
            GestioneSensori.this.sensorListener.setFirstCalibrationDone ( );

        } ).start ( );
    }

    /*function used to unregister a listener*/
    public void unregisterListener ( ) {
        if ( this.sensorManager != null ) {
            this.sensorManager.unregisterListener ( this.sensorListener );
        }
    }

    /*function used to register a lister*/
    public void registerListener ( ) {
        if ( this.sensorManager != null ) {
            this.sensorManager.registerListener ( this.sensorListener , this.sensor , SensorManager.SENSOR_DELAY_FASTEST );
        }
    }

}