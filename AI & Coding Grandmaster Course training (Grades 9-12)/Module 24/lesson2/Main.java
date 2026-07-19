//this program is created to teach the concept of abstraction
abstract class Objects{
                //abstract method declaration
                abstract void showShape();
				public void shape(){
					System.out.println("I'm form abstract class");
				}
}
 
class Sphere extends Objects{
                /**
                 *this is indirectly a overrideen showshape method by making use of abstract class
                 */
                void showShape() {
                      System.out.println("Object type is Sphere.");
                }     
}
 
class Cuboid extends Objects{
                /**
                 *this is indirectly a overrideen showshape method by making use of abstract class
                 */
                void showShape() {
                     System.out.println("Object type is Cuboid.");
               }  
}
 
class Prism extends Objects{
                /**
                 *this is indirectly a overrideen showshape method by making use of abstract class
                 */
                void showShape() {
                     System.out.println("Object type is Prism.");
                }             
 
}
 
public class Main {
                public static void main(String args[]){
                       Objects obj = new Sphere();//object of sphere
                       obj.showShape();
                       obj = new Cuboid();//cuboid
                       obj.showShape();
                       obj = new Prism();//prism
                       obj.showShape();
					   obj.shape();
                }  
}
