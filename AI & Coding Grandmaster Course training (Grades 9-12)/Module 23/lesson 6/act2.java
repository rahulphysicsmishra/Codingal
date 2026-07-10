class Parent{
	public void sayHello(){
		System.out.println("Hello from Parent");
	}
}

class Child extends Parent{
	@Override
	public void sayHello(){
		System.out.println("Hello from Chid");
	}
}


class Main
{
	public static void main(String[] args) 
	{
		Parent p = new Child();   //for calling hello from child
		//Parent p = new Parent();  //for calling hello from parent
		p.sayHello();
	}
}

