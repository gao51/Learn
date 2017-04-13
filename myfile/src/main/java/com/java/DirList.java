package com.java;

import java.io.File;

/**
 * Created by gaozhh on 2017/2/15.
 */
public class DirList {
    public static void main(String[] args) {
    DirList list = new DirList();
    list.cdDirectory("D:\\test");



    }
    public void Directory(String Filename){
        File f1 = new File(Filename);
        if (f1.isDirectory()) {
            System.out.println( "目录 " + Filename);
            String s[] = f1.list();
            for (int i=0; i < s.length; i++) {
                File f = new File(Filename + "/" + s[i]);
                if (f.isDirectory()) {
                    System.out.println(s[i] + " 是一个目录");
                } else {
                    System.out.println(s[i] + " 是一个文件");
                }
            }
        } else {
            System.out.println(Filename + " 不是一个目录");
        }

    }
    public void cdDirectory(String Filename){
        File f1 = new File(Filename);
        if (f1.isDirectory()) {
            System.out.println( "目录 " + Filename);
            String s[] = f1.list();
            for (int i=0; i < s.length; i++) {
                File f = new File(Filename + "/" + s[i]);
                System.out.println();
                if (f.isDirectory()) {
                    System.out.println(s[i] + " 是一个目录");
                    cdDirectory(Filename+"\\"+s[i]);
                } else {
                    System.out.println(s[i] + " 是一个文件");
                }
            }
        } else {
            System.out.println(Filename + " 不是一个目录");
        }
    }
}
