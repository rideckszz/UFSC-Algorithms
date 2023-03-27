public class Estojo{
    int quantidadeMaterias;
    int idEstojo;
    double precoEstojo;
    
    Estojo(int quantidadeMateriais, int idEstojo, double precoEstojo){
        set_quantidadeMateriais(quantidadeMateriais);
        set_idEstojo(idEstojo);
        set_precoEstojo(precoEstojo);
    }
    
    public void set_quantidadeMateriais(int quantidadeMateriais){
        this.quantidadeMaterias = quantidadeMateriais;
    }
    
    public void set_idEstojo(int idEstojo){
        this.idEstojo = idEstojo; 
    }
    
    public void set_precoEstojo(double precoEstojo){
        this.precoEstojo = precoEstojo;
    }
    
    public int quantidadeMateriais(){
        return this.quantidadeMaterias;
    }
    
    public int idEstojo(){
        return idEstojo;
    }
    
    public double precoEstojo(){
        return precoEstojo;
    }
    @Override
    public String toString(){
        return "Id Estojo" + this.idEstojo  + "\nQuantidade de Materias" + this.quantidadeMaterias + "\nPreço : " + precoEstojo;
    }

}