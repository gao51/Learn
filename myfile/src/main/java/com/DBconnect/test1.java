package com.DBconnect;

import java.sql.*;

/**
 * Created by gaozhh on 2017/4/1.
 */
public class test1 extends connect{

    public String test(String sql){
        Connection conn = null;
        Statement stmt = null;
        try{

            Class.forName("com.mysql.jdbc.Driver");



            conn = DriverManager.getConnection(DB_URL,USER,PASS);

            stmt = conn.createStatement();

            ResultSet rs = stmt.executeQuery(sql);

            while(rs.next()){


                user_id = rs.getString("user_id");
                name = rs.getString("name");

                result = "user_id:"+user_id+",name:"+name;
            }
            // 完成后关闭
            rs.close();
            stmt.close();
            conn.close();
        }catch(SQLException se){
            // 处理 JDBC 错误
            se.printStackTrace();
        }catch(Exception e){
            // 处理 Class.forName 错误
            e.printStackTrace();
        }finally{
            // 关闭资源
            try{
                if(stmt!=null) stmt.close();
            }catch(SQLException se2){
            }// 什么都不做
            try{
                if(conn!=null) conn.close();
            }catch(SQLException se){
                se.printStackTrace();
            }
        }
        return result;
    }


}
