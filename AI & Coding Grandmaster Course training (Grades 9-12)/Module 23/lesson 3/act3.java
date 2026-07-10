import java.util.*;

class Main {
  public static void main(String[] args) {
	int sum=0;
    String result;
    Scanner sc=new Scanner(System.in);
	System.out.println("Enter the number of Subjects: ");
	int noOfSubjects = sc.nextInt();
	int marks[]=new int[noOfSubjects]; //intializing array
	System.out.println("Enter the marks of " +noOfSubjects +" Subjects.Press Enter to give marks for another subject");
	//entering marks
	for(int i=0;i<noOfSubjects;i++){
		marks[i]=sc.nextInt();
	}//calculating sum
	for(int j=0;j<noOfSubjects;j++){
		sum=sum+marks[j];
	}//generating result
	int percentage=sum/noOfSubjects;
	//can also be written as
	//int percentage=(sum/noOfSubjects*100)*100;
	System.out.println(percentage);
	if(percentage>= 95){
		result="You scored O grade. Great Work!";

	}else if(percentage>90 && percentage<95){
		result="You scored A+.Well Done!";
	}
	//make sure to to create grading for other marks too
	//percentage can also be converted to cgpa
	else {
		result="you pased";
	}
	System.out.println(result);
  }
}