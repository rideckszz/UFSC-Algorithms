public class TestaLivro {
  public static void main(String[] args) {
    Autor a1 = new Autor("Benjamin", "Sáenz");
    Autor a2 = new Autor("Christie", "Golden");

    Livro l1 = new Livro("Aristótoles and Dante Dive into the Waters of the World", "Romance e Aventura", 47.5f, a1);
    l1.aplicaDesconto(0.5f);

    Livro e1 = new EBook("World of Warcraft: Tides of War", "Fantasia e Aventura", 50, a2);
    e1.aplicaDesconto(0.5f);

    System.out.println(l1);
    System.out.println(e1);

    l1.aplicaDesconto(0.1f);
    System.out.println(l1);
  }
}
