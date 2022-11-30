package com.progetto.tesi.recharge.detection;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.os.BatteryManager;

/*class used to receive all broadcast notifications from the battery manager*/
public class RechargeReceiver extends BroadcastReceiver {

    /*definition of useful variables for battery informations*/
    private int status;
    private int chargePlug;

    /*definitions of useful variables for all types of charging*/
    private boolean isCharging;
    private boolean usbCharge;
    private boolean acCharge;

    /*definitions of useful variables for all old types of charging*/
    private boolean oldIsCharging;
    private boolean oldUsbCharge;
    private boolean oldAcCharge;

    /*variable for counter number of misurations*/
    private int misurations;

    /*public constructor*/
    public RechargeReceiver ( ) {

        /*initialize all necessary variables*/
        this.initializeAllVariables ( );

    }

    /*function used to initialize all necessary variables*/
    private void initializeAllVariables ( ) {

        /*at beginning 0 misurations*/
        this.misurations = 0;

    }

    @Override
    public void onReceive ( Context context , Intent intent ) {

        /*get battery informations from the device*/
        this.status = intent.getIntExtra ( BatteryManager.EXTRA_STATUS , - 1 );
        this.isCharging = this.status == BatteryManager.BATTERY_STATUS_CHARGING || this.status == BatteryManager.BATTERY_STATUS_FULL;

        /*get all types of charging*/
        this.chargePlug = intent.getIntExtra ( BatteryManager.EXTRA_PLUGGED , - 1 );
        this.usbCharge = this.chargePlug == BatteryManager.BATTERY_PLUGGED_USB;
        this.acCharge = this.chargePlug == BatteryManager.BATTERY_PLUGGED_AC;

        /*if first time of check all types of charging*/
        if ( this.misurations == 0 ) {

            /*print debug row*/
            this.printDetailsRechargerTypes ( );

        }

        /*if not the first time*/
        else {

            /*if change at least one parameter*/
            if ( this.oldIsCharging != this.isCharging || this.oldAcCharge != this.acCharge || this.oldUsbCharge != this.usbCharge ) {

                /*print debug row*/
                this.printDetailsRechargerTypes ( );

            }
        }

        /*save actual values*/
        this.saveActualValues ( );

        /*increment number of misurations*/
        this.misurations++;

    }

    /*function used to print all details of all types of charging*/
    private void printDetailsRechargerTypes ( ) {

        /*print debug row*/
        System.out.println ( "UsbChecker: ischarg: " + this.isCharging + " usbcharg: " + this.usbCharge + " accharge: " + this.acCharge );

    }

    /*function used to save actual valus in old variables*/
    private void saveActualValues ( ) {

        /*save actual values*/
        this.oldIsCharging = this.isCharging;
        this.oldAcCharge = this.acCharge;
        this.oldUsbCharge = this.usbCharge;

    }

}
