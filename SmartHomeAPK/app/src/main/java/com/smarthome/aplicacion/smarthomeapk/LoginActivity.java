package com.smarthome.aplicacion.smarthomeapk;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.AsyncTask;
import android.preference.PreferenceManager;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.Toast;

import com.google.gson.Gson;
import com.smarthome.aplicacion.smarthomeapk.Preferencias.Preferences;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;

public class LoginActivity extends AppCompatActivity {

    private EditText txtUsuario;
    private EditText txtPass;
    private Button btnEntrar;
    private ImageView imLogo;
    private LoginTask loginTask;



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        txtUsuario = (EditText) findViewById(R.id.txtUsuario);
        txtPass = (EditText) findViewById(R.id.txtPass);
        btnEntrar = (Button) findViewById(R.id.btnEntrar);
        imLogo = (ImageView) findViewById(R.id.imageView);
        btnEntrar.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String srtUser = txtUsuario.getText().toString();
                String srtPass = txtPass.getText().toString();

                loginTask = new LoginTask(srtUser, srtPass);
                loginTask.execute((Void) null);
            }
        });
    }


    public class LoginTask extends AsyncTask<Void, Void, String> {
        private final String ltUsuario;
        private final String ltPass;

        LoginTask(String ltUsuario, String ltPass) {
            this.ltUsuario = ltUsuario;
            this.ltPass = ltPass;
        }

        protected String doInBackground(Void... params) {
            String data = "";
            URL url = null;

            try {
                SharedPreferences shpref = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
                String strURL = shpref.getString("key_servidor", getApplicationContext().getString(R.string.direccionServidor));
                url = new URL(strURL + "/rest-auth/login/");
            } catch (MalformedURLException e) {
                e.printStackTrace();
            }

            try {
                HttpURLConnection urlConn = (HttpURLConnection) url.openConnection();

                urlConn.setRequestMethod("POST");
                urlConn.setRequestProperty("USER-AGENT", "Mozilla/5.0");
                urlConn.setRequestProperty("ACCEPT-LANGUAGE", "en-US,en;0.5");
                urlConn.setDoOutput(true);

                DataOutputStream dOS = new DataOutputStream(urlConn.getOutputStream());
                dOS.writeBytes("username=" + ltUsuario + "&password=" + ltPass);
                dOS.flush();
                dOS.close();

                int codeHTTP = urlConn.getResponseCode();

                switch (codeHTTP){
                    case 200:
                        BufferedReader bReader = new BufferedReader(new InputStreamReader(urlConn.getInputStream()));
                        String line = "";
                        StringBuilder response = new StringBuilder();
                        while ((line = bReader.readLine())!=null){
                            response.append(line);
                        }
                        bReader.close();

                        data = response.toString();
                        Log.d(LoginActivity.class.getSimpleName(), "data: "+ data);
                        break;
                    default:
                        Toast.makeText(getApplicationContext(), "responseCode" + codeHTTP, Toast.LENGTH_SHORT).show();
                }


            } catch (IOException e) {
                e.printStackTrace();
            }
            return data;
        }

        protected void onPostExecute(final String succes){
            loginTask = null;
            if (succes.isEmpty()){

            }else{
                Gson gson = new Gson();
                Token token = gson.fromJson(succes, Token.class);
                Log.d(LoginActivity.class.getSimpleName(), "token.getKey: "+ token.getKey());
                Preferences pref = new Preferences(getApplicationContext());
                pref.saveKey(token.getKey());

                startActivity(new Intent(getApplicationContext(), MainActivity.class));
            }
        }

    }

}
