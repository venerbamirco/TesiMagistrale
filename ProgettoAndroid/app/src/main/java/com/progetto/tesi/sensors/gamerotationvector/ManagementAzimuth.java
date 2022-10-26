package com.progetto.tesi.sensors.gamerotationvector;

public class ManagementAzimuth {

    /*variables to store the limit points of azimuth value*/
    private double azimuthLimitBottom;
    private double azimuthLimitCenter;
    private double azimuthLimitTop;
    private double azimuthMinimumValue;
    private double azimuthMaximumValue;

    /*variables to store the values of azimuth*/
    private double azimuthDouble;
    private int azimuthInt;

    /*variable to store the calibrated value of azimuth*/
    private double azimuthCalibrateValue;

    /*constructor to initialize the manager of azimuth value*/
    public ManagementAzimuth ( ) {

        /*initialize all necessary variables*/
        this.initializeAllVariables ( );

    }

    /*function used to initialize all necessary variables*/
    private void initializeAllVariables ( ) {

        /*initialize the limit range of azimuth value*/
        this.azimuthLimitBottom = - 180;
        this.azimuthLimitCenter = 0;
        this.azimuthLimitTop = 180;

        /*initialize the limit top and bottom value of azimuth*/
        this.azimuthMinimumValue = - 180;
        this.azimuthMaximumValue = 180;

        /*initialize the azimuth values*/
        this.azimuthInt = 0;
        this.azimuthDouble = 0;

        /*initialize the calibrated value of azimuth*/
        this.azimuthCalibrateValue = 0;

    }

    /*function used to calibrate the azimuth values*/
    public void calibrateAzimuth ( double azimuth ) {

        /*save actual value of azimuth*/
        this.azimuthCalibrateValue = azimuth;

        /*save new range of azimuth values*/
        this.azimuthLimitBottom = this.azimuthCalibrateValue - 180;
        this.azimuthLimitCenter = this.azimuthCalibrateValue;
        this.azimuthLimitTop = this.azimuthCalibrateValue + 180;

        /*calculate new extreme range points for azimuth*/
        if ( this.azimuthLimitBottom < - 180 ) {
            this.azimuthMinimumValue = 360 - Math.abs ( this.azimuthLimitBottom );
            this.azimuthMaximumValue = 180 - Math.abs ( this.azimuthLimitCenter );
        } else if ( this.azimuthLimitTop >= 180 ) {
            this.azimuthMinimumValue = - 180 + Math.abs ( this.azimuthLimitCenter );
            this.azimuthMaximumValue = - 360 + Math.abs ( this.azimuthLimitTop );
        }

    }

    /*function used to filter the azimuth values*/
    public void filterAzimuth ( double azimuth ) {

        /*calculate the new value of azimuth in relation with the calibrated value using 0 - 360 degree range*/
        if ( azimuth >= 0 ) {
            if ( this.azimuthLimitCenter >= 0 ) {
                this.azimuthDouble = azimuth - this.azimuthLimitCenter;
            } else if ( azimuth >= this.azimuthMinimumValue && azimuth <= 180 ) {
                this.azimuthDouble = - 360 + azimuth - this.azimuthLimitCenter;
            } else if ( azimuth >= this.azimuthLimitCenter ) {
                this.azimuthDouble = azimuth - this.azimuthLimitCenter;
            }
        } else if ( this.azimuthLimitCenter >= 0 ) {
            if ( azimuth <= this.azimuthMinimumValue && azimuth >= - 180 ) {
                this.azimuthDouble = 360 + azimuth - this.azimuthLimitCenter;
            } else {
                this.azimuthDouble = azimuth - this.azimuthLimitCenter;
            }
        } else {
            this.azimuthDouble = azimuth - this.azimuthLimitCenter;
        }
        if ( this.azimuthDouble < 0 ) {
            this.azimuthDouble = 360 + this.azimuthDouble;
        }

        /*save also the integer version of the azimuth value*/
        this.azimuthInt = ( int ) this.azimuthDouble;

    }

    /*function used to get the double value of azimuth*/
    public double getAzimuthDouble ( ) {
        return this.azimuthDouble;
    }

    /*function used to get the integer value of azimuth*/
    public int getAzimuthInt ( ) {
        return this.azimuthInt;
    }

}