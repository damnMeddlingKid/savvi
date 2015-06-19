package savvi;

import android.os.AsyncTask;

import org.apache.http.HttpResponse;
import org.apache.http.HttpStatus;
import org.apache.http.StatusLine;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.DefaultHttpClient;
import org.json.JSONArray;

import java.io.ByteArrayOutputStream;
import java.io.IOException;

/**
 * Created by franklyn on 18/06/15.
 */
public final class Savvi {
    protected static final int SAVVI_PAGE_LIMIT = 100;
    //protected static final String SAVVI_HOST = "http://127.0.0.1:8000/";
    //need to use this address on the emulator to access the host loop back address
    protected static final String SAVVI_HOST = "http://10.0.2.2:8000/";

    private Savvi() {}

    private static String getJSONStringFromHost(String api) {
            String url = Savvi.SAVVI_HOST+api;
            HttpClient httpclient = new DefaultHttpClient();
            String JSONResponse = null;

            try {
                HttpResponse response = httpclient.execute(new HttpGet(url));
                StatusLine statusLine = response.getStatusLine();
                if (statusLine.getStatusCode() == HttpStatus.SC_OK) {
                    ByteArrayOutputStream out = new ByteArrayOutputStream();
                    response.getEntity().writeTo(out);
                    JSONResponse = out.toString();
                    out.close();
                } else {
                    response.getEntity().getContent().close();
                    throw new IOException(statusLine.getReasonPhrase());
                }
            } catch(IOException e) {
                e.printStackTrace();
            }

            return JSONResponse;
    }

    private static JSONArray getJSONFromHost(String api) {
        String JSONString = getJSONStringFromHost(api);
        JSONArray obj = null;

        try {
            obj = new JSONArray(JSONString);
        } catch(Exception e) {
            e.printStackTrace();
        }

        return obj;
    }

    public static void getAPIResponse(String api,CallBack<JSONArray> onComplete) {
        RetrieveJSONResponse jsonResponse = new RetrieveJSONResponse(onComplete);
        jsonResponse.execute(api);
    }

    static class RetrieveJSONResponse extends AsyncTask<String, Integer, JSONArray> {

        private CallBack<JSONArray> onComplete;

        public RetrieveJSONResponse(CallBack<JSONArray> onComplete) {
            this.onComplete = onComplete;
        }

        protected JSONArray doInBackground(String... urls) {
            JSONArray jsonArray = null;
            try {
                jsonArray = Savvi.getJSONFromHost(urls[0]);
            } catch (Exception e) {
                e.printStackTrace();
            }
            return jsonArray;
        }

        protected void onPostExecute(JSONArray jsonArray) {
            onComplete.call(jsonArray);
        }
    }
}
