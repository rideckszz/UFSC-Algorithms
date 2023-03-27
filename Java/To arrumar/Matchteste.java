

public class Matchteste {
    public static void main (String[] args) {
        
        Match match = new Match("Brasil", "Bolivia");

        match.setScores(2,0);

        System.out.println(match.teamB);
        System.out.println(match.scoresA);
    }
}
