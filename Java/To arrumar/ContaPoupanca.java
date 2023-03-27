public class ContaPoupanca extends ContaBancaria{
    protected float juros;
    
    ContaPoupanca(String agencia, int numero, String titular, float juros){
        super(agencia, numero, titular);
        this.juros = juros;
    }
    
    void setJuros(float juros){
        if (juros >= 0) this.juros = juros;
        else this.juros = 0;
    }
    
    void atualiza(){
        this.saldo = this.saldo * juros + this.saldo;
    }
    @Override 
    public String toString(){
        return super.toString() + "\nTaxa de Juros : "+ this.juros;
    }

}