import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class DayTwo {
  public static void main(String[] args) {
    try {
      File myObj = new File("input_day_2.txt");
      Scanner fileReader = new Scanner(myObj);
      int count = 0;
      while (fileReader.hasNextLine()) {
        String data = fileReader.nextLine();
        if (validateTwo(data)) {count++;}
      }
      System.out.println(count);
      fileRead`er.close();
    } catch (FileNotFoundException e) {
      System.out.println("An error occurred.");
      e.printStackTrace();
    }
  }
  public static boolean validateOne(String pswd) {
    String[] kv =  pswd.split(" ");
    String[] r = kv[0].split("-");
    int[] range = new int[2];
    for (int i = 0; i < 2; i++) {
      range[i] = Integer.parseInt(r[i]);
    }
    kv[0].split("-");
    char key = kv[1].charAt(0);
    int count = 0;
    for (char c: kv[2].toCharArray()) {
      if (c == key) {count++;}
    }
    return range[0] <= count && count <= range[1];
  }
  public static boolean validateTwo(String pswd) {
    String[] kv =  pswd.split(" ");
    String[] r = kv[0].split("-");
    int[] range = new int[2];
    for (int i = 0; i < 2; i++) {
      range[i] = Integer.parseInt(r[i]);
    }
    kv[0].split("-");
    char key = kv[1].charAt(0);
    return key == kv[2].charAt(range[0] - 1) ^ key == kv[2].charAt(range[1] -1 );

  }
}
