package com.progetto.tesi.sensors.gamerotationvector;

import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import com.progetto.tesi.R;

public class SensorListener implements SensorEventListener {

    /*enum used to get a visual text of the azimuth value*/
    private AppCompatActivity appCompatActivity;
    private TextView textView;

    /*variable used to contain the text that we want to show to see sensor values and sensor text values but actually not used*/
    private String textSensorListener;

    /*variables used to the azimuth management*/
    private GestioneAzimuth gestioneAzimuth;
    private AzimuthPitchRollTextValue azimuth;
    private double azimuthDouble;
    private int azimuthInt;

    /*variables used to the pitch management*/
    private GestionePitch gestionePitch;
    private AzimuthPitchRollTextValue pitch;
    private double pitchDouble;
    private int pitchInt;

    /*variables used to the roll management*/
    private GestioneRoll gestioneRoll;
    private AzimuthPitchRollTextValue roll;
    private double rollDouble;
    private int rollInt;

    /*variables to check the available and alert device angles*/
    private AzimuthPitchRollTextValue rememberAzimuth;
    private AzimuthPitchRollTextValue rememberPitch;
    private AzimuthPitchRollTextValue rememberRoll;

    /*variable to check if the first calibration is done*/
    private boolean firstCalibrationDone;

    /*variable used to say to the program when calibrate the sensor again*/
    private boolean calibrate;

    /*variable used to check if the sensors are stationary*/
    private boolean stationary;

    /*variable used to store the number of measurements*/
    private int numberMeasurements;

    /*constructor to initialize the sensor listener*/
    public SensorListener ( AppCompatActivity appCompatActivity ) {

        /*initialize all necessary variables*/
        this.initializeAllVariables ( appCompatActivity );

    }

    /*function used initialize all necessary variables*/
    private void initializeAllVariables ( AppCompatActivity appCompatActivity ) {

        /*save the actual activity to access forward to the layout object*/
        this.appCompatActivity = appCompatActivity;

        /*get the references of all necessary object in the activity layout*/
        this.textView = this.appCompatActivity.findViewById ( R.id.valori );

        /*initialize all azimuth values*/
        this.azimuthInt = 0;
        this.azimuthDouble = 0;

        /*initialize all pitch values*/
        this.pitchInt = 0;
        this.pitchDouble = 0;

        /*initialize all roll values*/
        this.rollInt = 0;
        this.rollDouble = 0;

        /*at the beginning the first calibration is not done*/
        this.firstCalibrationDone = false;

        /*at the beginning we don't calibrate because we wait the thread to start the calibration*/
        this.calibrate = false;

        /*at the beginning the sensor is not stationary*/
        this.stationary = false;

        /*at the beginning the number of measurements is equal to zero*/
        this.numberMeasurements = 0;

        /*create all object for the management of each part of the sensor data*/
        this.gestioneAzimuth = new GestioneAzimuth ( );
        this.gestionePitch = new GestionePitch ( );
        this.gestioneRoll = new GestioneRoll ( );

        /*initial calibration for the azimuth and roll*/
        this.gestioneAzimuth.calibraAzimuth ( 0 );
        this.gestioneRoll.calibrateRoll ( 0 );

    }

    /*when there is a new sensor measurement*/
    @Override
    public void onSensorChanged ( SensorEvent event ) {

        /*if and only if the first calibration is done*/
        if ( this.firstCalibrationDone ) {

            /*check if the data is for the game rotation vector sensor*/
            if ( event.sensor.getType ( ) == Sensor.TYPE_GAME_ROTATION_VECTOR ) {

                /*string to store and then show the sensor values*/
                this.textSensorListener = "";

                /*calculate the right values for azimuth pitch and roll*/
                this.calculateRightValuesAzimuthPitchRoll ( event );

                /*set the azimuth text value*/
                this.setAzimuthTextValue ( );

                /*set the pitch text value*/
                this.setPitchTextValue ( );

                /*set the roll text value*/
                this.setRollTextValue ( );

                /*set azimuth pitch and roll number and text values into text label*/
                this.setMeasurementIntoTextLabel ( );

                /*only if we have already at least one measurement and we don't calibrate the sensor*/
                if ( this.numberMeasurements > 0 && ! this.calibrate ) {

                    /*show details inside the text label if there are some alerts*/
                    this.setAlerts ( );

                    /*check if device is stationary or not*/
                    this.checkDeviceStationary ( );

                }

                /*update remember values for azimuth pitch and roll*/
                this.rememberAzimuthPitchRollTextValues ( );

                /*we can change the calibrate status if there was active*/
                this.calibrate = false;

                /*increment the number of measurements*/
                this.numberMeasurements++;

            }

        }

    }

