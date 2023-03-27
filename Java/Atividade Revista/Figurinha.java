public public class Figurinha {
  private String nomeJogador;
  private int numeracao;

  public Figurinha(String nomeJogador, int numeracao) {
    this.nomeJogador = nomeJogador;
    setNumeracao(numeracao);
  }

  public String getNomeJogador() {
    return nomeJogador;
  }
  public void setNomeJogador(String nomeJogador) {
    this.nomeJogador = nomeJogador;
  }
  public int getNumeracao() {
    return numeracao;
  }
  public void setNumeracao(int numeracao) {
    if (numeracao >= 0) this.numeracao = numeracao;
  }

  @Override
  public String toString() {
    return "Figurinha: " + nomeJogador + ", Numeração: " + numeracao;
  }

  @Override
  public boolean equals(Object obj) {
    if (this == obj) return true;
    if (obj == null) return false;
    if (getClass() != obj.getClass()) return false;
    Figurinha f = (Figurinha) obj;
    if (!nomeJogador.equals(f.nomeJogador)) return false;
    if (numeracao != f.numeracao) return false;
    return true;
  }
}
