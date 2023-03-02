import java.util.EmptyStackException;
import java.util.Scanner;
import java.util.Stack;

public class ex3 {
    public static void main(String[] args) {
        Stack<Double> stack = new Stack<>();
        Scanner sc = new Scanner(System.in);
        Double result = null;

        while (sc.hasNext()) {
            stack = new Stack<Double>();
            String[] input = sc.nextLine().split(" ");
            // use operate function from ex2
			do {
				for (String s : input) { 
					if (ex2.isNumber(s)) 
						stack.add(Double.parseDouble(s)); // push number to stack
                    else {
                        try {
                            result = ex2.operate(stack.pop(), s, stack.pop()); // pop twice
                        } catch (EmptyStackException e) {
                            System.err.println("Invalid expression");
                            break;
                        }

                        if (result != null)
                            stack.add(result); // push result to stack
                        else
                            break; 
                    }
                    System.out.println(stack); 
                }
            } while(result == null);    
        }
        sc.close();

    }
}
