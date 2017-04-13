package com.gao.test1;

import java.io.*;

/**
 * Created by gao on 2017/4/9.
 */
public class outfile {
    public static void main(String[] args) {
        File file = new File("G://test","test2.txt");
        try {
            FileInputStream in = new FileInputStream(file);
            byte[] bye = new byte[1024];
            int x= in.read(bye);
            System.out.println(new String(bye));
            in.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    };
}

