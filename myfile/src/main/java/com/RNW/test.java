package com.RNW;

/**
 * Created by gaozhh on 2017/3/24.
 */
public class test {
    public static void main(String[] args) {
        String Rfilename = "E:\\test\\test1.txt";
        String Wfilename = "E:\\test\\test3.txt";
        Read read = new Read();
        read.readFileByLines(Rfilename,Wfilename);
    }
}
