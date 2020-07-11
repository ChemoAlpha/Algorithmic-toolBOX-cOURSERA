import java.util.Scanner;
 class sumoftwonum {
	int a,b;
	Scanner sc;
	void add()
	{
		sc=new Scanner(System.in);
		a=sc.nextInt();
		b=sc.nextInt();
		int c=a+b;
		System.out.println("the sum of the entered number is "+ c);
		
	}
	
	public static void main(String args[])
	{
		sumoftwonum s1=new sumoftwonum();
		s1.add();
		
	}

}
