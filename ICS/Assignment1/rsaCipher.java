import java.io.*;
import java.math.*;
import java.util.*;

public class rsaCipher {
    private static BigInteger p, q, N, phi, e, d;
    private int bitlen = 1024;
    private Random r;

    public rsaCipher() {
        r = new Random();
        p = BigInteger.probablePrime(bitlen, r);
        q = BigInteger.probablePrime(bitlen, r);

        N = p.multiply(q);
        phi = p.subtract(BigInteger.ONE).multiply(q.subtract(BigInteger.ONE));
        e = BigInteger.probablePrime(bitlen / 2, r);

        while (phi.gcd(e).compareTo(BigInteger.ONE) > 0 && e.compareTo(phi) < 0) {
            e.add(BigInteger.ONE);
        }

        d = e.modInverse(phi);
    }

    public static void main(String[] args) {
        rsaCipher rsa_object = new rsaCipher();
        Scanner in = new Scanner(System.in);
        String inputString;

        System.out.println("Enter string to be encrypted");
        inputString = in.nextLine();

        System.out.println("Encrypting string : " + inputString);
        System.out.println("\nString in Bytes : " + bytesToString(inputString.getBytes()));

        byte[] encrypted = rsaCipher.encrypt(inputString.getBytes());
        System.out.println("Encrypted string : " + new String(encrypted));

        byte[] decrypted = rsaCipher.decrypt(encrypted);
        System.out.println("Decrypted string : " + new String(decrypted));
    }

    private static String bytesToString(byte[] encrypted) {
        String toReturn = "";
        for (byte b : encrypted) {
            toReturn += Byte.toString(b);
        }
        return toReturn;
    }

    public static byte[] encrypt(byte[] msg) {
        byte[] eString;
        eString = (new BigInteger(msg)).modPow(e, N).toByteArray();
        return eString;
    }

    public static byte[] decrypt(byte[] msg) {
        byte[] dString;
        dString = (new BigInteger(msg)).modPow(d, N).toByteArray();
        return dString;
    }
}