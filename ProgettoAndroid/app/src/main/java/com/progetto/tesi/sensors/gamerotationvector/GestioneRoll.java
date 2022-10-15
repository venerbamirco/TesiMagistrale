package com.progetto.tesi.sensors.gamerotationvector;

public class GestioneRoll {

    private double rollLimitBottom = -90;
    private double rollLimitCenter = 0;
    private double rollLimitTop = 90;

    private double rollValoreMinimo = -90;
    private double rollValoreMassimo = 90;

    private double rollDouble = 0;
    private int rollInt;

    private double rollCalibra = 0;

    public GestioneRoll() {

    }

    public void calibraRoll(double roll) {
        this.rollCalibra = roll;
        this.rollLimitBottom = this.rollCalibra - 180;
        this.rollLimitCenter = this.rollCalibra;
        this.rollLimitTop = this.rollCalibra + 180;
        if (this.rollLimitBottom < -180) {
            this.rollValoreMinimo = 360 - Math.abs(this.rollLimitBottom);
            this.rollValoreMassimo = 180 - Math.abs(this.rollLimitCenter);
        } else if (this.rollLimitTop >= 180) {
            this.rollValoreMinimo = -180 + Math.abs(this.rollLimitCenter);
            this.rollValoreMassimo = -360 + Math.abs(this.rollLimitTop);
        }
    }

    public void filtraRoll(double roll) {
        if (roll >= 0) {
            if (this.rollLimitCenter >= 0) {
                this.rollDouble = roll - this.rollLimitCenter;
            } else if (roll >= this.rollValoreMinimo && roll <= 180) {
                this.rollDouble = -360 + roll - this.rollLimitCenter;
            } else if (roll >= this.rollLimitCenter) {
                this.rollDouble = roll - this.rollLimitCenter;
            }
        } else if (this.rollLimitCenter >= 0) {
            if (roll <= this.rollValoreMinimo && roll >= -180) {
                this.rollDouble = roll + 360 - this.rollLimitCenter;
            } else {
                this.rollDouble = roll - this.rollLimitCenter;
            }
        } else {
            this.rollDouble = roll - this.rollLimitCenter;
        }
        if (this.rollDouble < 0) {
            this.rollDouble = 360 + this.rollDouble;
        }
        this.rollInt = (int) this.rollDouble;
    }

    public double getRollDouble() {
        return this.rollDouble;
    }

    public int getRollInt() {
        return this.rollInt;
    }
}