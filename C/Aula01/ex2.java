import java.util.*;

public class ex2 {
    static Map<String, Double> map = new HashMap<String, Double>();
    public static void main(String[] args) {        
        Scanner sc = new Scanner(System.in);

        String[] expr;
		int exprSize;
        String expr0;

        while(sc.hasNextLine()) {
            Scanner sl = new Scanner(sc.nextLine());
            String key = sl.next();
            expr = sc.nextLine().split(" ");
            exprSize = expr.length;
            double value = expr[1];

            map.put(key, value);

            while(sl.hasNext()) {
                String operand = sl.next();
                String value2 = sl.next();
                if (!operand.equals("=")) {
                    value = operate(value, operand, valueDecision(value2));
                } else {
                    map.put(value2, value);
                }
            }

            System.out.println(value);

            sl.close();
        }

        sc.close();

    }

    private static double valueDecision(String value) {
		return isNumber(value) ? Double.parseDouble(value) : map.get(value);
	}

	public static boolean isNumber(String value) {
        // java.lang.NullPointerException at ex2.valueDecision(ex2.java:61)
        try {
            Double.parseDouble(value);
            return true;
        } catch (NumberFormatException e) {
            return false;
        }
	}

    public static Double operate(double op1, String operand, double op2) {
		Double result = null;
		switch (operand) {
			case "+":
				result = op1+op2;
				break;
			case "-":
				result = op1-op2;
				break;		
			case "*":
				result = op1*op2;
				break;
			case "/":
				result = op1/op2;
				break;				
			default:
				System.err.println("Invalid operator!");
		}
		return result;
	}

}
