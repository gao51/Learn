package com.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * Created by gaozhh on 2017/2/15.
 */
public class BRRealLines {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader( new InputStreamReader(System.in));
        String str = null;
        System.out.println("Enter lines of text.");
        System.out.println("Enter 'end' to quit.");
        do{
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            System.out.println(str);
        }while(!str.equals("end"));
    }
}
