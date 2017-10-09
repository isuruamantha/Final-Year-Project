package rapticon.com.rememb.helper;


import android.app.Activity;
import android.os.AsyncTask;

import org.json.JSONException;

import java.io.IOException;


public class AsyncTaskHelper extends AsyncTask<String, Void, Integer> {

    private OnBackgroundTaskListener mOnBackgroundTaskListener;
    private Activity mActivity;
    // private ProgressDialogHelper progressDialogHelper;

    public AsyncTaskHelper(Activity mActivity) {
        this.mActivity = mActivity;
    }

    /**
     * set loading text
     *
     * @param text dialog label
     */
    public void setProgressDialogText(String text) {

        /*if (progressDialogHelper != null) {
            //  progressDialogHelper.setText(text);
        }*/

    }

    /**
     * @param listener
     */
    public void setOnBackgroundListener(OnBackgroundTaskListener listener) {
        this.mOnBackgroundTaskListener = listener;
    }

    @Override
    protected void onPreExecute() {
        super.onPreExecute();
        //  progressDialogHelper.showDialog();
        mOnBackgroundTaskListener.onPreExecute();
    }

    @Override
    protected void onPostExecute(Integer integer) {
        super.onPostExecute(integer);


//        if (integer == com.fg.vogue.util.ServiceStatus.OK.getStatus()) {
//
//            mOnBackgroundTaskListener.onPostExecute();
//
//        } else if (integer == com.fg.vogue.util.ServiceStatus.JSON_EXCEPTION.getStatus()) {
//
//        } else if (integer == com.fg.vogue.util.ServiceStatus.NULL_EX.getStatus()) {
//
//        } else if (integer == com.fg.vogue.util.ServiceStatus.SERVICE_DOWN.getStatus()) {
//
//        } else if (integer == com.fg.vogue.util.ServiceStatus.NO_INTERNET.getStatus()) {
//
//        } else {
//
//        }


    }

    @Override
    protected Integer doInBackground(String... strings) {
//        try {
//
//            mOnBackgroundTaskListener.onBackground(strings);
//
//            return com.fg.vogue.util.ServiceStatus.OK.getStatus();
//        } catch (JSONException jsonEx) {
//            Log.e("JSON_EXCEPTION", jsonEx.toString());
//            return com.fg.vogue.util.ServiceStatus.JSON_EXCEPTION.getStatus();
//        } catch (ServiceUnreachableException noServiceEx) {
//            Log.e("ServiceException", noServiceEx.toString());
//            return com.fg.vogue.util.ServiceStatus.SERVICE_DOWN.getStatus();
//        } catch (NoInternetException nulEx) {
//            Log.e("NoInternetException", nulEx.toString());
//            return com.fg.vogue.util.ServiceStatus.NO_INTERNET.getStatus();
//        } catch (IOException ioEx) {
//            Log.e("IOException", ioEx.toString());
//            return com.fg.vogue.util.ServiceStatus.IO_EXCEPTION.getStatus();
//        }
        return null;
    }

    public interface OnBackgroundTaskListener {

        void onBackground(String... strings) throws IOException, JSONException;

        void onPreExecute();

        void onPostExecute();
    }
}
