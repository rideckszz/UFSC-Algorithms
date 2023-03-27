import java.util.ArrayList;
import java.util.Scanner;


public class TestaBiblioteca{

    public static void main(String[] args){
        Livro v1 = new Livro("Crime e Castigo", "Fiodor", 500, 45);
        
        Biblioteca atenas = new Biblioteca();
        
        atenas.adicionaLivro(v1);
        atenas.imprimeLivros();

       
        for (Livro liv: bib){
            System.out.println(liv);
        }
    
    
    }

}