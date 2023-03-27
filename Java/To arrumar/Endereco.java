public class Endereco {
    
    private String nomeDaRua;
    private Endereco endereco;

    Endereco (int n, String Nome){
        this.num = n;
        this.nomeDaRua = nome;

    }

    void setNum (int n){
        this.num = n;

    }

    public String toString (){
        return "Rua: " + this.nomeDaRua + "Numero:" + this.num
    }
}