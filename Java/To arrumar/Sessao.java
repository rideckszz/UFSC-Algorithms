public class Sessao{
    private Tetas filme;
    private int numeroSala;
    private int assentosDisponiveis;
    private int hora;

    Sessao(Filme f, int n, int a, int h){
        this.filme = f;
        setNumeroSala(n);
        setAssentos(a);
        setHora(h);

    }

    setNumeroSala(int n){
        if (n >= 1 && n <= 10) this.numeroSala = n;
        else this.numeroSala = 1;
    } 

    setAssentos(int a) {
        if (n >= 1 && n <= 100) this.assentosDispoveis = a;
        else this.assentosDisponiveis = 100;


    }

    setHota(int h) {
        if ()
    }
}