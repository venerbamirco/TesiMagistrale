package com.progetto.tesi.sensors.gamerotationvector_done;

public class ManagementRoll {

    /*variables to store the limit points of roll value*/
    private double rollLimitBottom;
    private double rollLimitCenter;
    private double rollLimitTop;
    private double rollMinimumValue;
    private double rollMaximumValue;

    /*variables to store the values of pitch*/
    private double rollDouble;
    private int rollInt;

    /*variable to store the calibrated value of roll*/
    private double rollCalibrateValue;

    /*constructor to initialize the manager of roll value*/
    public ManagementRoll ( ) {

        /*initialize all necessary variables*/
        this.initializeAllVariables ( );

    }

    /*function used to initialize all necessary variables*/
    private void initializeAllVariables ( ) {

        /*initialize the limit range of roll value*/
        this.rollLimitBottom = - 90;
        this.rollLimitCenter = 0;
        this.rollLimitTop = 90;

        /*initialize the limit top and bottom value of roll*/
        this.rollMinimumValue = - 90;
        this.rollMaximumValue = 90;

        /*initialize the roll values*/
        this.rollInt = 0;
        this.rollDouble = 0;

        /*initialize the calibrated value of roll*/
        this.rollCalibrateValue = 0;

    }

    /*function used to calibrate the roll values*/
    public void calibrateRoll ( double roll ) {

        /*save actual value of roll*/
        this.rollCalibrateValue = roll;

        /*save new range of roll values*/
        this.rollLimitBottom = this.rollCalibrateValue - 180;
        this.rollLimitCenter = this.rollCalibrateValue;
        this.rollLimitTop = this.rollCalibrateValue + 180;

        /*calculate new extreme range points for roll*/
        if ( this.rollLimitBottom < - 180 ) {
            this.rollMinimumValue = 360 - Math.abs ( this.rollLimitBottom );
            this.rollMaximumValue = 180 - Math.abs ( this.rollLimitCenter );
        } else if ( this.rollLimitTop >= 180 ) {
            this.rollMinimumValue = - 180 + Math.abs ( this.rollLimitCenter );
            this.rollMaximumValue = - 360 + Math.abs ( this.rollLimitTop );
        }

    }

    /*function used to filter the roll values*/
    public void filterRoll ( double roll ) {

        /*calculate the new value of roll in relation with the calibrated value using 0 - 360 degree range*/
        if ( roll >= 0 ) {
            if ( this.rollLimitCenter >= 0 ) {
                this.rollDouble = roll - this.rollLimitCenter;
            } else if ( roll >= this.rollMinimumValue && roll <= 180 ) {
                this.rollDouble = - 360 + roll - this.rollLimitCenter;
            } else if ( roll >= this.rollLimitCenter ) {
                this.rollDouble = roll - this.rollLimitCenter;
            }
        } else if ( this.rollLimitCenter >= 0 ) {
            if ( roll <= this.rollMinimumValue && roll >= - 180 ) {
                this.rollDouble = roll + 360 - this.rollLimitCenter;
            } else {
                this.rollDouble = roll - this.rollLimitCenter;
            }
        } else {
            this.rollDouble = roll - this.rollLimitCenter;
        }
        if ( this.rollDouble < 0 ) {
            this.rollDouble = 360 + this.rollDouble;
        }

        /*save also the integer version of the roll value*/
        this.rollInt = ( int ) this.rollDouble;

    }

    /*function used to get the double value of roll*/
    public double getRollDouble ( ) {
        return this.rollDouble;
    }

    /*function used to get the integer value of roll*/
    public int getRollInt ( ) {
        return this.rollInt;
    }
}