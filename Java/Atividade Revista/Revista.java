import java.util.ArrayList;

public class Revista {
  private ArrayList<Figurinha> list = new ArrayList<>();

  void addFigurinha(Figurinha f){
    if (!(list.contains(f))) list.add(f);
  }

  int retornaIndice(Figurinha f){
    for (int i = 0; i < list.size(); i++){
      Figurinha x = this.list.get(i);
      if (x.equals(f)) return i;
    } return -1;
  }

  void imprimeFigurinhas(){
    for (Figurinha f: list){
      System.out.println(f);
    }
  }

  void removeFigurinha(int indice){
    if (indice < list.size()) list.remove(indice);
  }
}
