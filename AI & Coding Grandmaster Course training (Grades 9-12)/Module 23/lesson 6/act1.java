class Student 
{
	int id;
	String name;
	float stipend;
	
	Student(){}

	Student(int id, String name){
		this.id = id;
		this.name = name;
	}

	Student(int id, String name, float stipend){
		this.id = id;
		this.name = name;
		this.stipend=stipend;
		
	}

	void displayDetails(){
		System.out.println(this.id + " | " + this.name + " | " + this.stipend);
	}
} //Student

class Main 
{
	public static void main(String[] args) 
	{
       Student st1=new Student(); //default constructor
	   Student st2=new Student(45,"Aashish"); //overloaded constructor with 2 parameters
	   Student st3=new Student(234,"Cody",10000);//overloaded constructor with 3 parameters

       st1.displayDetails();
       st2.displayDetails();
       st3.displayDetails();
	}
}