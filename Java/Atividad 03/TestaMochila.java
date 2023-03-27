public class TestaMochila{
    double precoEstojo;
    double precoMochila;
    double precoCaderno;
    public static void main (String [] args){
        double precoEstojo;
        double precoMochila;
        double precoCaderno;
        Caderno caderno01 = new Caderno(20, 300, 8, 30.5);
        Estojo estojo01= new Estojo(100 ,8, 100);
        Mochila mochila01 = new Mochila (caderno01, estojo01, 430.5);
        double soma = precoEstojo + precoMochila + precoCaderno;
        System.out.println(mochila01);
        System.out.println(soma);
    }
}