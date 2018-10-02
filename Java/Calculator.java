// The goal for this is to make a text based calculator in Java
public class Calculator {

	String name = "Nathan";

	public void sayHello() {
		System.out.println("Hello " + name + "!");
	}

	public void compareNumbers(int x, int y) {
		if(x == y) {
			System.out.println(x + " is equal to " + y + ".");
		} else if (x > y) {
			System.out.println(x + " is bigger than " + y + ".");
		} else if (x < y) {
			System.out.println(x + " is less than " + y + ".");
		}
	}

	public static void main(String[] args) {

		Calculator app = new Calculator();

		app.sayHello();

		app.compareNumbers(2, 2);

	}

}