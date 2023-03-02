import java.util.*;

public class ex2 {
	
	static Map<String, Double> vars = new HashMap<>();
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String[] expr; // expression
		int exprSize; // expression size
		Double result, resultToSave;
		double op2; 
		String operand, expr0; 
		while(sc.hasNext()) {
			result = null;
			do {
				expr = sc.nextLine().split(" ");
				exprSize = expr.length;
				expr0 = expr[0];
				if (exprSize == 1) {
					if (!isNumber(expr0))
						result = vars.get(expr0);
				}
				else {
					operand = expr[1];
					op2 = valueDecision(expr[2]);
					if (!operand.equals("="))
						result = operate(valueDecision(expr0), operand, op2);
					else {
						resultToSave = op2;
						if (exprSize == 5) {
							resultToSave = operate(resultToSave, expr[3], valueDecision(expr[4]));
						}
						vars.put(expr0, resultToSave);
					}
				}
			} while (result == null || exprSize > 5);
			System.out.println(result);  
		}
        sc.close();    
    }

	private static double valueDecision(String value) {
		return isNumber(value) ? Double.parseDouble(value) : vars.get(value);
	}

	public static boolean isNumber(String value) {
		try {
			Double.parseDouble(value);
		} catch (NumberFormatException e) {
			return false;
		}
		return true;
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

    public static boolean isNumber(Object value) {
        return false;
    }
}