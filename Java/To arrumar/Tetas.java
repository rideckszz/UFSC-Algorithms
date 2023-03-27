public class Tetas{
    private String titulo, genero;
    private  int faixaEtaria;

    Filme(String titulo, String gen, int faixa){
        this.titulo = titulo;
        setGenero(gen);
        this.faixaEtaria = faixa;

    }

    void setGenero(String, gen){
        if (gen.equals("Acao") || gen.equals("Comedia") || gen.equals("Romance")) 
        this.genero = gen;

        else
            this.genero = "Nao classificado";

    }

    public String toString(){
        return "Nome: " + this.titulo + "Genero: " + this.genero
    } 
 
}