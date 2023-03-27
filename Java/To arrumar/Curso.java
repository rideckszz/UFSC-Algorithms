public class Curso {
    private String nomeCurso;
    private Estudante01 estudante;

    //cuidar das limitacoes do exemplo

    Curso(String nome, Estudante01 e){
        this.nomeCurso = nome;
        this.estudante = e;

    }
    public String toString(){
        return this.nomeCurso + "Estudante: " + this.estudante;
    }
}   
