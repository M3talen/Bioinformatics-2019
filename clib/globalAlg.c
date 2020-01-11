#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "globalAlg.h"

#define MATCH 5
#define MISMATCH -3
#define GAP -5

int find_maximum(int p[], int n){
    int max = p[0];
    for(int i = 1; i < n; i++){
        if(p[i] > max){
            max = p[i];
        }
    }
    return max;
}

int run(char genA[],  char genB[]){
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
