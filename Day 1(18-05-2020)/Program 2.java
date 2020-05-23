class OddThread extends Thread
{
int limit;
sharedPrinter printer;
public OddThread(int limit, sharedPrinter printer)
{
this.limit = limit;
this.printer = printer;
}
@Override
public void run() 
{
int oddNumber = 1;      
while (oddNumber <= limit)
{
printer.printOdd(oddNumber);       
oddNumber = oddNumber + 2;         
}
}
}

class EvenThread extends Thread
{
int limit;
sharedPrinter printer;
public EvenThread(int limit, sharedPrinter printer)
{
this.limit = limit;
this.printer = printer;
}
@Override
public void run() 
{
int evenNumber = 2;           
while (evenNumber <= limit)
{
printer.printEven(evenNumber);         
evenNumber = evenNumber + 2;          
}
}
}
class sharedPrinter
{

boolean isOddPrinted = false;


synchronized void printOdd(int number)
{
while (isOddPrinted)
{
try 
{
wait();
} 
catch (InterruptedException e)
{
e.printStackTrace();
}
}
System.out.println(Thread.currentThread().getName()+" "+number);
isOddPrinted = true;
try 
{
Thread.sleep(1000);
} 
catch (InterruptedException e) 
{
e.printStackTrace();
}
notify();
}

synchronized void printEven(int number)
{
while (! isOddPrinted)
{
try 
{
wait();
}
catch (InterruptedException e) 
{
e.printStackTrace();
}
}
System.out.println(Thread.currentThread().getName()+" "+number);
isOddPrinted = false;
try 
{
Thread.sleep(1000);
} 
catch (InterruptedException e) 
{
e.printStackTrace();
}
notify();
}
}
public class Main 
{
public static void main(String[] args) 
{
sharedPrinter printer = new sharedPrinter();
OddThread oddThread = new OddThread(20, printer);
oddThread.setName("—-pong");
EvenThread evenThread = new EvenThread(20, printer);
evenThread.setName("ping — >");
oddThread.start();
evenThread.start();
}
}

Output:
—-pong 1
ping — > 2
—-pong 3
ping — > 4
—-pong 5
ping — > 6
—-pong 7
ping — > 8
—-pong 9
ping — > 10
—-pong 11
ping — > 12
—-pong 13
ping — > 14
—-pong 15
ping — > 16
—-pong 17
ping — > 18
—-pong 19
ping — > 20