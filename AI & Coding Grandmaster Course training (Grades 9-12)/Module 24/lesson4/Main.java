// activity to understand the use of finally
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		try {
			System.out.println("enter two numbers:");
			int x = sc.nextInt();
			int y = sc.nextInt();
			int z = x / y;
			System.out.println(x + " / " + y + " = " + z);
		} catch (ArithmeticException ex) {
			System.out.println("--- catch block ---");
			System.out.println(ex.toString());
		} finally {
			System.out.println("---- finally block ----");
			System.out.println("Application Designed & Developed by");
			System.out.println("team @ Codingal");
			sc.close();
		}
		System.out.println("--- DONE ---");
	}
}
//Note*first try running the program with a arithmetic exception then without it and see the difference to understand use of finally

