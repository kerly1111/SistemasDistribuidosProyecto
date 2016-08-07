package com.smarthome.aplicacion.smarthomeapk;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import com.smarthome.aplicacion.smarthomeapk.Preferencias.Preferences;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        SharedPreferences shpref = getSharedPreferences("web_service", Context.MODE_PRIVATE);
        String srtKey = shpref.getString("valor_generado","default");
        if (srtKey.equals("")){
            Intent intent = new Intent(this, LoginActivity.class);
            startActivity(intent);
        }else {

        }

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);





    }
}
