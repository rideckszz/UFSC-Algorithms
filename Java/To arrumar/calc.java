import java.util.scanner

public static void (String [] args) {
  Scanner entrada = new Scanner (system.in);

  char op;
  double n1, n2; //float extendido

  System.out.println("Digite os dois numeros: ");
  n1 = entrada.nextDouble();
  n2 = entrada.nextDouble();

  System.out.println("Digite a operacao a ser feita:");
  op = entrada.next().charAt(0);


  switch (op) {
  case "+":
    System.out.printf (n1, n2, n1 + n2);
    break
  }
}
