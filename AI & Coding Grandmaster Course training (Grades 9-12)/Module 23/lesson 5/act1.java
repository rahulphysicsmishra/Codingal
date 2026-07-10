//this activity is mainly to undersand the concept of inheritance
//Parent Class
class Parent
{
    int age,id;
    String name;
    void naming(String name)
    {
        System.out.println("Name:"+name);
    }
}

//child class
class Child extends Parent
{
    void ageN(int age)
    {
        System.out.println("Age of student is:"+age);
    }
}
class Main
{
    public static void main(String [] er)
    {
        Child s= new Child();//creating object of child class
        s.naming("Aashish");
        s.ageN(14);
    }
    
}
