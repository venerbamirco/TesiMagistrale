package com.progetto.tesi.usb;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.os.BatteryManager;

public class UsbReceiver extends BroadcastReceiver {

    /*definition of useful variables for battery informations*/
    private int status;
    private int chargePlug;

    /*definitions of useful variables for all types of charging*/
    private boolean isCharging;
    private boolean usbCharge;
    private boolean acCharge;

    /*variable for counter number of misurations*/
    private int misurations;

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

            System.out.println ( "UsbChecker: ischarg: " + this.isCharging + " usbcharg: " + this.usbCharge + " accharge: " + this.acCharge );

            /*print all types of charging*/
            //Toast.makeText ( this.appCompatActivity.getApplicationContext () , "UsbChecker: ischarg: " + this.isCharging + " usbcharg: " + this.usbCharge + " accharge: " + this.acCharge , Toast.LENGTH_SHORT );

        }

        /*if not the first time*/
        else {

            System.out.println ( "UsbChecker: ischarg: " + this.isCharging + " usbcharg: " + this.usbCharge + " accharge: " + this.acCharge );

        }

        this.misurations++;


    }

}
