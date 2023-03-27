import java.util.Scanner;

public class calcu {
  public static void main(String [] args){
    Scanner entrada = new Scanner (System.in);

    char op;
    do {
      double n1, n2;

      System.out.println("Digite os dois numeros: ");
      n1 = entrada.nextDouble();
      n2 = entrada.nextDouble();

      System.out.println("Digite a operacao a ser feita:");
      op = entrada.next().charAt(0);
      double result;

      switch (op)
      {
        case '+': result = n1 + n2;
                System.out.println (n1 + " + " + n2 + " = " + result);
                break;

        case '-': result = n1 - n2;
                  System.out.println (n1 + " - " + n2 + " = " + result);
                  break;

        case '*': result = n1 * n2;
                  System.out.println (n1 + " * " + n2 + " = " + result);
                  break;

        case '/': if (n2 != 0) {
                  result = n1 / n2;
                  System.out.println (n1 + " / " + n2 + " = " + result);
                  }
                  else
                    System.out.println("Nao e possivel dividir por zero.");
                  break;
        default: System.out.println ("Operador inválido");
      }
    } while (op != '0');
  }
}