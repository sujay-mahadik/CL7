import java.util.*;
import java.io.*;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class sha{
    public static String sha1String(String ip) throws NoSuchAlgorithmException {
        StringBuffer sb = new StringBuffer();
        MessageDigest md = MessageDigest.getInstance("SHA1");
        byte[] resultInBytes = md.digest(ip.getBytes());

        for(int i = 0 ; i < resultInBytes.length ; i++){
            sb.append(String.format("%02x", resultInBytes[i]));
        }

        return sb.toString();
    }

    public static String sha1File(String fp) throws NoSuchAlgorithmException, FileNotFoundException, IOException{
        StringBuffer sb = new StringBuffer();
        MessageDigest mdf = MessageDigest.getInstance("SHA1");
        FileInputStream fip = new FileInputStream(fp);
        byte[] data = new byte[1024];
        int nread;

        while((nread = fip.read(data)) != -1){
            mdf.update(data, 0, nread);
        }

        byte[] result = mdf.digest();

        for(int i = 0 ; i < result.length ; i++){
            sb.append(String.format("%02x", result[i]));
        }

        return sb.toString();
    }
    public static void main(String[] args) throws NoSuchAlgorithmException, FileNotFoundException, IOException {
        //
        Scanner input = new Scanner(System.in);
        String inputString;
        int ch;

        //
        String filePath;
        int nread;


        do{
            System.out.println("Enter choice\n1: String Checksum\n2: File Checksum\n3: Exit");
            ch = Integer.parseInt(input.nextLine());

            switch(ch){
                case 1:
                System.out.println("Enter the string");
                inputString = input.nextLine();
                System.out.println("\nSHA1: " + sha1String(inputString));
                break;

                case 2:
                System.out.println("Enter file path");
                filePath = input.nextLine();
                System.out.println("\nFile: " + filePath+ "\nSHA1: " + sha1File(filePath));
                break;
            }
        }   while(ch < 3);
    }
}