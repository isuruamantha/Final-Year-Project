package rapticon.com.rememb.util;

/**
 * *   *  Created by Tharindu on 1/24/2017.
 */

public enum ServiceURL {

    CATEGORY("maincat")
    ;

    private String url;

    ServiceURL(String url) {
        this.url = url;
    }

    /**
     * Gets url
     *
     * @return value of url
     */
    public String getUrl() {

        return "http://origin.adaderana.lk/app_services/androidV2/V2Test/android_news_service_main.php?q="+url;
    }
}
