/* 
    Author : Zvonimir Kuciš
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "alignment.h"

#define MATCH 0
#define MISMATCH -1
#define GAP -1

/*
    Find maximum value in array of n integers.
*/
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

/*
    Print similarity matrix bewteen two sequences
*/
void print_matrix(int *matrix, int rows, int cols){
    for(int i = 0; i < rows; i++) {
        printf("\n");
		for(int j = 0; j < cols; j++) {
            printf("%5d", *(matrix + i*cols + j));
        }
    }
    printf("\n");
}

/*
    Run Needleman-Wunsch algorithm on genA and genB
*/
int global_score(char genA[], char genB[]){
    int rows = strlen(genA) + 1;
	int cols = strlen(genB) + 1;

    // Populate matrix 
    int *matrix = calloc(rows * cols, sizeof(int));
    for(int i = 0; i < rows; i++)
        *(matrix + i*cols) = GAP * i;
    
    for(int j = 0; j < cols; j++)
        *(matrix + j) = GAP * j;


    int values[3] = {0};
    int score;
    // Calculate similarity
    for(int i = 1; i < rows; i++) {
		for(int j = 1; j < cols; j++) {
            if(genA[i-1] == genB[j-1]){
                score = MATCH;
            } else {
                score = MISMATCH;
            }

            values[0] = *(matrix + i*cols + j-1) + GAP;
            values[1] = *(matrix + (i-1)*cols + j) + GAP;
            values[2] = *(matrix + (i-1)*cols + j-1) + score;
            *(matrix + i*cols + j) = find_maximum(values, 3);
        }
    }
    int res = (int) *(matrix + (rows - 1)*cols + cols - 1); // Last element in matrix
    free(matrix); // Free memory
    return res;
}

/*
    Run Smith-Waterman algorithm on genA and genB
*/
int local_score(char genA[],  char genB[]){
    int rows = strlen(genA) + 1;
	int cols = strlen(genB) + 1;

    //Initialize matrix
    int *matrix = calloc(rows * cols, sizeof(int));
    
    int max = 0;
    int values[4] = {0};
    int score;
    
    //Calculate similarity
    for(int i = 1; i < rows; ++i) {
		for(int j = 1; j < cols; ++j) {
            if(genA[i-1] == genB[j-1]){
                score = MATCH;
            }else{
                score = MISMATCH;
            }

            values[0] = *(matrix + (i-1)*cols + j) + GAP;
            values[1] = *(matrix + i*cols + j-1) + GAP;
            values[2] = *(matrix + (i-1)*cols + j-1) + score;

            *(matrix + i*cols + j) = find_maximum(values, 4); 
            if(*(matrix + i*cols + j) > max){
                max = *(matrix + i*cols + j); //Find maximum
            }
        }
    }
    free(matrix); // Free memory
    return max;
}