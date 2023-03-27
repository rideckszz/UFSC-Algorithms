public class TestaInstrumento{
    public static void main(String[] args){
        Orquestra o = new Orquestra();
        Instrumento [] coleção = new Instrumento[3];
        // Insturmento i = new Instrumento () -> NÃO FUNCIONA
        Guitarra g1 = new Guitarra();
        Viola v1= new Viola();
        Baixo b1 = new Baixo();
        
        coleção[0] = g1;
        coleção[1] = v1;
        coleção[2] = b1;

        for (Instrumento i: coleção)
            o.espetaculo(i);
    }
}
