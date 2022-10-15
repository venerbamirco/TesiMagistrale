package com.progetto.tesi.applications.debuggable;

import static android.os.Debug.isDebuggerConnected;

import android.content.Context;
import android.content.pm.ApplicationInfo;
import android.content.pm.PackageManager;

import java.util.ArrayList;
import java.util.List;

// class used to get all installed application in android
public class DebuggableApplications extends Thread {

    // variable used to store the context to access inside the thread
    private Context context;

    // variable used to retrieve informations related to the application packages that are currently installed on the device
    private PackageManager packageManager;

    // variable used to store all debuggable applications
    private List<ApplicationInfo> debugabbleApplications;

    public DebuggableApplications(Context context) {

        // save the context
        this.context = context;

        // save the package manager
        this.packageManager = this.context.getPackageManager();

        // initialize the list to contain all debuggable applications
        this.debugabbleApplications = new ArrayList<>();

        // start thread
        this.start();

        // print debuggable applications information's
        this.printDebuggableApplicationsInfo();

    }

    // function used to print information's of debuggable applications
    public void printDebuggableApplicationsInfo() {

        try {

            // try to wait until the thread finish its execution
            this.join();

            // debug row
            System.out.println("----------DEBUGGABLE APPLICATIONS----------");

            // for each debuggable application
            for (ApplicationInfo app : this.debugabbleApplications) {

                // print app information's
                System.out.println(this.packageManager.getApplicationLabel(app));
                System.out.println(isDebuggerConnected());
                System.out.println(isDebuggerConnected());

            }

        } catch (InterruptedException e) {
            e.printStackTrace();
        }

    }

    @Override
    public void run() {

        // get list of all applications inside the device
        List<ApplicationInfo> allApps = this.packageManager.getInstalledApplications(PackageManager.GET_META_DATA);

        // for each application
        for (ApplicationInfo app : allApps) {

            // if it a system application
            if ((app.flags & (ApplicationInfo.FLAG_UPDATED_SYSTEM_APP | ApplicationInfo.FLAG_SYSTEM)) > 0) {

                // do nothing for the moment

            }

            // if it is a user application
            else {

                // if it is a debuggable application
                if ((app.flags & ApplicationInfo.FLAG_DEBUGGABLE) > 0) {

                    // add to the list the current application
                    debugabbleApplications.add(app);

                }

            }

        }

    }

}
