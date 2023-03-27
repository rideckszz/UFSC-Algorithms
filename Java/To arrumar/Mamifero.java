public class Mamifero extends Animal {
    protected String tipoPelagem;

    Mamifero(String n, String e, String f, int i, String tP){
        super (n,e,f,i);
        this.tipoPelagem = tP;

    }
    void  alimentar(){
        System.out.println("Alimentou na classe mamifero");
    }
}
