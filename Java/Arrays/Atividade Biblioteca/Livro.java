

public class Livro {
    String autor, titulo;
    int npaginas;
    float preco;

    Livro(String titulo, String autor, int n, float preco){
        this.titulo = titulo;
        this.autor = autor;
        this.npaginas = n;
        this.preco = preco;

    }

    public boolean equals(Object o){
        if (this == o) return true;
        if (!(o instanceof Livro)) return false;
        Livro l = (Livro) o;
        return this.titulo.equals(l.titulo);
    }


    public String toString(){
        return "Titulo: " + this.titulo + "\nAutor: " + this.autor + "\nPáginas: " + this.npaginas + "\nPreço: " + this.preco + "R$";
    }

}
