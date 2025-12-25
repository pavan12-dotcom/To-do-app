import java.util.*;
public class calculator {
public static void main(String[] args) {
        Scanner sc=new Scanneimport java.util.*;
public class calculator{
    public static void mar(System.in);
        System.out.println("Enter A");
        int a=sc.nextInt();
        System.out.println("Enter B");
        int b=sc.nextInt();
        System.out.println("operator");
        char op=sc.next().charAt(0);
          int res,c = 0;
        switch(op){
          case '+':
            c=a+b;
            break;
           case '-':
            c=a-b;
            break;
           case '*':
            c=a*b;
            break;
           case '/':
            if(b>0)
                {
                c=a/b;break;
                }
            else{
                 System.out.println(b+"dosn't divisible by"+a);
              break;
                }
            
          case '^':
            c=a^b;
            break;
        default :
             System.out.println("INVAILD OPERATOR");
        }
  if (true) {
            res=c;
        
  }   System.out.println(res);
    }
}          

