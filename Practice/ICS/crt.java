import java.util.*;
import java.io.*;
import java.lang.Math;

public class crt{
    public static int chiRemainder(int[] xi, int[] remainder){
        int X = 0;
        int M = 1;
        int no = xi.length;
        int[] Mi = new int[no];
        int[] Minv = new int[no];

        for(int i = 0; i < no ; i++){
            M = M * xi[i];
        }

        for(int i = 0; i < no ; i++){
            Mi[i] = M / xi[i];
            Minv[i] = (int)(Math.pow(Mi[i], xi[i] - 2)) % xi[i];
            X = X + (remainder[i] * Mi[i] * Minv[i]);
        }
        return X;
    }
    
    public static void main(String[] args) {
        Scanner ip = new Scanner(System.in);

        System.out.println("Enter number of equations");
        int n = Integer.parseInt(ip.nextLine());

        int[] xi = new int[n];
        int[] remainder = new int[n];

        for(int i = 0 ; i < n; i++){
            System.out.println("Enter X("+ i +"): ");
            xi[i] = Integer.parseInt(ip.nextLine());
        }

        for(int i = 0 ; i < n; i++){
            System.out.println("Enter remainder("+ i +"): ");
            remainder[i] = Integer.parseInt(ip.nextLine());
        }

        System.out.println("X is " + chiRemainder(xi, remainder));
    }
}