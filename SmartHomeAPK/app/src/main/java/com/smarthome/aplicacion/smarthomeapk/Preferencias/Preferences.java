package com.smarthome.aplicacion.smarthomeapk.Preferencias;

import android.content.Context;
import android.content.SharedPreferences;

/**
 * Created by ferna on 06/08/2016.
 */
public class Preferences {
    Context context;

    public Preferences(Context context) {
        this.context = context;
    }

    public void saveKey(String key) {
        SharedPreferences.Editor editor = this.context.getSharedPreferences("web_service", Context.MODE_PRIVATE).edit();
        editor.putString("valor_generado", key);
        editor.commit();
    }

    public String getKey() {
        SharedPreferences preferences = context.getSharedPreferences("web_service", Context.MODE_PRIVATE);
        return preferences.getString("valor_generado", "default");
    }
}
