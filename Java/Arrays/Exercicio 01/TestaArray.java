import java.util.ArrayList;
import java.util.Scanner;

public class TestaArray{

    public static void main(String[] args){
        ArrayList<Integer> lista = new ArrayList<>();
        Scanner entrada = new Scanner(System.in);
        System.out.println(lista.isEmpty());

        for (int i = 0; i < 10; i++){
            System.out.println("Digite o elemento:  ");
            int n = entrada.nextInt();

            if (!lista.contains(n))
                lista.add(n);
            else System.out.println("Esse número ja existe na lista.");

        }

        for (int item: lista){
            System.out.println(item + " ");
        }
       
        System.out.println(lista.isEmpty());
        System.out.println("tamanho = "+ lista.size());
        
        //ArrayList<Integer> lista = new ArrayList<Integer>();
    
    }

}
