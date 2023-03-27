public class ContaBancaria{
    protected float saldo;
    protected String agencia;
    protected int numero;
    protected String titular;
    
    ContaBancaria(String agencia, int numero, String titular){
        this.agencia = agencia;
        this.numero = numero;
        this.titular = titular;
        this.saldo = 0;
    }
    boolean saque(float valor){
        if (valor >= 0) {
            if (valor <= this.saldo){
                this.saldo = this.saldo - valor;
                return true;
            }
        }
        return false;
    }
    void deposito(float valor){
        if (valor > 0){
            this.saldo = this.saldo + valor;
        }
    }
    void transferePara(ContaBancaria destino, float valor){
        if (this.saque(valor)) 
            destino.deposito(valor);
    }
    
    @Override
    public String toString(){
        return "Agência: "+ this.agencia+ "\nNúmero da Conta: "+ this.numero+"\nCliente: "+this.titular+ "\nSaldo: "+ this.saldo;
    }

}