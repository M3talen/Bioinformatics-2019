#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "alignment.h"

#define MATCH 5
#define MISMATCH -3
#define GAP -5

int find_maximum(int p[], int n)
{
    int max = p[0];
    for(int i = 1; i < n; i++){
        if(p[i] > max){
            max = p[i];
        }
    }
    return max;
}

void swap(char *str1, char *str2) 
{ 
  char *temp = (char *)malloc((strlen(str1) + 1) * sizeof(char)); 
  strcpy(temp, str1); 
  strcpy(str1, str2); 
  strcpy(str2, temp); 
  free(temp); 
}   

int global_score(char genA[], char genB[]){
    int rows = strlen(genA) + 1;
	int cols = strlen(genB) + 1;
    int *matrix = calloc(rows * cols, sizeof(int));
    
    for(int i = 0; i < rows; i++)
        *(matrix + i*rows) = GAP * i;
    
    for(int j = 0; j < cols; j++)
        *(matrix + j) = GAP * j;

    int values[3] = {0};
    int score;
    for(int i = 1; i < rows; i++) {
		for(int j = 1; j < cols; j++) {
            if(genA[i-1] == genB[j-1]){
                score = MATCH;
            } else {
                score = MISMATCH;
            }

            values[0] = *(matrix + i*rows + j-1) + GAP;
            values[1] = *(matrix + (i-1)*rows + j) + GAP;
            values[2] = *(matrix + (i-1)*rows + j-1) + score;

            *(matrix + i*rows + j) = find_maximum(values, 3);
        }
    }
    int res = (int) *(matrix + (rows - 1)*rows + cols - 1);
    free(matrix);
    return res;
}

int local_score(char strA[],  char strB[]){
    int lenA = strlen(strA) + 1;
	int lenB = strlen(strB) + 1;
    if(lenA > lenB){
        swap(strA, strB);
        lenA = strlen(strA) + 1;
        lenB = strlen(strB) + 1;
    }

    int *matrix = calloc(lenA * lenB, sizeof(int));

	//Create empty table
	for(int i=0;i<lenA;++i){
		*(matrix + i*lenA)=0;
	}
	for(int j=0;j<lenB;j++){
		*(matrix + j) = 0;
	}

    int max = 0;
    int values[4] = {0};
    int score;
    for(int i = 1; i < lenA; ++i) {
		for(int j = 1; j < lenB; ++j) {
            if(strA[i-1] == strB[j-1]){
                score = MATCH;
            }else{
                score = MISMATCH;
            }

            values[0] = *(matrix + (i-1)*lenA + j) + GAP;
            values[1] = *(matrix + i*lenA + j-1) + GAP;
            values[2] = *(matrix + (i-1)*lenA + j-1) + score;

            *(matrix + i*lenA + j) = find_maximum(values, 4);
            if(*(matrix + i*lenA + j) > max){
                max = *(matrix + i*lenA + j);
            }
        }
    }
    free(matrix);
    return max;
}