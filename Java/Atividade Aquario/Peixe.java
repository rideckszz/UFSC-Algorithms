public class Peixe {
    private String especie;
    private double comprimento;

    public Peixe(String especie, double comprimento){
        this.especie = especie;
        setComprimento(comprimento);
    }
    public String getEspecie() {
      return especie;
    }
    public void setEspecie(String especie) {
      this.especie = especie;
    }
    public double getComprimento() {
      return comprimento;
    }
    public void setComprimento(double comprimento) {
      if (comprimento > 0) this.comprimento = comprimento;
    }

    @Override
    public String toString() {
        return "\nPeixe da espécie: " + especie + "\nTamanho: " +
        comprimento;
    }

    @Override
    public boolean equals(Object obj) {
      if (this == obj)
        return true;
      if (getClass() != obj.getClass())
        return false;
      Peixe other = (Peixe) obj;
      if (!especie.equals(other.especie))
        return false;
      if (Double.doubleToLongBits(comprimento) != Double.doubleToLongBits(other.comprimento))
        return false;
      return true;
    }

  }
