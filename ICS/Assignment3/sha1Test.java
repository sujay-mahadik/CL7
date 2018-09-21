import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.io.*;
import java.util.*;

public class sha1Test {

    static String sha1(String ip) throws NoSuchAlgorithmException {

        Scanner input = new Scanner(System.in);
        MessageDigest md = MessageDigest.getInstance("SHA1");
        byte[] result = md.digest(ip.getBytes());
        StringBuffer sb = new StringBuffer();

        for (int i = 0; i < result.length; i++) {
            // byte to hexademical conversion use any one of the foll
            // explanation at
            // https://stackoverflow.com/questions/25838473/what-does-0xff-do-and-md5-structure
            // sb.append(Integer.toString((result[i] & 0xff) + 0x100, 16).substring(1));
            // sb.append(String.format("%02x", result[i]));
            sb.append(Integer.toString((result[i] & 0xff) + 0x100, 16).substring(1));
        }

        return sb.toString();

    }

    public static void main(String[] args) throws NoSuchAlgorithmException {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter a String: ");
        String input = scanner.nextLine();
        System.out.println("\nInput String: " + input + " \nMessage digest using SHA1: " + sha1(input));

    }

}
