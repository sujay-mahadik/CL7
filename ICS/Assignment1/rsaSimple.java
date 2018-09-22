import java.util.*;
import java.io.*;
import java.math.*;

public class rsaSimple {
    static BigInteger p, q, N, phi, e, d;
    int bitlen = 1024;
    Random r;

    public rsaSimple() {
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
        rsaSimple rsa_object = new rsaSimple();
        Scanner in = new Scanner(System.in);
        String inputString;
        byte[] eByte;
        byte[] dByte;

        System.out.println("Enter string");
        inputString = in.nextLine();

        // byte[] inputByte = BigInteger.valueOf(inputInteger).toByteArray();

        eByte = (new BigInteger(inputString.getBytes())).modPow(e, N).toByteArray();
        System.out.println("\nEncryption : " + new String(eByte));

        dByte = (new BigInteger(eByte)).modPow(d, N).toByteArray();
        System.out.println("Decryption : " + new String(dByte));
    }

}