    @Override
    public void onAccuracyChanged ( Sensor sensor , int accuracy ) {

        /*do nothing for the moment*/

    }

    /*function used to calculate the right values for azimuth pitch and roll*/
    private void calculateRightValuesAzimuthPitchRoll ( SensorEvent event ) {

        /*variables used to store temp value to do analysis*/
        float[] rotMatrix = new float[ 9 ];
        float[] rotVals = new float[ 3 ];

        /*get all necessary values from the sensor*/
        SensorManager.getRotationMatrixFromVector ( rotMatrix , event.values );
        SensorManager.remapCoordinateSystem ( rotMatrix , SensorManager.AXIS_X , SensorManager.AXIS_Y , rotMatrix );
        SensorManager.getOrientation ( rotMatrix , rotVals );

        /*transformation of radius values in degree values*/
        double azimuth = Math.toDegrees ( rotVals[ 0 ] );
        double pitch = Math.toDegrees ( rotVals[ 1 ] );
        double roll = Math.toDegrees ( rotVals[ 2 ] );

        /*if we must calibrate again the sensor*/
        if ( this.calibrate ) {

            /*calibrate azimuth and roll with actual values*/
            this.gestioneAzimuth.calibraAzimuth ( azimuth );
            this.gestioneRoll.calibrateRoll ( roll );

        }

        /*calculate the right value for azimuth using a 360 degrees value*/
        this.gestioneAzimuth.filtraAzimuth ( azimuth );
        this.azimuthDouble = this.gestioneAzimuth.getAzimuthDouble ( );
        this.azimuthInt = this.gestioneAzimuth.getAzimuthInt ( );

        /*calculate the right value for pitch using the standard values of the sensor*/
        this.gestionePitch.filtraPitch ( pitch );
        this.pitchDouble = this.gestionePitch.getPitchDouble ( );
        this.pitchInt = this.gestionePitch.getPitchInt ( );

        /*calculate the right value for roll using a 360 degrees value*/
        this.gestioneRoll.filterRoll ( roll );
        this.rollDouble = this.gestioneRoll.getRollDouble ( );
        this.rollInt = this.gestioneRoll.getRollInt ( );

    }

    /*function used to set the azimuth text value*/
    private void setAzimuthTextValue ( ) {

        /*transform actual azimuth value*/
        if ( this.azimuthInt > 315 || this.azimuthInt < 45 ) {
            this.azimuth = AzimuthPitchRollTextValue.NORTH;
        } else if ( this.azimuthInt > 45 && this.azimuthInt < 135 ) {
            this.azimuth = AzimuthPitchRollTextValue.EAST;
        } else if ( this.azimuthInt > 135 && this.azimuthInt < 225 ) {
            this.azimuth = AzimuthPitchRollTextValue.SOUTH;
        } else if ( this.azimuthInt > 225 && this.azimuthInt < 315 ) {
            this.azimuth = AzimuthPitchRollTextValue.WEST;
        } else if ( this.azimuthInt == 45 ) {
            this.azimuth = AzimuthPitchRollTextValue.NORTHEAST;
        } else if ( this.azimuthInt == 135 ) {
            this.azimuth = AzimuthPitchRollTextValue.SOUTHEAST;
        } else if ( this.azimuthInt == 225 ) {
            this.azimuth = AzimuthPitchRollTextValue.SOUTHWEST;
        } else if ( this.azimuthInt == 315 ) {
            this.azimuth = AzimuthPitchRollTextValue.NORTHWEST;
        }

    }

