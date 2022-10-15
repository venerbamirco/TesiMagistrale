package com.progetto.tesi.sensors.gamerotationvector;

import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import com.progetto.tesi.R;

/*enum used to get a visual text of the azimuth value*/
enum Azimuth {
    NORTH, EAST, SOUTH, WEST, NORTHEAST, SOUTHEAST, SOUTHWEST, NORTHWEST
}

/*enum used to get a visual text of the roll value*/
enum Roll {
    NORTH, EAST, SOUTH, WEST, NORTHEAST, SOUTHEAST, SOUTHWEST, NORTHWEST
}

/*enum used to get a visual text of the pitch value thinking to incline device from the photo camera side*/
enum Pitch {
    NORTH, EAST, SOUTH, WEST, NORTHEAST, SOUTHEAST, SOUTHWEST, NORTHWEST
}

public class SensorListener implements SensorEventListener {

    /*enum used to get a visual text of the azimuth value*/
    private AppCompatActivity appCompatActivity = null;
    private TextView textView = null;

    /*variable used to contain the text that we want to show to see sensor values and sensor text values but actually not used*/
    private String string = null;

    /*variables used to the azimuth management*/
    private GestioneAzimuth gestioneAzimuth = null;
    private Azimuth azimuth = null;
    private double azimuthDouble = 0;
    private int azimuthInt = 0;

    /*variables used to the pitch management*/
    private GestionePitch gestionePitch = null;
    private Pitch pitch = null;
    private double pitchDouble = 0;
    private int pitchInt = 0;

    /*variables used to the roll management*/
    private GestioneRoll gestioneRoll = null;
    private Roll roll = null;
    private double rollDouble = 0;
    private int rollInt = 0;

    /*variables to check the available and alert device angles*/
    private Azimuth rememberAzimuth = null;
    private Pitch rememberPitch = null;
    private Roll rememberRoll = null;

    /*variable used to say to the program when calibrate the sensor again*/
    private boolean calibrate = false;

    /*variable used to check if the sensors are stationary*/
    private final boolean stationary = false;

    public SensorListener(AppCompatActivity appCompatActivity) {

        /*save the actual activity to access forward to the layout object*/
        this.appCompatActivity = appCompatActivity;

        /*get the references of all necessary object in the activity layout*/
        this.textView = this.appCompatActivity.findViewById(R.id.valori);

        /*create all object for the management of each part of the sensor data*/
        this.gestioneAzimuth = new GestioneAzimuth();
        this.gestionePitch = new GestionePitch();
        this.gestioneRoll = new GestioneRoll();

        /*initial calibration for the azimuth and roll*/
        this.gestioneAzimuth.calibraAzimuth(0);
        this.gestioneRoll.calibraRoll(0);

    }

    /*when there is a new sensor measurement*/
    @Override
    public void onSensorChanged(SensorEvent event) {

        /*check if the data is for the game rotation vector sensor*/
        if (event.sensor.getType() == Sensor.TYPE_GAME_ROTATION_VECTOR) {

            /**/
            this.string = "";

            /*calculate the right values for azimuth pitch and roll*/
            this.calculateRIghtValuesAzimuthPitchRoll(event);

            /*set the azimuth text value*/
            this.setAzimuthTextValue();

            /*set the pitch text value*/
            this.setPitchTextValue();

            /*set the roll text value*/
            this.setRollTextValue();

            /*set azimuth pitch and roll number and text values into text label*/
            this.setMeasurementIntoTextLabel();

            /*show details inside the text label if there are some alerts*/
            this.setAlerts();

        }

    }

    @Override
    public void onAccuracyChanged(Sensor sensor, int accuracy) {

    }

