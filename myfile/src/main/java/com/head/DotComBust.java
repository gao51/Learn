package com.head;

import java.util.ArrayList;
/**
 * Created by gao on 2017/4/12.
 */
public class DotComBust {
    private GameHelper helper = new GameHelper();
    private ArrayList<DotCom> dotcomlist = new ArrayList<DotCom>();
    private int numofGuesses =0 ;
    private void setUpGame(){
        DotCom one = new DotCom();
        one.setName("Pets.com");
        DotCom two = new DotCom();
        two.setName("eToys.com");
        DotCom three = new DotCom();
        three.setName("Go2.com");
        dotcomlist.add(one);
        dotcomlist.add(two);
        dotcomlist.add(three);

        System.out.println("Your goal is to sinx three dot coms.");
        System.out.println("pets.com,eToys.com,Go2.com");
        System.out.println("Try to sink them all in the fewest number of guess");

        for(DotCom dotcomtoset:dotcomlist){
            ArrayList<String> newLocation = helper.placeDotCom(3);
            dotcomtoset.setLocationCells(newLocation);
        }
    }
    private void startPlaying(){
        while(!dotcomlist.isEmpty()){
            String userGuess = helper.getUserInput("Enter a guess");
        }
        finishGame();
    }
    private void checkUserGuess(String userGuess){
        numofGuesses++;
        String result = "miss";

        for(DotCom dotComToTest:dotcomlist){
            result = dotComToTest.checkYourself(userGuess);
            if(result.equals("hit")){
                break;
            }
            if(result.equals("kill")){
                dotcomlist.remove(dotComToTest);
                break;
            }
        }
        System.out.println(result);
    }
    private void finishGame(){
        System.out.println("All Dot Coms are dead! Your");
        if(numofGuesses<=18){
            System.out.println("It only took you"+numofGuesses+"guesses");
            System.out.println("You got out before you option sank");
        }else {
            System.out.println("Took you long enough"+numofGuesses+"guesses");
            System.out.println("Fish are dancing with your option");
        }
    }


    public static void main(String[] args) {
        DotComBust game = new DotComBust();
        game.setUpGame();
        game.startPlaying();

    }
}
