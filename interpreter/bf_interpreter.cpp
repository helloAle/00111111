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

	// as letras podem ser escritas em caixa alta ou baixa, porém a tradução remete apenas às letras maiusculas.
    cout << "Digite um caractere: ";
    cin >> c;

    int index = (int)c - 97;
    if (index < 0 || index >= 26) {
        cout << "Caractere inválido." << endl;
    } else {
        cout << translations[index] << endl;
    }

    return 0;
}


//		Este código é um programa em C++ que recebe um caractere do 
//		usuário e retorna uma tradução em Brainfuck para a letra 
//		correspondente do alfabeto, no entanto, em letras maiúsculas. 
//		O programa usa um array de strings para armazenar as traduções 
//		de cada letra do alfabeto em Brainfuck.
//		
//		O programa começa declarando uma variável c do tipo char para 
//		armazenar o caractere digitado pelo usuário. Em seguida, é 
//		definido um array de strings chamado translations que contém 
//		as traduções de cada letra do alfabeto em Brainfuck.
//		
//		Em seguida, o programa imprime uma mensagem pedindo ao usuário 
//		para digitar um caractere, lê o caractere digitado pelo usuário 
//		e calcula o índice correspondente no array translations subtraindo 
//		97 (o valor ASCII da letra 'a') do valor do caractere digitado. Se 
//		o índice calculado estiver fora dos limites do array translations, 
//		o programa imprime uma mensagem de erro, caso contrário, ele imprime 
//		a tradução correspondente em Brainfuck para a letra em questão.
//		
//		Por fim, o programa retorna 0, indicando que o 
//		programa foi executado com sucesso.

