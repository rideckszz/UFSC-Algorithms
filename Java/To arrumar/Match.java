

import javax.sound.sampled.SourceDataLine;

/*Desenvolva uma classe em Java que represente uma partida de futebol entre duas equipes. A classe deve se chamar Partida. Todos
os atributos da classe são privados.
 * 
 *
 * c) Desenvolva um método que retorne o nome da equipe vencedora do jogo. Em caso de empate o método deve retornar a String “empate”.
 * 
 * d) Desenvolva o método toString que deve retornar os nomes das equipes, os gols que cada equipe marcou, e o nome da equipe vencedora.
 */
public class Match {
    private String teamA;
    private String teamB;
    private int scoresA;
    private int scoresB;
    private String empate;
    
        public Match(String teamA, String teamB){
            this.teamA = "Brasil";
            this.teamB = "Bolivia";
            this.empate = "Empate";
        }
        void setScores(int scoresA, int scoresB){
            this.scoresA++;
            this.scoresB++;

        }
}



