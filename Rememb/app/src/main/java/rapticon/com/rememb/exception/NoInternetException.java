package rapticon.com.rememb.exception;

import java.io.IOException;

/**
 * *   *  Created by Tharindu on 5/5/2016.
 */
public class NoInternetException extends IOException {

    public NoInternetException(String detailMessage) {
        super(detailMessage);
    }
}
