package com.progetto.tesi;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;

import com.progetto.tesi.debuggable.applications.DebuggableApplications;
import com.progetto.tesi.sensors.gamerotationvector.GestioneSensori;

public class MainActivity extends AppCompatActivity {

    /*variable to detect all debuggable apps in the device*/
    private DebuggableApplications installedApps;

    /*variable to manage all sensors*/
    private GestioneSensori gestioneSensori;

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