    /*function used to set the pitch text value*/
    private void setPitchTextValue ( ) {

        /*transform actual pitch value*/
        if ( this.pitchInt > - 90 && this.pitchInt < - 45 ) {
            if ( this.roll == AzimuthPitchRollTextValue.NORTH ) {
                this.pitch = AzimuthPitchRollTextValue.NORTH;
            } else if ( this.roll == AzimuthPitchRollTextValue.SOUTH ) {
                this.pitch = AzimuthPitchRollTextValue.NORTH;
            }
        } else if ( this.pitchInt > - 45 && this.pitchInt < 45 ) {
            if ( this.roll == AzimuthPitchRollTextValue.NORTH ) {
                this.pitch = AzimuthPitchRollTextValue.EAST;
            } else if ( this.roll == AzimuthPitchRollTextValue.SOUTH ) {
                this.pitch = AzimuthPitchRollTextValue.WEST;
            }
        } else if ( this.pitchInt > 45 && this.pitchInt < 90 ) {
            if ( this.roll == AzimuthPitchRollTextValue.NORTH ) {
                this.pitch = AzimuthPitchRollTextValue.SOUTH;
            } else if ( this.roll == AzimuthPitchRollTextValue.SOUTH ) {
                this.pitch = AzimuthPitchRollTextValue.SOUTH;
            }
        } else if ( this.pitchInt == - 45 ) {
            if ( this.roll == AzimuthPitchRollTextValue.NORTH ) {
                this.pitch = AzimuthPitchRollTextValue.NORTHEAST;
            } else if ( this.roll == AzimuthPitchRollTextValue.SOUTH ) {
                this.pitch = AzimuthPitchRollTextValue.NORTHWEST;
            }
        } else if ( this.pitchInt == 45 ) {
            if ( this.roll == AzimuthPitchRollTextValue.NORTH ) {
                this.pitch = AzimuthPitchRollTextValue.SOUTHEAST;
            } else if ( this.roll == AzimuthPitchRollTextValue.SOUTH ) {
                this.pitch = AzimuthPitchRollTextValue.SOUTHWEST;
            }
        }

    }

    /*function used to set the roll text value*/
    private void setRollTextValue ( ) {

        /*transform actual roll value*/
        if ( this.rollInt > 315 || this.rollInt < 45 ) {
            this.roll = AzimuthPitchRollTextValue.NORTH;
        } else if ( this.rollInt > 45 && this.rollInt < 135 ) {
            this.roll = AzimuthPitchRollTextValue.EAST;
        } else if ( this.rollInt > 135 && this.rollInt < 225 ) {
            this.roll = AzimuthPitchRollTextValue.SOUTH;
        } else if ( this.rollInt > 225 && this.rollInt < 315 ) {
            this.roll = AzimuthPitchRollTextValue.WEST;
        } else if ( this.rollInt == 45 ) {
            this.roll = AzimuthPitchRollTextValue.NORTHEAST;
        } else if ( this.rollInt == 135 ) {
            this.roll = AzimuthPitchRollTextValue.SOUTHEAST;
        } else if ( this.rollInt == 225 ) {
            this.roll = AzimuthPitchRollTextValue.SOUTHWEST;
        } else if ( this.rollInt == 315 ) {
            this.roll = AzimuthPitchRollTextValue.NORTHWEST;
        }

    }

    /*function used to set the measurements into the text label*/
    private void setMeasurementIntoTextLabel ( ) {

        /*initialize again the text label value*/
        this.textView.setText ( "" );

        /*put inside azimuth pitch and roll their number values*/
        this.textView.setText ( this.textView.getText ( ) + "\n\nNumber values" );
        this.textView.setText ( this.textView.getText ( ) + "\nAzimuth: " + this.azimuthInt );
        this.textView.setText ( this.textView.getText ( ) + "\nPitch: " + this.pitchInt );
        this.textView.setText ( this.textView.getText ( ) + "\nRoll: " + this.rollInt );

        /*put inside azimuth pitch and roll their text values*/
        this.textView.setText ( this.textView.getText ( ) + "\n\nText values" );
        this.textView.setText ( this.textView.getText ( ) + "\nAzimuth: " + this.azimuth );
        this.textView.setText ( this.textView.getText ( ) + "\nPitch: " + this.pitch );
        this.textView.setText ( this.textView.getText ( ) + "\nRoll: " + this.roll );

    }

    /*function used to remember the azimuth pitch and roll text values when the calibrate button is pressed*/
    private void rememberAzimuthPitchRollTextValues ( ) {

        /*save the actual azimuth pitch and roll text values*/
        this.rememberAzimuth = this.azimuth;
        this.rememberPitch = this.pitch;
        this.rememberRoll = this.roll;

    }

