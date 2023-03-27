public class Caderno{
    int numMaterias;
    int numFolhas;
    int idCaderno;
    double precoCaderno;
    
    Caderno(int numMaterias, int numFolhas, int idCaderno, double precoCaderno){
        set_numMaterias(numMaterias);
        set_numFolhas(numFolhas);
        set_idCaderno(idCaderno);
        set_precoCaderno(precoCaderno);
    }
    
    public void set_numMaterias(int numMaterias){
        this.numMaterias = numMaterias;
    }
    
    public void set_numFolhas(int numFolhas){
        this.numFolhas = numFolhas;
    }
    
    public void set_idCaderno(int idCaderno){
        this.idCaderno = idCaderno;
    }

    public void set_precoCaderno(double precoCaderno){
        this.precoCaderno = precoCaderno;
    }
    
    public int get_numMaterias(){
        return this.numMaterias;
    }
    
    public int getnumFolhas(){
        return this.numFolhas;
    }
    
    public int get_idCaderno(){
        return this.idCaderno;
    }
    
    public double get_precoCaderno(){
        return this.precoCaderno;
    }
    
    @Override
    public String toString(){
        return "Id Caderno: " + this.idCaderno + "\nNúmero de matérias : " + this.numMaterias + "\nNúmero de folhas: " + this.numFolhas + "\nPreço: " + this.precoCaderno;
    }
}