import java.util.*;
import java.io.*;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class sha1Checksum {
    public static void main(String[] args) throws NoSuchAlgorithmException, IOException, FileNotFoundException {
        Scanner input = new Scanner(System.in);
        MessageDigest md = MessageDigest.getInstance("SHA1");
        StringBuffer sb = new StringBuffer();

        System.out.println("Enter the name of the file");
        String fileName = input.nextLine();
        FileInputStream fip = new FileInputStream(fileName);

        byte[] data = new byte[1024];
        int nread = 0;

        while ((nread = fip.read(data)) != -1) {
            md.update(data, 0, nread);
        }

        byte[] result = md.digest();

        for (int i = 0; i < result.length; i++) {
            sb.append(Integer.toString((result[i] & 0xff) + 0x100, 16).substring(1));
        }

        System.out.println("\nFile: " + fileName + "\nSHA1 checksum: " + sb.toString());
    }
}
