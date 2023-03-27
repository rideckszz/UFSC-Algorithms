public class TestaRelogio{
    public static void main(String[] args){
        Relogio r = new Relogio(7, 59, 58);
        System.out.println(r);

        Relogio r2 = new Relogio(7, 59, 58);
        System.out.println(r2);


        r.equals (r);
        System.out.println(r.hora + ":" + r.minuto + ":" + r.segundo);
        r.passaSegundo();
        System.out.println(r.hora + ":" + r.minuto + ":" + r.segundo);
        r.passaSegundo();
        System.out.println(r.hora + ":" + r.minuto + ":" + r.segundo);

    }


}
