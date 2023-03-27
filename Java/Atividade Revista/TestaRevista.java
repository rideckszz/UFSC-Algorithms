public class TestaRevista {
  public static void main(String[] args) {
    Revista r = new Revista();

    Figurinha f1 = new Figurinha("Alextraza", 274);
    Figurinha f2 = new Figurinha("Nozdormo", 395);
    Figurinha f3 = new Figurinha("Ysera", 150);
    Figurinha f4 = new Figurinha("Chromie", 120);
    Figurinha f5 = new Figurinha("Wrathion", 456);

    r.addFigurinha(f1);
    r.addFigurinha(f2);
    r.addFigurinha(f3);
    r.addFigurinha(f4);
    r.addFigurinha(f5);

    r.imprimeFigurinhas();
    System.out.println(r.retornaIndice(f2));
    r.removeFigurinha(0);

    r.imprimeFigurinhas();
  }
}
