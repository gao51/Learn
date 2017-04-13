package com.DBconnect;

/**
 * Created by gaozhh on 2017/4/1.
 */
public class test2 {
    public static void main(String[] args) {
        test1 a = new test1();
        String result = a.test("SELECT * from t_user");
        System.out.println(result);
    }
}
