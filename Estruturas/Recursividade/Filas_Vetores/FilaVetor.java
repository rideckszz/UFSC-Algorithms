
public class FilaVetor {
    int inicio;
    int fim;
    int qt;
    Integer[] vetor;

    FilaVetor(int tamanho){
        vetor = new int[tamanho];
        qt = 0;
        inicio = 0;
    }

    /* Aula 1403
    (ini+qt)% tam 
    inicio = (inicio + 1) % tam
    Se o inicio n for o final 
    Atributos -> Vetor, qt, inicio
    Métodos -> Insere fila e remove*/

    Integer removeLista(){
        if (qt != 0){
            qt--;
            Integer item = dados[qt];
            if (qt  > 0 && qt == dados.length/4)
                resize(dados.length/2);
            return item;
        }
        return null;
    }

    void imprimeCircular(){
        int fim = (inicio + qt) % dados.length;
        for (int i = inicio; i != fim; i = (i+1)% dados.length){
            System.out.print(dados[i])
        }

    }


    boolean vazia(){
        return qt ==0;
    }

    boolean cheia(){
        return qt == vetor.length;
    }

    int posicao (int i){
        return (inicio+ 1)% qt;
    }

    void insereFila(int n){ 
        if (!(qt == dados.length)){
            int pos = (inicio + qt) % dados.length;
            dados[pos] = new
            qt+= 1;
        }
    }

    Integer retiraFila(){
      

    }
}
