public class Viola extends InstrumentoCorda {
    Viola(){
        super(4);
    }
    
    Viola(int n){
        super(n);
    }
    
    public void tocar(){
        System.out.println("Tocando viola");
    }


}

