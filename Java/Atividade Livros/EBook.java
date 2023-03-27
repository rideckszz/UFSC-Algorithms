public class EbookMoodle extends LivroMoodle{
  public class EBook extends Livro{
    EBook(String nome, String descricao, float valor, Autor autor) {
      super(nome, descricao, valor, autor);
    }

    @Override
    void aplicaDesconto(float desconto) {
      if (!(isDescontoAplicado())) {
        if (desconto <= 0.3 && desconto >= 0) {
          setValor(getValor() - (getValor() * desconto));
          setDescontoAplicado(true);
        } else {
          setValor(getValor() - (getValor() * 0.3f));
          setDescontoAplicado(true);
          }
      }
    }
    @Override
    public String toString() {
      return super.toString();
    }
  }
