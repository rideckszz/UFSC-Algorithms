public class Animal {
    protected String nome, especie, familia;
    protected int idade;

    Animal (String n, String e, String f, int i){
        this.nome = n;
        this.especie = e;
        this.familia = f;
        this.idade = i;
    }
    void alimentar(){
        System.out.println("Alimentou um animal");
    }
}
