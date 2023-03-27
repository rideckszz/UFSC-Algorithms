/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */


public class TestaFilaVetor {

    public static void main(String[] args) {
        FilaVetor fila = new FilaVetor(5);
 
        fila.insereFila(10);
        fila.insereFila(20);
        fila.insereFila(30);
        fila.insereFila(40);
        fila.insereFila(50);
        fila.insereFila(60);
        Integer x = fila.retiraFila();
        System.out.println(x);
        x = fila.retiraFila();
        System.out.println(x);
        x = fila.retiraFila();
        System.out.println(x);
        x = fila.retiraFila();
        System.out.println(x);
        x = fila.retiraFila();
        System.out.println(x);
  

    }
    
}
