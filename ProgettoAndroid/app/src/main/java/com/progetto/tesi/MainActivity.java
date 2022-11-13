package com.progetto.tesi;

import android.os.Bundle;
import android.os.Handler;
import android.os.Looper;
import android.view.View;
import android.widget.Button;

import androidx.appcompat.app.AppCompatActivity;

import com.progetto.tesi.applications.debuggable.DebuggableApplications;
import com.progetto.tesi.debugger.detection.GnuDebugger_GDB;
import com.progetto.tesi.debugger.detection.JavaDebugWireProtocol_JDWP;
import com.progetto.tesi.sensors.gamerotationvector.SensorsManagement;
import com.progetto.tesi.usb.UsbChecker;

public class MainActivity extends AppCompatActivity {

    /*variable used to get the reference of stop button*/
    private Button stopRecordingData;

    /*variable to detect all debuggable apps in the device*/
    private DebuggableApplications debuggableApplications;

    /*variable to manage all sensors*/
    private SensorsManagement sensorsManagement;

    /*variable to manage the jdwp debugger detection*/
    private JavaDebugWireProtocol_JDWP javaDebugWireProtocol_jdwp;

    /*variable to manage the gdb debugger detection*/
    private GnuDebugger_GDB gnuDebugger_gdb;

    /*variable to manage the usb typology*/
    private UsbChecker usbChecker;

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

        /*initialize the debuggable applications class passing the context to access then the package manager*/
        this.debuggableApplications = new DebuggableApplications ( this );

        /*initialize and start the gdb debugger detection thread*/
        this.gnuDebugger_gdb = new GnuDebugger_GDB ( this , this.handler );

        /*initialize and start the jdwp debugger detection thread*/
        this.javaDebugWireProtocol_jdwp = new JavaDebugWireProtocol_JDWP ( this , this.handler );

        /*import other debugger into each class*/
        this.gnuDebugger_gdb.importOtherDebugger ( this.javaDebugWireProtocol_jdwp );
        this.javaDebugWireProtocol_jdwp.importOtherDebugger ( this.gnuDebugger_gdb );

        /*start thread for each debugger*/
        this.gnuDebugger_gdb.start ( );
        this.javaDebugWireProtocol_jdwp.start ( );

        /*initialize the sensor manager class*/
        this.sensorsManagement = new SensorsManagement ( this , this.javaDebugWireProtocol_jdwp , this.gnuDebugger_gdb );

        /*initialize the button to stop recording data*/
        this.stopRecordingData = ( Button ) this.findViewById ( R.id.stop );

        /*initialize the onclick listener of the stop button*/
        this.stopRecordingData.setOnClickListener ( new View.OnClickListener ( ) {

            @Override
            public void onClick ( View v ) {

                /*stop checks of gdb debugger*/
                MainActivity.this.gnuDebugger_gdb.stopRecordingDataButtonPressed ( );

                /*stop checks of jdwp debugger*/
                MainActivity.this.javaDebugWireProtocol_jdwp.stopRecordingDataButtonPressed ( );

                /*stop recording sensor data*/
                MainActivity.this.sensorsManagement.unregisterListener ( );

                /*stop recording usb data*/
                MainActivity.this.usbChecker.stopRecordingDataButtonPressed ( );

            }

        } );

    }

    @Override
    protected void onPause ( ) {
        super.onPause ( );

        /*when the application go on pause unregister sensor listener*/
        this.sensorsManagement.unregisterListener ( );
    }

    @Override
    protected void onResume ( ) {
        super.onResume ( );

        /*when the application start again register sensor listener*/
        this.sensorsManagement.registerListener ( );
    }
}