package it.matteodegiorgi.audiorecorder;

import static android.Manifest.permission.RECORD_AUDIO;
import static android.Manifest.permission.WRITE_EXTERNAL_STORAGE;

import android.app.AlertDialog;
import android.content.pm.PackageManager;
import android.media.MediaPlayer;
import android.media.MediaRecorder;
import android.os.Bundle;
import android.util.Log;
import android.view.Gravity;
import android.view.View;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;

import java.io.File;
import java.io.IOException;

import it.matteodegiorgi.audiorecorder.settings.Settings;

public class MainActivity extends AppCompatActivity {

    private TextView startTV, stopTV, playTV, stopplayTV, statusTV;
    private MediaRecorder mRecorder;
    private MediaPlayer mPlayer;
    private static File recording;
    public static final int REQUEST_AUDIO_PERMISSION_CODE = 1;

    /*variable for the data management class object*/
    DataManagement dataManagement;

    @Override
    protected void onCreate ( Bundle savedInstanceState ) {
        super.onCreate ( savedInstanceState );

        audioRecorder ( );

        /*initialize all necessary variables*/
        this.initializeVariables ( );

    }

    /*-----------------------------------------------------CONFIGURATION-------------------------------------------------------*/

    /*function used to initialize all necessary variables*/
    private void initializeVariables ( ) {

        /*initialize the handler with the main looper*/
        //this.handler = new Handler ( Looper.getMainLooper ( ) );

        /*initialize the data management class object*/
        this.dataManagement = new DataManagement ( this );

    }

    @Override
    protected void onPause ( ) {
        super.onPause ( );

        /*if the data management object is created*/
        if ( this.dataManagement != null ) {

            /*call the onpause method*/
            this.dataManagement.onPause ( );

        }

    }

    @Override
    protected void onResume ( ) {
        super.onResume ( );

        /*if the data management object is created*/
        if ( this.dataManagement != null ) {

            /*call the onresume method*/
            this.dataManagement.onResume ( );

        }

    }

    /*-----------------------------------------------------AUDIO RECORDER-------------------------------------------------------*/

    private void audioRecorder ( ) {
        setContentView ( R.layout.activity_main );

        statusTV = findViewById ( R.id.idTVstatus );
        startTV = findViewById ( R.id.btnRecord );
        stopTV = findViewById ( R.id.btnStop );
        playTV = findViewById ( R.id.btnPlay );
        stopplayTV = findViewById ( R.id.btnStopPlay );
        stopTV.setBackgroundColor ( getResources ( ).getColor ( R.color.gray ) );
        playTV.setBackgroundColor ( getResources ( ).getColor ( R.color.gray ) );
        stopplayTV.setBackgroundColor ( getResources ( ).getColor ( R.color.gray ) );

        startTV.setOnClickListener ( ( View v ) -> startRecording ( ) );
        stopTV.setOnClickListener ( ( View v ) -> pauseRecording ( ) );
        playTV.setOnClickListener ( ( View v ) -> playAudio ( ) );
        stopplayTV.setOnClickListener ( ( View v ) -> pausePlaying ( ) );
    }

    private void startRecording ( ) {
        if ( CheckPermissions ( ) ) {
            stopTV.setBackgroundColor ( getResources ( ).getColor ( R.color.purple_200 ) );
            startTV.setBackgroundColor ( getResources ( ).getColor ( R.color.gray ) );
            playTV.setBackgroundColor ( getResources ( ).getColor ( R.color.gray ) );
            stopplayTV.setBackgroundColor ( getResources ( ).getColor ( R.color.gray ) );
            recording = new File ( ContextCompat.getExternalFilesDirs ( getApplicationContext ( ) , "audio" )[ 0 ] , "/AudioRecording.3gp" );
            mRecorder = new MediaRecorder ( );
            mRecorder.setAudioSource ( MediaRecorder.AudioSource.MIC );
            mRecorder.setOutputFormat ( MediaRecorder.OutputFormat.THREE_GPP );
            mRecorder.setAudioEncoder ( MediaRecorder.AudioEncoder.AMR_NB );
            mRecorder.setOutputFile ( recording );
            try {
                mRecorder.prepare ( );
            } catch ( IOException e ) {
                Log.e ( "TAG" , "prepare() failed" );
            }
            mRecorder.start ( );
            statusTV.setText ( "Recording Started" );
        } else {
            RequestPermissions ( );
        }
    }

