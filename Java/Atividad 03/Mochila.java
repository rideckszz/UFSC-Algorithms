public class Mochila{
    Estojo estojo;
    Caderno caderno;
    double precoMochila;
    
    Mochila(Caderno caderno, Estojo estojo, double precoMochila){
        this.caderno = caderno;
        this.estojo = estojo;
        set_precoMochila(precoMochila);
    }
    
    public double get_precoMochila(){
        return precoMochila;
    }

    public void set_precoMochila(double precoMochila){
        this.precoMochila = precoMochila;
    }

    
    
    @Override
    public String toString(){
        return caderno + "\n" + estojo + "\nValor da Mochila: " + precoMochila;
    }
    
}