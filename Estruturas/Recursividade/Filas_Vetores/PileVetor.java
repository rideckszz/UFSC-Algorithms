public class PileVetor {
    private Integer[] dados;
    private int qt;

    PileVetor(int tamanho){
        dados = new Integer[tamanho];
        qt = 0;

    boolean vazia(){
        return qt == 0;
    }
    //Push
    void empilha(Integer item){
        if (qt < dados.length){
            dados [qt] = items;
            qt++
        }
    }
    //Pull
    Integer desempilha(){
        if (qt != 0){
            Integer item = dados[qt-1];
            qt--;
            return item;
        }
        return null;
    }
}