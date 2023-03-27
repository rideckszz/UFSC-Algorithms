/* Listas Simplismente Encadeadas
-- Notes:
    - N tem reserva de espaco continua na memoria -> Um por um
    - */

public class ListaEncadeada {
    private Nodo inicio;

    private class Nodo {
        int dado;
        Nodo proximo;
    }

    public ListaEncadeada(){
        inicio = null;

    }

    public void insereLista(){
      Nodo novo =  new Nodo();
      novo.dado = valor;
      novo.proximo = inicio;
      inicio = novo;
    }

    public void imprimeLista(){
      for (Nodo i = inicio; i != null; i = i.proximo){
        System.out.print(i.dado);
      }
      System.out.println();
    }
}
