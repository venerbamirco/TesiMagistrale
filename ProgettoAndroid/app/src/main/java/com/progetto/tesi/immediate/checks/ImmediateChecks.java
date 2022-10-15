package com.progetto.tesi.immediate.checks;

import android.os.Build;

public class ImmediateChecks {

    // function used to check if a debugger is connected
    public static boolean checkDebuggerConnected() {
        return android.os.Debug.isDebuggerConnected();
    }

    // function used to check if the device is an emulator
    private static boolean checkBuildConfig() {
        return Build.MANUFACTURER.contains("Genymotion")
                || Build.MODEL.contains("google_sdk")
                || Build.MODEL.toLowerCase().contains("droid4x")
                || Build.MODEL.contains("Emulator")
                || Build.MODEL.contains("Android SDK built for x86")
                || Build.HARDWARE == "goldfish"
                || Build.HARDWARE == "vbox86"
                || Build.HARDWARE.toLowerCase().contains("nox")
                || Build.FINGERPRINT.startsWith("generic")
                || Build.PRODUCT == "sdk"
                || Build.PRODUCT == "google_sdk"
                || Build.PRODUCT == "sdk_x86"
                || Build.PRODUCT == "vbox86p"
                || Build.PRODUCT.toLowerCase().contains("nox")
                || Build.BOARD.toLowerCase().contains("nox")
                || (Build.BRAND.startsWith("generic") && Build.DEVICE.startsWith("generic"));
    }

}
