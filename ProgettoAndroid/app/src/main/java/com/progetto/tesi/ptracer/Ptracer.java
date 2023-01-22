package com.progetto.tesi.ptracer;

import android.util.Log;

import androidx.appcompat.app.AppCompatActivity;

import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;

public class Ptracer {


    /*public constructor*/
    public Ptracer ( AppCompatActivity appCompatActivity ) {

        String[] cmd = new String[]{"ls","-c", "pwd"};

        try {
            // These two lines are what we care about
            Process process = Runtime.getRuntime().exec(cmd);
            InputStream iStream = process.getInputStream();

            // This is how we check whether it works
            tryWriteProcessOutput(iStream);
        } catch (IOException e) {
            System.out.println ("@@@@" );
            e.printStackTrace();
        }

    }

    private void tryWriteProcessOutput(InputStream iStream) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader (iStream));

        String output = "";
        String line;

        try {
            while ((line = reader.readLine()) != null) {
                output += line + "\n";
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            reader.close();
        }

        System.out.println ("####" );
        System.out.println (output);
        System.out.println ("####" );
    }

}
