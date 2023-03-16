import java.io.File;
import java.util.*;

public class ex5 {
    static HashMap<String, Integer> nums = new HashMap<>();

    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(new File("numbers.txt"));
        while(sc.hasNext()){
            int n = sc.nextInt();
            sc.next();
            String s = sc.next();
            nums.put(s, n);
        }

        Scanner in = new Scanner(System.in);
        in.useDelimiter("[ \\-\\n]");
        int ret = 0;
        Integer acc = null;
        while( in.hasNext() ) {
            String word = in.next();
            if( nums.containsKey(word) ) {
                int a = nums.get(word);
                if( acc==null ) acc = a;
                else if( a>acc ) acc *= a;
                else {
                    ret += acc;
                    acc = a;
                }
            }
        }
        
        ret += acc;
        System.out.printf("Result: %d\n", ret);
        
        sc.close();
        in.close();
    }
}
    
   