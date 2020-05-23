import java.util.Scanner;
 
public class ShortestPalindromeDemo {
 
public static String shortestPalindrome(String str) {
     
int x=0;  
int y=str.length()-1;
     
  while(y>=0){
     if(str.charAt(x)==str.charAt(y)){
          x++;
         }
            y--;
  }
 
if(x==str.length())
return str;
 
String suffix = str.substring(x);
String prefix = new StringBuilder(suffix).reverse().toString();
String mid = shortestPalindrome(str.substring(0, x));
 
return prefix+mid+suffix;
}
 
public static void main(String[] args) 
{
 
Scanner in = new Scanner(System.in);
 
System.out.println("Enter a String to find out shortest palindrome");
 
String str=in.nextLine();
 
System.out.println("Shortest palindrome of "+str+" is \n"+shortestPalindrome(str));
 
}
}

Output:
Enter a String to find out shortest palindrome
my name is amrutha
Shortest palindrome of my name is amrutha is 
ahturma si eman ymy name is amrutha