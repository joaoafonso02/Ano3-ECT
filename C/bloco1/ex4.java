import java.util.Map;
import java.util.HashMap;
import java.util.Scanner;
import java.io.*;

public class ex4 {
    public static void main(String[] args) throws FileNotFoundException{
        Map<String, Integer> nums = new HashMap<>();
        Scanner sc = new Scanner(new File("numbers.txt"));
        while(sc.hasNext()){
            int n = sc.nextInt();
            sc.next();
            String s = sc.next();
            nums.put(s, n);
        }
        
        Scanner in = new Scanner(System.in);
        String input = in.nextLine();
        String[] words = input.split(" ");

        for(String s : words){
            if(nums.containsKey(s)) {
                System.out.print(nums.get(s) + " ");
            } else if(s.contains("-")) {
                String[] split = s.split("-");
                for(String ss : split){
                    if(nums.containsKey(ss))
                        System.out.print(nums.get(ss) + " ");
                    else
                        System.err.print(ss + " ");
                }   
            }    
            else
                System.err.print(s + " ");
            

        }
        in.close();
        sc.close();
    }
    
}
