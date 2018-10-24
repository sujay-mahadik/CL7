import java.io.*;
import java.util.Scanner;
import java.lang.Math;

class crtAlgo{

    static int chiRemain(int xi[], int remainder[]){
        int X = 0;
        int M;
        int no = xi.length;

        int Mi[] = new int[no];
        int Minv[] = new int[no];

        M = 1;

        for (int i = 0; i < xi.length; i++) {
            M = M * xi[i];
            

            // System.out.println("Mi = " + Mi[i]);
            // System.out.println("Minv = " + Minv[i]);
            // System.out.println("X = " + X);
            

        }

        for (int i = 0; i < xi.length; i++) {
            Mi[i] = M / xi[i];
            Minv[i] = (int)(Math.pow(Mi[i], (xi[i] - 2))) % xi[i];
            X = X + (remainder[i] * Mi[i] * Minv[i]);

            // System.out.println("Mi = " + Mi[i]);
            // System.out.println("Minv = " + Minv[i]);
            // System.out.println("X = " + X);
        }

        return X;
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int n;
         System.out.println("Enter the number of equations");
         n = input.nextInt();

         int xi[] = new int[n];
         int remainder[] = new int[n];

         for (int i = 0; i < n; i++) {
            System.out.println("Enter x("+i+")");
            xi[i] = input.nextInt();
         }

         for (int i = 0; i < n; i++) {
             System.out.println("Enter the remainder("+i+")");
             remainder[i] = input.nextInt();
         }

         System.out.println("X is "+chiRemain(xi, remainder));
    }
}