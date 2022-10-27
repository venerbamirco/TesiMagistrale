package com.progetto.tesi.debugger.detected;

import android.os.Bundle;

import androidx.appcompat.app.AppCompatActivity;

import com.progetto.tesi.R;

/*activity to show that a gnu debugger is attached*/
public class GnuDebugger_GDB_Activity extends AppCompatActivity {

    @Override
    protected void onCreate ( Bundle savedInstanceState ) {
        super.onCreate ( savedInstanceState );
        setContentView ( R.layout.activity_gnu_debugger_gdb );
    }
}