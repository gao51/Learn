package com.RNW;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

/**
 * Created by gaozhh on 2017/3/24.
 * 以行为单位读取文件
 */
public class Read {
    public static void readFileByLines(String RfileName,String Wfilename) {
        File file = new File(RfileName);
        BufferedReader reader = null;
        write write =new write();
        getTemp getTemp = new getTemp();
        try {
            //System.out.println("以行为单位读取文件内容，一次读一整行：");
            reader = new BufferedReader(new FileReader(file));
            String tempString = null;
            int line = 1;
            // 一次读入一行，直到读入null为文件结束
            while ((tempString = reader.readLine()) != null) {
                // 显示行号
                //System.out.println("line " + line + ": " + tempString);
                line++;


                write.writer(Wfilename,getTemp.getTemp(tempString));




            }
            reader.close();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (reader != null) {
                try {
                    reader.close();
                } catch (IOException e1) {
                }
            }
        }
    }
}