    @Override
    public void onRequestPermissionsResult ( int requestCode , String[] permissions , int[] grantResults ) {
        super.onRequestPermissionsResult ( requestCode , permissions , grantResults );
        switch ( requestCode ) {
            case REQUEST_AUDIO_PERMISSION_CODE:
                if ( grantResults.length > 0 ) {
                    boolean permissionToRecord = grantResults[ 0 ] == PackageManager.PERMISSION_GRANTED;
                    boolean permissionToStore = grantResults[ 1 ] == PackageManager.PERMISSION_GRANTED;
                    if ( permissionToRecord && permissionToStore ) {
                        Toast.makeText ( getApplicationContext ( ) , "Permission Granted" , Toast.LENGTH_LONG ).show ( );
                    } else {
                        Toast.makeText ( getApplicationContext ( ) , "Permission Denied" , Toast.LENGTH_LONG ).show ( );
                    }
                }
                break;
        }
    }

    public boolean CheckPermissions ( ) {
        int result = ContextCompat.checkSelfPermission ( getApplicationContext ( ) , WRITE_EXTERNAL_STORAGE );
        int result1 = ContextCompat.checkSelfPermission ( getApplicationContext ( ) , RECORD_AUDIO );
        return result == PackageManager.PERMISSION_GRANTED && result1 == PackageManager.PERMISSION_GRANTED;
    }

    private void RequestPermissions ( ) {
        ActivityCompat.requestPermissions ( MainActivity.this , new String[] { RECORD_AUDIO , WRITE_EXTERNAL_STORAGE } , REQUEST_AUDIO_PERMISSION_CODE );
    }


    public void playAudio ( ) {
        stopTV.setBackgroundColor ( getResources ( ).getColor ( R.color.gray ) );
        startTV.setBackgroundColor ( getResources ( ).getColor ( R.color.purple_200 ) );
        playTV.setBackgroundColor ( getResources ( ).getColor ( R.color.gray ) );
        stopplayTV.setBackgroundColor ( getResources ( ).getColor ( R.color.purple_200 ) );
        mPlayer = new MediaPlayer ( );
        try {
            mPlayer.setDataSource ( recording.getPath ( ) );
            mPlayer.prepare ( );
            mPlayer.start ( );
            statusTV.setText ( "Recording Started Playing" );
        } catch ( IOException e ) {
            Log.e ( "TAG" , "prepare() failed" );
        }
    }

    public void pauseRecording ( ) {
        stopTV.setBackgroundColor ( getResources ( ).getColor ( R.color.gray ) );
        startTV.setBackgroundColor ( getResources ( ).getColor ( R.color.purple_200 ) );
        playTV.setBackgroundColor ( getResources ( ).getColor ( R.color.purple_200 ) );
        stopplayTV.setBackgroundColor ( getResources ( ).getColor ( R.color.purple_200 ) );
        mRecorder.stop ( );
        mRecorder.release ( );
        mRecorder = null;
        statusTV.setText ( "Recording Stopped" );
    }

    public void pausePlaying ( ) {
        mPlayer.release ( );
        mPlayer = null;
        stopTV.setBackgroundColor ( getResources ( ).getColor ( R.color.gray ) );
        startTV.setBackgroundColor ( getResources ( ).getColor ( R.color.purple_200 ) );
        playTV.setBackgroundColor ( getResources ( ).getColor ( R.color.purple_200 ) );
        stopplayTV.setBackgroundColor ( getResources ( ).getColor ( R.color.gray ) );
        statusTV.setText ( "Recording Play Stopped" );
    }
}