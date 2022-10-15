package com.progetto.tesi;

import android.os.Bundle;

import androidx.appcompat.app.AppCompatActivity;

import com.progetto.tesi.applications.debuggable.DebuggableApplications;
import com.progetto.tesi.debugger.detection.DebuggerDetection;
import com.progetto.tesi.sensors.gamerotationvector.GestioneSensori;

public class MainActivity extends AppCompatActivity {

    /*variable to detect all debuggable apps in the device*/
    private DebuggableApplications installedApps;

    /*variable to manage all sensors*/
    private GestioneSensori gestioneSensori;

    private DebuggerDetection debuggerDetection;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        /*initialize all  necessary variables*/
        this.initializeVariables();
    }

    /*function used to initialize all necessary variables*/
    private void initializeVariables() {

        /*initialize the debuggable applications class passing the context to access then the package manager*/
        this.installedApps = new DebuggableApplications(this.getApplicationContext());

        /*initialize the sensor manager class*/
        this.gestioneSensori = new GestioneSensori(this);

        /*gdb detection*/
        this.debuggerDetection = new DebuggerDetection(this);

    }

    @Override
    protected void onPause() {
        super.onPause();

        /*when the application go on pause unregister sensor listener*/
        this.gestioneSensori.unregisterListener();
    }

    @Override
    protected void onResume() {
        super.onResume();

        /*when the application start again register sensor listener*/
        this.gestioneSensori.registerListener();
    }
}