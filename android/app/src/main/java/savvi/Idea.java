package savvi;

import org.apache.http.HttpResponse;
import org.apache.http.HttpStatus;
import org.apache.http.StatusLine;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.DefaultHttpClient;
import org.json.JSONArray;
import org.json.JSONObject;

import java.io.ByteArrayOutputStream;
import java.io.IOException;

/**
 * Created by franklyn on 18/06/15.
 */
public class Idea {

    public static final String IDEAS_FROM = "idea/ideas_from/";

    public int id;
    public String content;

    public Idea(int idea_id,String idea_content) {
        id = idea_id;
        content = idea_content;
    }

    public static Idea[] getIdeasFromJSONArray(JSONArray jsonArray) {
        Idea[] ideas = null;

        try {
            ideas = new Idea[jsonArray.length()];
            for(int i=0;i<jsonArray.length();i++) {
                JSONObject obj = (JSONObject)jsonArray.getJSONObject(i);
                JSONObject fields = obj.getJSONObject("fields");
                ideas[i] = new Idea(obj.getInt("pk"),fields.getString("content"));
            }
        } catch(Exception e) {
            e.printStackTrace();
        }

        return ideas;
    }

    public static void getIdeasFrom(int idea_id,CallBack<JSONArray> onComplete) {
        String api = IDEAS_FROM+idea_id+"/"+Savvi.SAVVI_PAGE_LIMIT;
        Savvi.getAPIResponse(api,onComplete);
    }
}
