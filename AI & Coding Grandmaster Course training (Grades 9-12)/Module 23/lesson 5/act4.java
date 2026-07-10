class Main {

    int age;
    Main(int age){
        age = age;
		//this.age = age;
    }

    public static void main(String[] args) {
        Main obj = new Main(24);
        System.out.println("obj.age = " + obj.age);
    }
}
