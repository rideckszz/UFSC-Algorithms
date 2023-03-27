public class Livro {
  private String nome, descricao;
  private float valor;
  private Autor autor;
  private boolean descontoAplicado = false;

  Livro(String nome, String descricao, float valor, Autor autor) {
    this.nome = nome;
    this.descricao = descricao;
    this.valor = valor;
    this.autor = autor;
  }

  void aplicaDesconto(float desconto){
    if (!(isDescontoAplicado())) {
      if (desconto <= 0.15 && desconto >= 0) {
        setValor(getValor() - (getValor() * desconto));
        descontoAplicado = true;
      } else {
        setValor(getValor() - (getValor() * 0.15f));
        descontoAplicado = true;
        }
    }
  }

  @Override
  public String toString() {
    return "Livro " + this.nome + "\n" + this.autor + "\nDescrição: " + this.descricao + "\nValor: " + this.valor + " reais";
  }

  public String getNome() {
    return nome;
  }
  public void setNome(String nome) {
    this.nome = nome;
  }
  public String getDescricao() {
    return descricao;
  }
  public float getValor() {
    return valor;
  }
  public void setValor(float valor) {
    this.valor = valor;
  }
  public Autor getAutor() {
    return autor;
  }
  public void setAutor(Autor autor) {
    this.autor = autor;
  }
  public boolean isDescontoAplicado() {
    return descontoAplicado;
  }
  public void setDescontoAplicado(boolean descontoAplicado) {
    this.descontoAplicado = descontoAplicado;
  }

}
