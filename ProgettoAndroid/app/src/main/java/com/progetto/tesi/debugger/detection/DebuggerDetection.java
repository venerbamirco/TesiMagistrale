package com.progetto.tesi.debugger.detection;

import android.app.ActivityManager;
import android.app.ActivityManager.RunningAppProcessInfo;
import android.content.Context;

import androidx.appcompat.app.AppCompatActivity;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.List;

public class DebuggerDetection extends Thread {

    /*variable to save the reference of the main activity*/
    private AppCompatActivity appCompatActivity;

    /*variable used to access to the activity manager*/
    private ActivityManager activityManager;

    /*list used to save all running processes*/
    private List<RunningAppProcessInfo> listRunningProcesses;

    /*variable used to store the pid of this application*/
    private int pid = 0;

    /*variable used to store the tracer pid of this application*/
    private int tracerPid = 0;

    /*variable used to store the name of process that is attached to this application*/
    private String processAttached = "";

    public DebuggerDetection(AppCompatActivity appCompatActivity) {

        /*save the actual activity to access forward to its managers*/
        this.appCompatActivity = appCompatActivity;

        /*get the activity manager reference*/
        this.activityManager = (ActivityManager) this.appCompatActivity.getSystemService(Context.ACTIVITY_SERVICE);

        this.start();

    }


    @Override
    public void run() {

        /*obtain the list of running processes and find the actual pid*/
        this.getApplicationPid();

        /*while tracer pid is equal to zero -> not connected debugger*/
        while (this.tracerPid == 0) {

            /*recalculate the tracer pid*/
            this.readProcPidStatus();

            /*one analysis each 1 seconds*/
            try {
                this.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

        }

        /*now this applications has one process attached*/
        System.out.println("Process attached");

        /*get the name of attached process*/
        this.getNameProcessTracerPid();

    }

    /*function used to get the pid of this application*/
    private void getApplicationPid() {

        /*get the list of all running processes*/
        this.listRunningProcesses = this.activityManager.getRunningAppProcesses();

        /*for each process*/
        for (int i = 0; i < this.listRunningProcesses.size(); ++i) {

            /*if the actual process is this application*/
            if (this.listRunningProcesses.get(i).processName.equalsIgnoreCase("com.progetto.tesi")) {

                /*save the pid*/
                this.pid = this.listRunningProcesses.get(i).pid;

                /*break to not pass all running processes*/
                break;

            }

        }

    }

    /*function used to get the name of the process with pid=tracerpid*/
    private void getNameProcessTracerPid() {

        /*nothing to do because device requires root access to get the name of process with a specific pid*/

    }

    /*function used to read the proc/pid/status file*/
    private void readProcPidStatus() {

        /*create the buffer reader*/
        BufferedReader bufferedReader = null;

        try {

            /*current line in the file*/
            String currentLine;

            /*initialize the buffered reader*/
            bufferedReader = new BufferedReader(new FileReader("/proc/" + this.pid + "/status"));

            /*while there is one more line*/
            while ((currentLine = bufferedReader.readLine()) != null) {

                /*if the actual line is the line that contains the tracer pid*/
                if (currentLine.startsWith("TracerPid")) {

                    /*delete the tabulation from the string*/
                    currentLine = currentLine.replace("\t", "");

                    /*obtain the value of tracer pid from the last part of the actual row*/
                    this.tracerPid = Integer.parseInt(currentLine.split(":")[1]);

                    /*break to not pass all data in proc/pid/status file*/
                    break;
                }

            }

        } catch (IOException e) {

            /*print only the stack trace*/
            e.printStackTrace();

        } finally {

            try {

                /*if buffered reader is not null*/
                if (bufferedReader != null) {

                    /*close the buffered reader*/
                    bufferedReader.close();

                }

            } catch (IOException ex) {

                /*print only the stack trace*/
                ex.printStackTrace();

            }
        }

    }

}
