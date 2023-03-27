public class TesteProva1 {
    public static void main (String [] args) {
        Estudante01 aluno = new Estudante01 ("Ana", 3 , 4 , 5);

        Curso tic = new Curso ("Curso - TIC\n", aluno);
        System.out.println (tic);

    }
}