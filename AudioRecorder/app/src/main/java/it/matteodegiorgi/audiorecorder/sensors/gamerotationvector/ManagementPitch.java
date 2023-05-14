package it.matteodegiorgi.audiorecorder.sensors.gamerotationvector;

public class ManagementPitch {

    /*variables to store the values of pitch*/
    private double pitchDouble;
    private int pitchInt;

    /*constructor to initialize the manager of pitch value*/
    public ManagementPitch ( ) {

        /*initialize all necessary variables*/
        this.initializeAllVariables ( );

    }

    /*function used to initialize all necessary variables*/
    private void initializeAllVariables ( ) {

        /*initialize the pitch values*/
        this.pitchInt = 0;
        this.pitchDouble = 0;

    }

    /*function used to filter the pitch values*/
    public void filterPitch ( double pitch ) {

        /*simply save the actual value*/
        this.pitchDouble = pitch;
        this.pitchInt = ( int ) this.pitchDouble;

    }

    /*function used to get the double value of pitch*/
    public double getPitchDouble ( ) {
        return this.pitchDouble;
    }

    /*function used to get the integer value of roll*/
    public int getPitchInt ( ) {
        return this.pitchInt;
    }

}