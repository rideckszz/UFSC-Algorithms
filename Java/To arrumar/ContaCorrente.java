public class ContaCorrente extends ContaBancaria{
    protected float limite;
    
    ContaCorrente(String agencia, int numero, String titular, float limite){
        super(agencia, numero, titular);
        setLimite(limite);
    }
    
    void setLimite(float limite){
        if (limite > 0) this.limite = limite;
        else this.limite = 0;
    }
    
    @Override
    boolean saque (float valor){
        if (valor >= 0){
            if (valor <= this.saldo + this.limite){
                this.saldo = this.saldo - valor;
                return true;
            }
        }
        return false;
    }

    
    @Override
    void transferePara(ContaBancaria destino, float valor){
        if (this.saque(valor)) 
            destino.deposito(valor);
    }
    
    @Override
    public String toString(){
        return "Conta Corrente " + super.toString() + "\nLimite:  " + this.limite;
    
    }

}