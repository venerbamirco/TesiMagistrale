package com.progetto.tesi;

import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;
import android.os.Looper;

import androidx.appcompat.app.AppCompatActivity;

import com.progetto.tesi.applications.debuggable.DebuggableApplications;
import com.progetto.tesi.debugger.detected.GnuDebugger_GDB_Activity;
import com.progetto.tesi.debugger.detected.JavaDebugWireProtocol_JDWP_Activity;
import com.progetto.tesi.debugger.detection.GnuDebugger_GDB;
import com.progetto.tesi.debugger.detection.JavaDebugWireProtocol_JDWP;
import com.progetto.tesi.sensors.gamerotationvector.SensorsManagement;

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

        //this.waitThreadDebugger ( );
    }

    /*function used to initialize all necessary variables*/
    private void initializeVariables ( ) {

        /*initialize the debuggable applications class passing the context to access then the package manager*/
        this.debuggableApplications = new DebuggableApplications ( this );

        Handler handler = new Handler ( Looper.getMainLooper());

        /*initialize and start the gdb debugger detection thread*/
        this.gnuDebugger_gdb = new GnuDebugger_GDB ( this, handler );

        /*initialize and start the jdwp debugger detection thread*/
        this.javaDebugWireProtocol_jdwp = new JavaDebugWireProtocol_JDWP ( this );

        /*import other debugger into each class*/
        this.gnuDebugger_gdb.importOtherDebugger ( this.javaDebugWireProtocol_jdwp );
        this.javaDebugWireProtocol_jdwp.importOtherDebugger ( this.gnuDebugger_gdb );

        /*start thread for each debugger*/
        this.gnuDebugger_gdb.start ( );
        this.javaDebugWireProtocol_jdwp.start ( );

        /*initialize the sensor manager class*/
        this.sensorsManagement = new SensorsManagement ( this , this.javaDebugWireProtocol_jdwp , this.gnuDebugger_gdb );

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

    private void waitThreadDebugger ( ) {

        try {
            this.gnuDebugger_gdb.join ( );
            this.javaDebugWireProtocol_jdwp.join ( );
        } catch ( InterruptedException e ) {
            e.printStackTrace ( );
        }

        if ( this.gnuDebugger_gdb.isFoundGnuDebugger ( ) ) {
            Intent myIntent = new Intent ( this , GnuDebugger_GDB_Activity.class );
            startActivity ( myIntent );
        } else if ( this.javaDebugWireProtocol_jdwp.isFoundJdwpDebugger ( ) ) {
            Intent myIntent = new Intent ( this , JavaDebugWireProtocol_JDWP_Activity.class );
            startActivity ( myIntent );
        }

    }
}