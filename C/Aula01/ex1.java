import java.util.Scanner;

public class ex1 {
    public static void main(String[] args) {
        System.out.print("Input: ");

        Scanner sc = new Scanner(System.in); 

        String[] input;
        double n = 0;
        double m = 0;
        boolean valid = false;

        do{
            String in = sc.nextLine();
            input = in.split(" ");
            
            try{
                n = Double.parseDouble(input[0]);
                m = Double.parseDouble(input[2]);
                valid = true;
            } catch (NumberFormatException e){
                System.err.println("Invalid input");
                valid = false;
                continue;
            }
        } while(valid == false);
        
        switch(input[1]){
            case "+":
                System.out.println(n + m);
                break;
            case "-":
                System.out.println(n - m);
                break;
            case "*":
                System.out.println(n * m);
                break;
            case "/":
                System.out.println(n / m);
                break;
            case "%":
                System.out.println(n % m);
                break;
            default:
                System.err.println("Invalid operator");
                break;
        }
    
        sc.close();


    }
    
}
