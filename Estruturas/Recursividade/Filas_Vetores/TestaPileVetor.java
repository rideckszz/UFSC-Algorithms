

import java.util.Scanner;

public class TestaPileVetor {
    
    public static void main(String[] args){
        System.out.println("Digite tamanho da pilha");
        Scanner entrada = new Scanner(System.in);
        int tam = entrada.nextInt();
        PileVetor lis = new PileVetor(tamanho);
        int op;
        do {
            System.out.println("Digite a opção desejada "
                    + "\n 1 - Inserir elemento"
                    + "\n 2 - Remover elemento "
                    + "\n 3 - Imprimir lista "
                    + "\n 4 - Sair "
                    + "\n 5 - Remover posição ");
            op = entrada.nextInt();
            switch (op){
                case 1:
                    System.out.println("digite valor");
                    Integer v = entrada.nextInt();
                    lis.inserePilha(v);
                    break;
                case 2:
                    Integer r = lis.removeLista();
                    System.out.println("removeu " + r );
                    break;
                case 3: 
                    lis.imprimeLista();
                    break;
                case 4: 
                    System.out.println("saindo");
                    break;
                case 5:
                    System.out.println("Digite a posição");
                    Integer pos = entrada.nextInt();
                    pos = lis.removePos(pos);
                    System.out.println("Removido: "+ pos);
                default:
                    System.out.println("opção inválida");
                    break;
          }
   
        } while (op != 4);
    }
}
