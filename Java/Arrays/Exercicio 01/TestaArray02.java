import java.util.ArrayList;
import java.util.Scanner;

public class TestaArray02{

    public static void main(String[] args){
    
        ArrayList<Casa> listacasas = new ArrayList<>();
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite número de comodos para 4 casas");
        Casa c1 = new Casa(entrada.nextInt());
        Casa c2 = new Casa(entrada.nextInt());
        Casa c3 = new Casa(entrada.nextInt());
        Casa c4 = new Casa(entrada.nextInt());
        
        listacasas.add(c1);
        listacasas.add(c2);
        listacasas.add(c3);
        listacasas.add(c4);
       
        for (Casa c: listacasas){
            System.out.println(c);
        }
    
    
    }

}