import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.ArrayList;

public class DayOne {
  public static int partOne(String fileName) {
    int num = 0;
    try {
      File myObj = new File(fileName);
      Scanner myReader = new Scanner(myObj);
      ArrayList<Integer> n = new ArrayList<Integer>();
      while (myReader.hasNextLine()) {
        int data = Integer.decode(myReader.nextLine());
        n.add(data);
      }
      myReader.close();
      for (int i: n) {
        if (n.indexOf(2020 - i) != -1) {
          num = (2020 - i) * i;
          break;
        }
      }
    } catch (FileNotFoundException e) {
      System.out.println("An error occurred.");
      e.printStackTrace();
    }
    return num;
  }
  public static int partTwo(String fileName) {
    int num = 0;
    try {
      File myObj = new File(fileName);
      Scanner myReader = new Scanner(myObj);
      ArrayList<Integer> n = new ArrayList<Integer>();
      while (myReader.hasNextLine()) {
        int data = Integer.decode(myReader.nextLine());
        n.add(data);
      }
      myReader.close();
      for (int i: n) {
        for (int j : n) {
          if (n.indexOf(2020 - i - j) != -1) {
            num = (2020 - i - j) * i * j;
            break;
          }
        }
      }
    } catch (FileNotFoundException e) {
      System.out.println("An error occurred.");
      e.printStackTrace();
    }
    return num;
  }
  public static void main(String[] args) {
    System.out.println(partTwo("input.txt"));
    partOne("input.txt");
  }
}
