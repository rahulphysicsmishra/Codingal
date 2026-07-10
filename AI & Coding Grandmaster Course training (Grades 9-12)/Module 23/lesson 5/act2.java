//this activity is mainly to explain multi-level inheritance
//parent class
class Animal{
	void eat(){
		System.out.println("eating...Animal class...eat method");
		}
}
//child class
class Lion extends Animal{
	void roar(){
		System.out.println("Roar...Lion class...roar method");
		}
}
//child of child
class BabyLion extends Lion{
	void weep(){
		System.out.println("weeping...BabyLion class...weep method");
		}
}

class Main{
	public static void main(String args[]){
	BabyLion obj=new BabyLion();//object of child of child class
	obj.weep();
	obj.roar();
	obj.eat();
	}
}
 
