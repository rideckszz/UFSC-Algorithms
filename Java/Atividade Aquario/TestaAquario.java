public class TestaAquario {
    public static void main(String[] args) {

        Aquario aquario = new Aquario();

        Peixe p1 = new Peixe ("Baiacu",23.4);
        Peixe p2 = new Peixe ("Tilápia", 3.45);
        Peixe p3 = new Peixe ("Salmão", 25);
        Peixe p4 = new Peixe ("Atum", 15.2);


        a.addPeixe(p1);
        a.addPeixe(p2);
        a.addPeixe(p3);
        a.addPeixe(p4);

        a.imprimePeixe();
        System.out.println("Removido da lista");

        a.buscaPeixe(p4);
        a.removePeixe(1);

        a.imprimePeixe();
    }
}
