package com.progetto.tesi.debugger.detected;

import android.os.Bundle;

import androidx.appcompat.app.AppCompatActivity;

import com.progetto.tesi.R;

/*activity to show that a jdwp debugger is attached*/
public class JavaDebugWireProtocol_JDWP_Activity extends AppCompatActivity {

    @Override
    protected void onCreate ( Bundle savedInstanceState ) {
        super.onCreate ( savedInstanceState );
        setContentView ( R.layout.activity_java_debug_wire_protocol_jdwp );
    }
}