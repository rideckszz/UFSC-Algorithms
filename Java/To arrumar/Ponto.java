
//* */ construtor nao tem tipo
//* / todos os outros tem

public class Ponto{
    float x , y;
    //construtor

    Ponto(){
        this.x = 0;
        this.y = 0;
    }
    Ponto(float x){
        this.x = x;
        this.y = x;
    }

    Ponto(float x, float y){
        this.x = x;
        this.y = y;

    }

    public void move(float dx, float dy){
        x += dx;
        y += dy;


    }

}
