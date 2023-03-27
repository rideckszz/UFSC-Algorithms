public class Estudante {
    private String nome;
    private int mat;
    private Endereco endereco;

    Estudante (int m, String n, int num, String nome) {
        this.mat = m
        this.nome = n;
        this.endereco = new Endereco (num, nome);
    }

    Estudante (int m, String n, Endereco e) {
        this.mat = m
        this.nome = n;
        this.endereco = e;
    }

    public String toString() {
        return "Matricula: " + this.mat + "Aluno: " + this.nome + "Endereco: " + this.endereco;
    }

}
