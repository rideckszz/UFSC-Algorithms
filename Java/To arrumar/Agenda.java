public class Agenda {
    int dia, mes

    Agenda (int d, int m){

        setDiaMes (d, m);
    }
    void setDiaMes (int dia, int mes);
    // mes entre 1 e 12 
    // meses invalidos vai ser janeiro
    // mes 2 -> entre 1 28
    // mes 1 3 5 7 8 10 12- 1 e 31
    // mes 4 6 9 11 - 1 a 30

    if (mes >= 1 && mes <= 12){
        this.mes = mes;
        if (mes == 2)
            if (dia >= 1 && dia <= 28)
                this.dia = dia;
            else
                this.dia = 1;
        else
            if (mes == 4 || mes == 6 || mes == 9 || mes == 11)
                if (dia >= 1 && dia <= 30)
                    this.dia = dia;
                else
                    this.dia = 1;

            else
                if (dia >= 1 && dia <= 31)
                    this.dia = dia;
                else 
                    this.dia = 1;
    else
        this.mes = 1 ;
        this.dia = 1;
}