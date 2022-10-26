package com.progetto.tesi;

import android.os.Bundle;

import androidx.appcompat.app.AppCompatActivity;

import com.progetto.tesi.applications.debuggable_done.DebuggableApplications;
import com.progetto.tesi.debugger.detection_done.GnuDebugger_GDB;
import com.progetto.tesi.debugger.detection_done.JavaDebugWireProtocol_JDWP;
import com.progetto.tesi.sensors.gamerotationvector_done.SensorsManagement;

public class MainActivity extends AppCompatActivity {

    /*variable to detect all debuggable apps in the device*/
    private DebuggableApplications debuggableApplications;

    /*variable to manage all sensors*/
    private SensorsManagement sensorsManagement;

    /*variable to manage the jdwp debugger detection*/
    private JavaDebugWireProtocol_JDWP javaDebugWireProtocol_jdwp;

    /*variable to manage the gdb debugger detection*/
    private GnuDebugger_GDB gnuDebugger_gdb;

    @Override
    protected void onCreate ( Bundle savedInstanceState ) {
        super.onCreate ( savedInstanceState );
        setContentView ( R.layout.activity_main );

        /*initialize all necessary variables*/
        this.initializeVariables ( );
    }

    /*function used to initialize all necessary variables*/
    private void initializeVariables ( ) {

        /*initialize the debuggable applications class passing the context to access then the package manager*/
        this.debuggableApplications = new DebuggableApplications ( this );

        /*initialize the sensor manager class*/
        this.sensorsManagement = new SensorsManagement ( this );

        /*initialize and start the gdb debugger detection thread*/
        this.gnuDebugger_gdb = new GnuDebugger_GDB ( this );

        /*initialize and start the jdwp debugger detection thread*/
        this.javaDebugWireProtocol_jdwp = new JavaDebugWireProtocol_JDWP ( );

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