public class Circulo extends Ponto{
    private float raio;

    Circulo(float x, float y, float r){
        super(x,y); //Chamda do construtor do Ponto
        setRaio(r);

    }

    void setRaio(float r){
        if (r >= 0) this.raio = r;
        else this.raio = 0;

    }

    public String toString (){
        return "Círculo \n Raio: " + this.raio + "\n" + super.toString();
    }
    
}
