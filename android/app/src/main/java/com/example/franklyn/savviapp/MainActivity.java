package com.example.franklyn.savviapp;

import android.os.Bundle;
import android.support.v7.app.ActionBarActivity;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.TextView;

import org.json.JSONArray;

import savvi.CallBack;
import savvi.Idea;


public class MainActivity extends ActionBarActivity {

    protected static Idea[] ideas;
    protected static int currentIdea=0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        Idea.getIdeasFrom(0, new CallBack<JSONArray>() {
            @Override
            public void call(JSONArray result) {
                ideas = Idea.getIdeasFromJSONArray(result);
                TextView ideaView = (TextView) findViewById(R.id.idea_view);
                ideaView.setText(ideas[0].content);
                currentIdea = ideas[ideas.length-1].id;
            }
        });
        setContentView(R.layout.activity_main);
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }
}