    /*function used to calculate the right values for azimuth pitch and roll*/
    private void calculateRIghtValuesAzimuthPitchRoll(SensorEvent event) {

        /*variables used to store temp value to do analysis*/
        float[] rotMatrix = new float[9];
        float[] rotVals = new float[3];

        /*get all necessary values from the sensor*/
        SensorManager.getRotationMatrixFromVector(rotMatrix, event.values);
        SensorManager.remapCoordinateSystem(rotMatrix, SensorManager.AXIS_X, SensorManager.AXIS_Y, rotMatrix);
        SensorManager.getOrientation(rotMatrix, rotVals);

        /*transformation of radius values in degree values*/
        double azimuth = Math.toDegrees(rotVals[0]);
        double pitch = Math.toDegrees(rotVals[1]);
        double roll = Math.toDegrees(rotVals[2]);

        /*if we must calibrate again the sensor*/
        if (this.calibrate) {

            /*save the azimuth pitch and roll text values*/
            this.rememberAzimuthPitchRollTextValues();

            /*calibrate azimuth and roll with actual values*/
            this.gestioneAzimuth.calibraAzimuth(azimuth);
            this.gestioneRoll.calibraRoll(roll);

            /*calibration is done*/
            this.calibrate = false;

        }

        /*calculate the right value for azimuth using a 360 degrees value*/
        this.gestioneAzimuth.filtraAzimuth(azimuth);
        this.azimuthDouble = this.gestioneAzimuth.getAzimuthDouble();
        this.azimuthInt = this.gestioneAzimuth.getAzimuthInt();

        /*calculate the right value for pitch using the standard values of the sensor*/
        this.gestionePitch.filtraPitch(pitch);
        this.pitchDouble = this.gestionePitch.getPitchDouble();
        this.pitchInt = this.gestionePitch.getPitchInt();

        /*calculate the right value for roll using a 360 degrees value*/
        this.gestioneRoll.filtraRoll(roll);
        this.rollDouble = this.gestioneRoll.getRollDouble();
        this.rollInt = this.gestioneRoll.getRollInt();

    }

    /*function used to set the azimuth text value*/
    private void setAzimuthTextValue() {

        /*transform actual azimuth value*/
        if (this.azimuthInt > 315 || this.azimuthInt < 45) {
            this.azimuth = Azimuth.NORTH;
        } else if (this.azimuthInt > 45 && this.azimuthInt < 135) {
            this.azimuth = Azimuth.EAST;
        } else if (this.azimuthInt > 135 && this.azimuthInt < 225) {
            this.azimuth = Azimuth.SOUTH;
        } else if (this.azimuthInt > 225 && this.azimuthInt < 315) {
            this.azimuth = Azimuth.WEST;
        } else if (this.azimuthInt == 45) {
            this.azimuth = Azimuth.NORTHEAST;
        } else if (this.azimuthInt == 135) {
            this.azimuth = Azimuth.SOUTHEAST;
        } else if (this.azimuthInt == 225) {
            this.azimuth = Azimuth.SOUTHWEST;
        } else if (this.azimuthInt == 315) {
            this.azimuth = Azimuth.NORTHWEST;
        }

    }

    /*function used to set the pitch text value*/
    private void setPitchTextValue() {

        /*transform actual pitch value*/
        if (this.pitchInt > -90 && this.pitchInt < -45) {
            if (this.roll == Roll.NORTH) {
                this.pitch = Pitch.NORTH;
            } else if (this.roll == Roll.SOUTH) {
                this.pitch = Pitch.NORTH;
            }
        } else if (this.pitchInt > -45 && this.pitchInt < 45) {
            if (this.roll == Roll.NORTH) {
                this.pitch = Pitch.EAST;
            } else if (this.roll == Roll.SOUTH) {
                this.pitch = Pitch.WEST;
            }
        } else if (this.pitchInt > 45 && this.pitchInt < 90) {
            if (this.roll == Roll.NORTH) {
                this.pitch = Pitch.SOUTH;
            } else if (this.roll == Roll.SOUTH) {
                this.pitch = Pitch.SOUTH;
            }
        } else if (this.pitchInt == -45) {
            if (this.roll == Roll.NORTH) {
                this.pitch = Pitch.NORTHEAST;
            } else if (this.roll == Roll.SOUTH) {
                this.pitch = Pitch.NORTHWEST;
            }
        } else if (this.pitchInt == 45) {
            if (this.roll == Roll.NORTH) {
                this.pitch = Pitch.SOUTHEAST;
            } else if (this.roll == Roll.SOUTH) {
                this.pitch = Pitch.SOUTHWEST;
            }
        }

    }

    /*function used to set the roll text value*/
    private void setRollTextValue() {

        /*transform actual roll value*/
        if (this.rollInt > 315 || this.rollInt < 45) {
            this.roll = Roll.NORTH;
        } else if (this.rollInt > 45 && this.rollInt < 135) {
            this.roll = Roll.EAST;
        } else if (this.rollInt > 135 && this.rollInt < 225) {
            this.roll = Roll.SOUTH;
        } else if (this.rollInt > 225 && this.rollInt < 315) {
            this.roll = Roll.WEST;
        } else if (this.rollInt == 45) {
            this.roll = Roll.NORTHEAST;
        } else if (this.rollInt == 135) {
            this.roll = Roll.SOUTHEAST;
        } else if (this.rollInt == 225) {
            this.roll = Roll.SOUTHWEST;
        } else if (this.rollInt == 315) {
            this.roll = Roll.NORTHWEST;
        }

    }

