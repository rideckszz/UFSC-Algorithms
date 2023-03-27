public class Estudante01{
    private float nota1, nota2, nota3;
    private String nome;

    Estudante01(String nome, float n1, float n2, float n3){
        setNota1(n1);
        this.nota2 = n2; //correto fazer o setNota2
        this.nota3 = n3; //correto fazer o setNota3
        this.nome = nome;
    }
    float media(){
        return (this.nota1 + this.nota2 + this.nota3)/3;
    }

    //boolean tipo que poder receber verdadeiro ou falso
    boolean aprov(){
        if (media() >= 6) return true;
        else return false;
    }

    void setNota1(float n1){
        if (n1 >= 0 && n1 <= 10) this.nota1 = n1;
        else this.nota1 = 0;
    }
    public boolean equals(Object o){
        if (this == o) return true;
        if (!(o instanceof Estudante01)) return false;
        Estudante01 e = (Estudante01) o;
        return this.nome.equals(e.nome);

    }

    public String toString(){
        return this.nome + "\nNota 1: "+ this.nota1 + "\nNota 2: "+ this.nota2 + "\nNota SS3: "+ this.nota3 + "\nMédia: "+ this.media() + "\nAprovação: "+ this.aprov();


    }



}