    /*function used to alert if some sensor values are suspicious*/
    private void setAlerts ( ) {

        /*boolean variables to detect where there is an alert*/
        boolean azimuthAlert = false;
        boolean pitchAlert = false;
        boolean rollAlert = false;

        /*alert on azimuth text value*/
        if ( this.azimuth == AzimuthPitchRollTextValue.SOUTH || this.azimuth == AzimuthPitchRollTextValue.SOUTHEAST || this.azimuth == AzimuthPitchRollTextValue.SOUTHWEST ) {
            azimuthAlert = true;
        }

        /*alert on pitch text value*/
        if ( this.rememberPitch == AzimuthPitchRollTextValue.NORTH || this.rememberPitch == AzimuthPitchRollTextValue.NORTHEAST || this.rememberPitch == AzimuthPitchRollTextValue.NORTHWEST ) {
            if ( this.pitch == AzimuthPitchRollTextValue.SOUTH ) {
                pitchAlert = true;
            }
        } else if ( this.rememberPitch == AzimuthPitchRollTextValue.EAST ) {
            if ( this.pitch == AzimuthPitchRollTextValue.WEST ) {
                pitchAlert = true;
            }
        } else if ( this.rememberPitch == AzimuthPitchRollTextValue.SOUTH || this.rememberPitch == AzimuthPitchRollTextValue.SOUTHEAST || this.rememberPitch == AzimuthPitchRollTextValue.SOUTHWEST ) {
            if ( this.pitch == AzimuthPitchRollTextValue.NORTH ) {
                pitchAlert = true;
            }
        } else if ( this.rememberPitch == AzimuthPitchRollTextValue.WEST ) {
            if ( this.pitch == AzimuthPitchRollTextValue.EAST ) {
                pitchAlert = true;
            }
        }

        /*alert on roll text value*/
        if ( this.roll == AzimuthPitchRollTextValue.SOUTH || this.roll == AzimuthPitchRollTextValue.SOUTHEAST || this.roll == AzimuthPitchRollTextValue.SOUTHWEST ) {
            rollAlert = true;
        }

        /*if there aren't alerts*/
        if ( ! azimuthAlert && ! pitchAlert && ! rollAlert ) {

            /*the device is correctly used*/
            this.textView.setText ( this.textView.getText ( ) + "\n\nDevice is correctly used" );

            /*debug row for device correctly used*/
            System.out.println ( "SensorListener: Device is correctly used" );

        }

        /*if there are one or more alerts*/
        else {

            /*debug row in the text label to make a list of alerts*/
            this.textView.setText ( this.textView.getText ( ) + "\n\nAlert:" );

        }

        /*if there is a azimuth alert*/
        if ( azimuthAlert ) {

            /*the device is wrongly directed*/
            this.textView.setText ( this.textView.getText ( ) + "\nWrongly directed" );

            /*debug row for azimuth alert*/
            System.out.println ( "SensorListener: Azimuth alert" );

        }

        /*if there is a pitch alert*/
        if ( pitchAlert ) {

            /*the device is wrongly inclined*/
            this.textView.setText ( this.textView.getText ( ) + "\nWrongly inclined" );

            /*debug row for pitch alert*/
            System.out.println ( "SensorListener: Pitch alert" );

        }

        /*if there is a pitch alert*/
        if ( rollAlert ) {

            /*the device is wrongly rotated*/
            this.textView.setText ( this.textView.getText ( ) + "\nWrongly rotated" );

            /*debug row for roll alert*/
            System.out.println ( "SensorListener: Roll alert" );

        }

    }

    /*function used to calibrated again all the sensors*/
    public void calibrateSensors ( ) {

        /*we must calibrate again the sensor*/
        this.calibrate = true;

    }

    /*function used to check if the device is stationary*/
    private void checkDeviceStationary ( ) {

        /*boolean variable to store if the device is stationary*/
        this.stationary = true;

        /*check azimuth stationary*/
        if ( this.azimuth != this.rememberAzimuth ) {

            /*not stationary*/
            this.stationary = false;

            /*debug row for azimuth change*/
            System.out.println ( "SensorListener: Azimuth change: " + this.rememberAzimuth + " -> " + this.azimuth );

        }

        /*check pitch stationary*/
        if ( this.pitch != this.rememberPitch ) {

            /*not stationary*/
            this.stationary = false;

            /*debug row for pitch change*/
            System.out.println ( "SensorListener: Pitch change: " + this.rememberPitch + " -> " + this.pitch );

        }

        /*check roll stationary*/
        if ( this.roll != this.rememberRoll ) {

            /*not stationary*/
            this.stationary = false;

            /*debug row for roll change*/
            System.out.println ( "SensorListener: Roll change: " + this.rememberRoll + " -> " + this.roll );

        }

        /*if device is stationary*/
        if ( this.stationary ) {

            /*nothing to do now*/

        }
        /*if device is not stationary*/
        else {

            /*nothing to do now*/

        }

    }

    /*function used to say that the first calibration of the device is done*/
    public void setFirstCalibrationDone ( ) {
        this.firstCalibrationDone = true;
    }

}