public class TesteAnimal {
    public static void main (String [] args){
        Animal a = new Animal("Rex", "Canina","Mamifero", 1);

        a.alimentar();

        Mamifero m = new Mamifero("Mingal", "Felina","Animalea", 2, "pelo");

        m.alimentar();
    }
    
}
