
import java.util.Scanner;
import java.io.*;


public class TestaFile{
  public static void main(String [] args) throws IOException{

    File f = new File ("dados.txt");
    FileWriter writer = new FileWriter (f);
    BufferedWriter bf = new BufferedWriter(writer);
    PrintWriter printer = new PrintWriter(bf);

//////////////////////////////////////////////////////// -> Writer "printa"
    writer.write("Oi puta!");
/////////////////////////////////////////////////////// -> Scanner para coletar o numeros
    Scanner entrada = new Scanner(System.in);
    System.out.println("Digite os numeros: ");
    int n = entrada.nextInt();
/////////////////////////////////////////////////////// -> loop que realiza a tabuada
    for (int i = 0; i < 11; i++){
      printer.println("\n" + i + "*" + n + " = " + i * n);
      }
/////////////////////////////////////////////////////// -> Fecha os imports
    bf.close();
    printer.close();
    writer.close();
///////////////////////////////////////////////////////
 }

}
