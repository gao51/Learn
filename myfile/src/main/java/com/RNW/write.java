package com.RNW;

import java.io.*;

/**
 * Created by gaozhh on 2017/3/24.
 */
public class write {
    public  void writer(String filename,String  temp) throws IOException {
        File file = new File(filename);
        FileInputStream fip = new FileInputStream(file);
        InputStreamReader reader = new InputStreamReader(fip,"UTF-8");
        FileWriter fw =null;
        fw = new FileWriter(file ,true);
        PrintWriter pw = new PrintWriter(fw);
        pw.append(temp+"\r\n");
        pw.close();
        fw.close();
    }
}
