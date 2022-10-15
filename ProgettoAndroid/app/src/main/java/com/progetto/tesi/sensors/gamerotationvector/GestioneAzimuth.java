package com.progetto.tesi.sensors.gamerotationvector;

public class GestioneAzimuth {

    private double azimuthLimitBottom = -180;
    private double azimuthLimitCenter = 0;
    private double azimuthLimitTop = 180;

    private double azimuthValoreMinimo = -180;
    private double azimuthValoreMassimo = 180;

    private double azimuthDouble = 0;
    private int azimuthInt;

    private double azimuthCalibra = 0;

    public GestioneAzimuth() {

    }

    public void calibraAzimuth(double azimuth) {
        this.azimuthCalibra = azimuth;

        this.azimuthLimitBottom = this.azimuthCalibra - 180;
        this.azimuthLimitCenter = this.azimuthCalibra;
        this.azimuthLimitTop = this.azimuthCalibra + 180;

        if (this.azimuthLimitBottom < -180) {
            this.azimuthValoreMinimo = 360 - Math.abs(this.azimuthLimitBottom);
            this.azimuthValoreMassimo = 180 - Math.abs(this.azimuthLimitCenter);
        } else if (this.azimuthLimitTop >= 180) {
            this.azimuthValoreMinimo = -180 + Math.abs(this.azimuthLimitCenter);
            this.azimuthValoreMassimo = -360 + Math.abs(this.azimuthLimitTop);
        }
    }

    public void filtraAzimuth(double azimuth) {
        if (azimuth >= 0) {
            if (this.azimuthLimitCenter >= 0) {
                this.azimuthDouble = azimuth - this.azimuthLimitCenter;
            } else if (azimuth >= this.azimuthValoreMinimo && azimuth <= 180) {
                this.azimuthDouble = -360 + azimuth - this.azimuthLimitCenter;
            } else if (azimuth >= this.azimuthLimitCenter) {
                this.azimuthDouble = azimuth - this.azimuthLimitCenter;
            }
        } else if (this.azimuthLimitCenter >= 0) {
            if (azimuth <= this.azimuthValoreMinimo && azimuth >= -180) {
                this.azimuthDouble = 360 + azimuth - this.azimuthLimitCenter;
            } else {
                this.azimuthDouble = azimuth - this.azimuthLimitCenter;
            }
        } else {
            this.azimuthDouble = azimuth - this.azimuthLimitCenter;
        }
        if (this.azimuthDouble < 0) {
            this.azimuthDouble = 360 + this.azimuthDouble;
        }
        this.azimuthInt = (int) this.azimuthDouble;
    }

    public double getAzimuthDouble() {
        if (this.azimuthDouble < -180) {
            return -180;
        } else if (this.azimuthDouble > 180) {
            return 180;
        } else {
            return this.azimuthDouble;
        }
    }

    public int getAzimuthInt() {
        return this.azimuthInt;
    }

}