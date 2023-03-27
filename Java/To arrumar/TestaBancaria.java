public class TestaBancaria{

    public static void main(String[] args){
        ContaPoupanca cp = new ContaPoupanca("Bradesco", 5367, "Pute", (float)30.05);
        ContaCorrente cc = new ContaCorrente("BB", 234, "Lux", 500);
        cc.transferePara(cp, 300);
        
        
        System.out.println(cp);
        System.out.println(cc);
    }
}