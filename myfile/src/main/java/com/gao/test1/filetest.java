package com.gao.test1;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;

/**
 * Created by gao on 2017/4/9.
 */
public class filetest {
    public static void main(String[] args) throws IOException {
        File file = new File("G:\\test","test2.txt");
        FileOutputStream out  = new FileOutputStream(file);
        byte bye[] = "测试写入".getBytes();
        out.write(bye);

        out.close();
    }
}
