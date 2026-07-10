class Main {
  public static void main(String[] args) {
	//user input process can also be used rather than giving manual inputs
    String first="Cod";
	String second="ingal";
	String codingal=first+second;
	String codingalTrick="Welcome"+"to"+"Codingal";
	String codingalCapital=codingal.toUpperCase();
	String codingalSmall = codingalCapital.toLowerCase();
	//correct spelling is length not lenght
	int lengthOfCodingal=codingal.length();
	int lengthOfCodingalTrick=codingalTrick.length();
	int sum=lengthOfCodingal+lengthOfCodingalTrick;

	//Guess the answer before running
	// a msg can also be added for the output screen if required
	System.out.println(codingal);
	System.out.println(codingalTrick);
	System.out.println(codingalCapital);
	System.out.println(codingalSmall);
	System.out.println(sum);

  }
}