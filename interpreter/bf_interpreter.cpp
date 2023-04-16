#include <iostream>
using namespace std;

int main() {
    char c;
    string translations[26] = {
        "++++++[>++++++++++<-]>+++++.",  			// "A"
        "++++++[>++++++++++<-]>++++++.",   			// "B"
        "++++++[>++++++++++<-]>+++++++.",     		// "C"
        "++++++[>++++++++++<-]>++++++++.",      	// "D"
        "++++++[>++++++++++<-]>+++++++++.",     	// "E"
        "+++++++[>++++++++++<-]>.",        			// "F"
        "+++++++[>++++++++++<-]>+.",     			// "G"
        "+++++++[>++++++++++<-]>++.",    			// "H"
        "+++++++[>++++++++++<-]>+++.",         		// "I"
        "+++++++[>++++++++++<-]>++++.",         	// "J"
        "+++++++[>++++++++++<-]>+++++.",        	// "K"
        "+++++++[>++++++++++<-]>++++++.",       	// "L"
        "+++++++[>++++++++++<-]>+++++++.<",     	// "M"
        "+++++++[>++++++++++<-]>++++++++.",     	// "N"
        "+++++++[>++++++++++<-]>+++++++++.",    	// "O"
        "++++++++[>++++++++++<-]>.",      			// "P"
        "++++++++[>++++++++++<-]>+.",      			// "Q"
        "++++++++[>++++++++++<-]>++.",      		// "R"
        "++++++++[>++++++++++<-]>+++.",         	// "S"
        "++++++++[>++++++++++<-]>++++.",        	// "T"
        "++++++++[>++++++++++<-]>+++++.",       	// "U"
        "++++++++[>++++++++++<-]>++++++.",      	// "V"
        "++++++++[>++++++++++<-]>+++++++.",     	// "W"
        "++++++++[>++++++++++<-]>++++++++.",    	// "X"
        "++++++++[>++++++++++<-]>+++++++++.",    	// "Y"
        "+++++++++[>++++++++++<-]>.",          		// "Z"
    };

	// as letras podem ser escritas em caixa alta ou baixa, por�m a tradu��o remete apenas �s letras maiusculas.
    cout << "Digite um caractere: ";
    cin >> c;

    int index = (int)c - 97;
    if (index < 0 || index >= 26) {
        cout << "Caractere inv�lido." << endl;
    } else {
        cout << translations[index] << endl;
    }

    return 0;
}


//		Este c�digo � um programa em C++ que recebe um caractere do 
//		usu�rio e retorna uma tradu��o em Brainfuck para a letra 
//		correspondente do alfabeto, no entanto, em letras mai�sculas. 
//		O programa usa um array de strings para armazenar as tradu��es 
//		de cada letra do alfabeto em Brainfuck.
//		
//		O programa come�a declarando uma vari�vel c do tipo char para 
//		armazenar o caractere digitado pelo usu�rio. Em seguida, � 
//		definido um array de strings chamado translations que cont�m 
//		as tradu��es de cada letra do alfabeto em Brainfuck.
//		
//		Em seguida, o programa imprime uma mensagem pedindo ao usu�rio 
//		para digitar um caractere, l� o caractere digitado pelo usu�rio 
//		e calcula o �ndice correspondente no array translations subtraindo 
//		97 (o valor ASCII da letra 'a') do valor do caractere digitado. Se 
//		o �ndice calculado estiver fora dos limites do array translations, 
//		o programa imprime uma mensagem de erro, caso contr�rio, ele imprime 
//		a tradu��o correspondente em Brainfuck para a letra em quest�o.
//		
//		Por fim, o programa retorna 0, indicando que o 
//		programa foi executado com sucesso.

