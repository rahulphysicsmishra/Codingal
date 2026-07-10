//this activity is mainly to explain Hierarchical inheritance
//parent class
class Mammals{
	void mam(){
		System.out.println("Inside Mammals Class");
		}
}
//child class
class Lion extends Mammals{
	void roar(){
		System.out.println("Inside Lion class ");
		}
}
//child 
class Human extends Mammals{
	void hum(){
		System.out.println("Inside Human");
		}
}

class Main{
	public static void main(String args[]){
	Lion obj=new Lion();//object of child of child class
	obj.hum();//this will result in error to run this we have to create object of Human
	obj.roar();
	obj.mam();
	}
}
 