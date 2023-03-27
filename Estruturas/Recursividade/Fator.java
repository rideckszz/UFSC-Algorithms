public class Fator{

    public static void aw(int n){
        if (n != 1) aw(n-1);
    }
    public static int fatorial(int n){
        if (n == 0)
            return 1;
        else
            return n * fatorial(n-1);
    }
    public static void main(String[] args) {
        System.out.print(fatorial(5) + " ");
    }

}
