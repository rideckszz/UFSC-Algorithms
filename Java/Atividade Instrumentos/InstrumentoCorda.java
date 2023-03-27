public abstract class InstrumentoCorda extends Instrumento{
    public int ncordas;
    
    InstrumentoCorda(int ncordas){
        setCordas(ncordas);
    }
    
    void setCordas(int n){
        if (n >= 1) this.ncordas = n;
        else this.ncordas = 1;
    }

}
