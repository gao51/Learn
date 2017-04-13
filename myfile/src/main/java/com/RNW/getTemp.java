package com.RNW;

import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * Created by gaozhh on 2017/3/24.
 */
public class getTemp {

    public String getTemp(String temp){
      //  public static void main(String[] args) {
            String tem = null;
            String s = temp;
            Pattern p = Pattern.compile("requestId.*bankAccount");
            Matcher m = p.matcher(s);
            List<String> result=new ArrayList<String>();
            while(m.find()){
                result.add(m.group());
            }
            for(String s1:result){
                tem = s1;

                        tem = tem.replace("requestId\":\"","'");
                        tem = tem .replace("\",\"bankAccount","',");
                // System.out.println(s1+"s1");
            }

        return tem;
    }

}

