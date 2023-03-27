import java.util.ArrayList;

public class Biblioteca {
    Arraylist<Livro> lista;

    Biblioteca(){
        lista = new ArrayList<>();

    }
    void adicionaLivro(Livro liv){
        lista.add(liv);
    }

    void imprimeLivros(){
        for (Livro liv: lista){
            System.out.println(liv);
            System.out.println("-----------------");

        }
    }

    void precoEstoque(){
        for (Livro liv: lista){
            return preco;
            
        }
    }
}
