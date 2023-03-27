import java.util.ArrayList;
public class Aquario {
  private ArrayList<Peixe> listaDePeixes = new ArrayList<>();

  void addPeixe(Peixe p){
    if (!listaDePeixes.contains(p)) listaDePeixes.add(p);
  }

  int buscaPeixe(Peixe p){
    for (int i = 0; i < listaDePeixes.size(); i++){
      Peixe x = this.listaDePeixes.get(i);
      if (x.equals(p)) return i;
    } return -1;
  }

  void imprimePeixe(){
    for (Peixe p: listaDePeixes){
      System.out.println(p + "\n");
    }
  }

  void removePeixe(int indice){
    if (indice < listaDePeixes.size()) listaDePeixes.remove(indice);
  }
}
