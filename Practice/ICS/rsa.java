import java.util.*;
import java.io.*;
import java.math.*;

public class rsa{
    static BigInteger p, q,n, phi, e, d ;
    Random rnd;
    int bitLength = 1024;
    
    public rsa(){
        rnd = new Random();

        p = BigInteger.probablePrime(bitLength, rnd);
        q = BigInteger.probablePrime(bitLength, rnd);

        n = p.multiply(q);

        phi = p.subtract(BigInteger.ONE).multiply(q.subtract(BigInteger.ONE));

        e = BigInteger.probablePrime(bitLength/2, rnd);

        //System.out.println("Public key used for encryption (" + e + ", " + n +")");

        while(phi.gcd(e).compareTo(BigInteger.ONE) > 0 && e.compareTo(phi) < 0){
            e.add(BigInteger.ONE);
        }

        d = e.modInverse(phi);
        //System.out.println("Public key used for decryptioon (" + d + ", " + n + ")");
    }

    public static void main(String[] args) {
        rsa rsaObject = new rsa();
        String inputString;
        Scanner in = new Scanner(System.in);
        byte[] eByte;
        byte[] dbyte;

        System.out.println("Enter String to be Encrypted");
        inputString = in.nextLine();

        eByte = (new BigInteger(inputString.getBytes())).modPow(e, n).toByteArray();
        System.out.println("\n\nEncrypted String: ");
        for (byte b : eByte) {
            System.out.printf("|");
            System.out.printf("%02X", b);
            
        }

        dbyte = (new BigInteger(eByte)).modPow(d, n).toByteArray();
        System.out.println("\n\nOriginal String: " + new String(dbyte));

    }
}