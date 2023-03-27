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
}