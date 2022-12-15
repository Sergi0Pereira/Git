
import java.util.Scanner; 
import java.util.Arrays; 

public class OrderNumbers { 
	public static void main(String[] args) { 
		
		Scanner sc = new Scanner(System.in); 
		
		System.out.print("How many numbers do you want to order? "); 
		int n = sc.nextInt(); 
		
		int[] nums = new int[n]; 
		
		System.out.println("Enter the numbers: "); 
		for(int i = 0; i < n; i++) 
			nums[i] = sc.nextInt(); 
		
		Arrays.sort(nums); 
		
		System.out.print("The ordered numbers are: "); 
		for(int i = 0; i < n; i++) 
			System.out.print(nums[i] + " "); 
		
		sc.close(); 
	} 
}