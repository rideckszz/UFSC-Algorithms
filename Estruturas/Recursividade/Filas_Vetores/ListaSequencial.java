/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

public class ListaSequencial {
    private Integer[] dados;
    private int qt;
    
    ListaSequencial(int tam){
        dados = new Integer[tam];
    }
    Integer removeLista(){
        if (qt != 0){
            qt--;
            Integer item = dados[qt];
            if (qt > 0 && qt == dados.length/4)
                resize(dados.length/2);
            
            return item;
        }
        return null;
    }
    Integer removePos(int i){
        if (i >= 0 && i < qt){
            Integer item = dados[i];
            for (int j= i; j < qt-1; j++){
                dados[j]=dados[j+1];
            }
            dados[qt-1] = null;
            qt--;
            return item;
    }
    return null;
}

    
    void resize(int max){
        Integer temp[] = new Integer[max];
        for (int i = 0; i < this.qt; i++) {
            temp[i] = this.dados[i];
        }
        this.dados = temp;
    }
    
    void insereLista(int novo){
    
        if (this.qt == dados.length)
            resize(dados.length * 2);
        dados[qt] = novo;
        qt++;
            
    }
    int quantidade(){
        return qt;
    }

    
    int posicao(Integer item){
        for (int i = 0; i < qt; i++)
            if (item == dados[i]) return i;
        return -1;  
    }
    
    boolean listaVazia(){
        if (qt == 0) return true;
        return false;
    }
            
    void imprimeLista(){
        for (int i = 0; i < qt; i++)
            System.out.print(dados[i] + "=>");
        System.out.println("comprimento - " + dados.length);
    }
}
