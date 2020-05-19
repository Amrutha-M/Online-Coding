/*We have a Letter or a word then we need add some letters to it and need to find out shortest palindrome 
For example we take "S": S will be the shortest palindrome string. If we take "xyz": zyxyz will be the shortest palindrome string
So we need to add some characters to the given string or character and find out what will be the shortest palindrome string by using simple java program.*/

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
