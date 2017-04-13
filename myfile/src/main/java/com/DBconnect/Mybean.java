package com.DBconnect;

/**
 * Created by gaozhh on 2017/4/1.
 */
import java.sql.*;

public class Mybean {
    private String url = "jdbc:mysql://localhost:3306/dbcon";
    Connection conn = null;
    PreparedStatement ps = null;
    ResultSet rs = null;

    public Mybean() {
        System.out.println("开始初始化 ");
        try {
            Class.forName("com.mysql.jdbc.Driver");
            conn = DriverManager.getConnection(url,"root","");
            System.out.println("初始化完成");
        } catch (Exception e) {
            System.out.println("初始化错误 ");
            e.printStackTrace();
        }
    }

    public ResultSet SelectBySQL(String SQLString) throws SQLException  {

        try {
            //conn = DriverManager.getConnection(url);
            System.out.println("conn");
            String QueryString = SQLString;
            System.out.println(QueryString);
            ps = conn.prepareStatement(QueryString);
            rs = ps.executeQuery();


        } catch (SQLException e) {
            System.out.println("Exception appear in  Select");
            e.printStackTrace();
            throw e;
        }


        return rs;
    }


    public String InsertBySQL(String SQLString)  {
        System.out.println("Entering  InsertBySQL()");

        String judgement = null;
        try{
            //conn = DriverManager.getConnection("url", "root","123456");
            String QueryString=SQLString;
            ps=conn.prepareStatement(QueryString);
            ps.executeUpdate();
            System.out.println("InsertString is "+QueryString);
        }catch(SQLException e){
            System.out.println("Exception appear in   InsertBySQL()"+e);
            e.printStackTrace();
            return judgement = "repeat";
        }
        finally{
            try {
                ps.close();
                //conn.close();
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
        System.out.println("Leaving  InsertBySQL()");
        return judgement = "success";
    }

    public String UpdateBySQL(String SQLString)  {
        System.out.println("Entering UserManDaoImpl.UpdateBySQL()");

        String judgement = null;
        try{
            //conn = DriverManager.getConnection("url", "root","");
            String QueryString=SQLString;
            ps=conn.prepareStatement(QueryString);
            ps.executeUpdate();
            System.out.println("UpdateString is "+QueryString);

        }catch(Exception e){
            System.out.println("Exception appear in  UserManDaoImpl.UpdateBySQL()"+e);
            e.printStackTrace();
            return judgement = "repeat";
        }

        System.out.println("Leaving UserManDaoImpl.UpdateBySQL()");
        return judgement = "success";
    }

    public String DeleteBySQL(String SQLString) {
        System.out.println("Entering DeleteBySQL()");

        String judgement = null;
        try{

            String QueryString=SQLString;
            ps=conn.prepareStatement(QueryString);
            int count=ps.executeUpdate();
            if(count==0){
                return judgement = "repeat";
            }
        }
        catch(SQLException e){
            System.out.println("Exception appear in  UserManDaoImpl.DeleteBySQL()"+e);
            e.printStackTrace();
            return judgement = "repeat";
        }

        System.out.println("Leaving UserManDaoImpl.DeleteBySQL()");
        return judgement = "success";
    }

    public void close(){

        try {
            rs.close();
            ps.close();
            conn.close();
        } catch (SQLException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }

}