    /*function used to set the measurements into the text label*/
    private void setMeasurementIntoTextLabel() {

        /*initialize again the text label value*/
        this.textView.setText("");

        /*put inside azimuth pitch and roll their number values*/
        this.textView.setText(this.textView.getText() + "\n\nNumber values");
        this.textView.setText(this.textView.getText() + "\nAzimuth: " + this.azimuthInt);
        this.textView.setText(this.textView.getText() + "\nPitch: " + this.pitchInt);
        this.textView.setText(this.textView.getText() + "\nRoll: " + this.rollInt);

        /*put inside azimuth pitch and roll their text values*/
        this.textView.setText(this.textView.getText() + "\n\nText values");
        this.textView.setText(this.textView.getText() + "\nAzimuth: " + this.azimuth);
        this.textView.setText(this.textView.getText() + "\nPitch: " + this.pitch);
        this.textView.setText(this.textView.getText() + "\nRoll: " + this.roll);

    }

    /*function used to remember the azimuth pitch and roll text values when the calibrate button is pressed*/
    private void rememberAzimuthPitchRollTextValues() {

        /*save the actual azimuth pitch and roll text values*/
        this.rememberAzimuth = this.azimuth;
        this.rememberPitch = this.pitch;
        this.rememberRoll = this.roll;

    }

    /*function used to alert if some sensor values are suspicious*/
    private void setAlerts() {

        /*boolean variables to detect where there is an alert*/
        boolean azimuthAlert = false;
        boolean pitchAlert = false;
        boolean rollAlert = false;

        /*alert on azimuth text value*/
        if (this.azimuth == Azimuth.SOUTH || this.azimuth == Azimuth.SOUTHEAST || this.azimuth == Azimuth.SOUTHWEST) {
            azimuthAlert = true;
        }

        /*alert on pitch text value*/
        if (this.rememberPitch == Pitch.NORTH || this.rememberPitch == Pitch.NORTHEAST || this.rememberPitch == Pitch.NORTHWEST) {
            if (this.pitch == Pitch.SOUTH) {
                pitchAlert = true;
            }
        } else if (this.rememberPitch == Pitch.EAST) {
            if (this.pitch == Pitch.WEST) {
                pitchAlert = true;
            }
        } else if (this.rememberPitch == Pitch.SOUTH || this.rememberPitch == Pitch.SOUTHEAST || this.rememberPitch == Pitch.SOUTHWEST) {
            if (this.pitch == Pitch.NORTH) {
                pitchAlert = true;
            }
        } else if (this.rememberPitch == Pitch.WEST) {
            if (this.pitch == Pitch.EAST) {
                pitchAlert = true;
            }
        }

        /*alert on roll text value*/
        if (this.roll == Roll.SOUTH || this.roll == Roll.SOUTHEAST || this.roll == Roll.SOUTHWEST) {
            rollAlert = true;
        }

        /*if there aren't alerts*/
        if (!azimuthAlert && !pitchAlert && !rollAlert) {

            /*the device is correctly used*/
            this.textView.setText(this.textView.getText() + "\n\nDevice is correctly used");

        }

        /*if there are one or more alerts*/
        else {

            /*debug row in the text label to make a list of alerts*/
            this.textView.setText(this.textView.getText() + "\n\nAlert:");

        }

        /*if there is a azimuth alert*/
        if (azimuthAlert) {

            /*the device is wrongly directed*/
            this.textView.setText(this.textView.getText() + "\nWrongly directed");

        }

        /*if there is a pitch alert*/
        if (pitchAlert) {

            /*the device is wrongly inclined*/
            this.textView.setText(this.textView.getText() + "\nWrongly inclined");

        }

        /*if there is a pitch alert*/
        if (rollAlert) {

            /*the device is wrongly rotated*/
            this.textView.setText(this.textView.getText() + "\nWrongly rotated");

        }

    }

    /*function used to calibrated again all the sensors*/
    public void calibrateSensors() {

        /*we must calibrate again the sensor*/
        this.calibrate = true;

    }

}