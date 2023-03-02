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
        while(in.hasNextLine()) {
            System.out.println(expression(in.nextLine()));
        }
        in.close();
        sc.close();
    }
    
    static String expression(String line) throws Exception {
        String r = line + " -> ";
        Stack<Integer> stack = new Stack<>();

        String[] symbols = line.split(" |\\-");
        for (String s : symbols) {
            if (s.equals("and")) {
                stack.add(value(stack));
                continue;
            } else if(!nums.containsKey(s)) {
                throw new Exception("Invalid symbol: " + s + "");
            } else {
                stack.add(nums.get(s));
            }
        }
        r += value(stack);
        return r;
    }

    static int value(Stack<Integer> numbers) {
        int v1, v2;

        while (numbers.size() > 1) {
            v1 = numbers.pop();
            v2 = numbers.pop();
            if ((v1/10) > (v2/10))
                numbers.push(v1 * v2);  
            else
                numbers.push(v1 + v2);
        }
        
        return numbers.pop();
    }
}