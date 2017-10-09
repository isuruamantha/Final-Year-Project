package rapticon.com.rememb.util;

/**
 * *   *  Created by Tharindu on 3/14/2017.
 */

public enum RecycleAdapterElement {

    CAT(0);

    private int type;

    RecycleAdapterElement(int type) {
        this.type = type;
    }

    /**
     * Gets type
     *
     * @return value of type
     */
    public int getType() {
        return type;
    }
}
