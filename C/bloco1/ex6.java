import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class ex6 {
    private static HashMap<String, String> dic;
    public static void main(String[] args) throws FileNotFoundException {
        dic = new HashMap<>();

        File dicFile = new File("dic1.txt");
        Scanner sc = new Scanner(dicFile);
        while( sc.hasNextLine() ) {
            String a = sc.next();
            String b = sc.nextLine();
            dic.put(a, b);
        }
        sc.close();

        Scanner in = new Scanner(System.in);
        String res = "";
        while( in.hasNext() ) {
            res += solve( in.next() ) + " ";
        }
        res = res.trim();
        System.out.println(res);

        in.close();
    }

    public static String solve(String a) {
        Scanner s = new Scanner(a);
        String res = "";
        while( s.hasNext() ) {
            String b = s.next();
            if( dic.containsKey(b) ) res += solve(dic.get(b)) + " ";
            else res += b + " ";
        }
        s.close();
        return res.trim();
    }
}