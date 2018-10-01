// The goal for this is to make a text based calculator in Java
public class Calculator {

	String name = "Nathan";

	public void sayHello() {
		System.out.println("Hello " + name + "!");
	}

	public static void main(String[] args) {

		Calculator app = new Calculator();

		app.sayHello();

	}

}