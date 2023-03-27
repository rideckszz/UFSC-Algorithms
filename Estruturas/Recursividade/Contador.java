public class Contador {
    public static void aw(int n){
        System.out.print(n + " ");
        if (n != 1) aw(n-1);
    }
    public static int cont(int n){
        if (n == 0)
            return 1;
        else
            return n * cont(n-1);
    }
    public static void main(String[] args) {
        aw(50);
    }
}
