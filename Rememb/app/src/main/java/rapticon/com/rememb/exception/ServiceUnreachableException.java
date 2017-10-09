package rapticon.com.rememb.exception;

import java.io.IOException;

/**
 * *   *  Created by Tharindu on 5/5/2016.
 */
public class ServiceUnreachableException extends IOException {

    public ServiceUnreachableException(String detailMessage) {
        super(detailMessage);
    }
}
