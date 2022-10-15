package com.progetto.tesi.sensors.gamerotationvector;

public class GestionePitch {

    private double pitchDouble = 0;
    private int pitchInt;

    public GestionePitch() {

    }

    public void filtraPitch(double pitch) {
        this.pitchDouble = pitch;
        this.pitchInt = (int) this.pitchDouble;
    }

    public double getPitchDouble() {
        return this.pitchDouble;
    }

    public int getPitchInt() {
        return this.pitchInt;
    }
}