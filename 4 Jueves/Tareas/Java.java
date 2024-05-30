public class Java {

    public static void main(String[] args) {
        
        int lista [] = new int [3];

        lista [0] = 10;
        lista [1] = 5;
        lista [2] = 20;
        int mayor;
        int menor;
        for(int i =0;i < lista.length;i++){
            for(int j = 1; j < lista.length;j++){
                if(lista[i]>lista[j]&&lista[i]>lista[j-1]){    
                    mayor = lista[i];             
                    System.out.println("Numero mayor:"+mayor);
                    
                    menor = lista[j];

                    System.out.println("Menor"+menor);
                }
            }
            
        }

        
    }
}