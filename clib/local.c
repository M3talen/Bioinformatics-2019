#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "local.h"

#define MAX 2000
#define Match 3
#define MissMatch -2
#define GapPenalty -3

int SWArray[MAX][MAX];

int find_maximum(int p[], int n){
    int max = p[0];
    for(int i = 1; i < n; i++){
        if(p[i] > max){
            max = p[i];
        }
    }

    return max;
}

/* Swaps strings by swapping data*/
void swap2(char *str1, char *str2) 
{ 
  char *temp = (char *)malloc((strlen(str1) + 1) * sizeof(char)); 
  strcpy(temp, str1); 
  strcpy(str1, str2); 
  strcpy(str2, temp); 
  free(temp); 
}   

int run(char strA[],  char strB[]){
    swap2(strA, strB);
    int lenA = strlen(strA);
	int lenB = strlen(strB);

	//Create empty table
	for(int i=0;i<=lenA;++i){
		SWArray[0][i]=0;
	}
	for(int i=0;i<=lenB;++i){
		SWArray[i][0]=0;
	}

    int max = 0;
    int values[4] = {0};
    for(int i = 1; i <= lenA; ++i) {
		for(int j = 1; j <= lenB; ++j) {
            if(strA[i-1] == strB[j-1]){
                values[0] = (SWArray[i-1][j-1] + Match);
            }else{
                values[0] = (SWArray[i-1][j-1] + MissMatch);
            }

            values[1] = (SWArray[i-1][j] + GapPenalty);
            values[2] = (SWArray[i][j-1] + GapPenalty);

            SWArray[i][j] = find_maximum(values, 4);
            if(SWArray[i][j] > max){
                max = SWArray[i][j];
            }
        }
    }

    return max;
}

int * get_distance_matrix( char* data[], int N){
    int *matrix = (int *)calloc(N * N,  sizeof(int));
    for(int i = 0 ; i < N ; i++){
        for(int j = 0; j < N; j++){
            int score;
            if(*(matrix + j*N + i) == 0)
                score = run(data[i], data[j]);
            else
                score = *(matrix + j*N + i);

            *(matrix + i*N + j) = score; 
        }
    }
    return matrix;
}


///*MAIN FUNCTIONS*/
//int main()
//{
//     char *data[22];
//    data[0] = "CTGTAGAGCGAGTGTCAACGGGAC";
//    data[1] = "CTGTATGCTAAGAGCGAGTGTCATTTCTCGTTTCACTGTG";
//    data[2] = "CTGTATGCTAAGATTTCTCGGAGCTGGGGCGGCCG";
//    data[3] = "CTGAGAGCGAGTGTCA";
//    data[4] = "CTGTATAGAGCGAGTGTCATTTCGG";
//    data[4] = "CTGTATGCTAAGAGCGAGTGTCATTTCGG";
//    data[5] = "CTGTATGCTAAGAGCGAGTGTCGG";
//    data[6] = "CTGTATAAGAGCGAGTGTCATTTCGG";
//    data[7] = "CTGTATGCTAAGAGCGACATTTCGG";
//    data[8] = "CTGTATGCTAAGAGCGAGTGTTTCGG";
//    data[9] = "CTGTATGCTAAGAGCGAGTGTCATTTCGG";
//    data[10] = "CTGTATGCTAAGAGCGAGTGTCATTTCGG";
//    data[11] = "CTATGCTAAGAGCGAGTGTCATTTCGG";
//    data[12] = "CTGTATGCTAAGAGCGAGTGTCATTTCGG";
//    data[13] = "CTGTATGCTAAGAGCGAGTGTCATTTCGG";
//    data[14] = "CTGTATGCTAAGATCATTTCGG";
//    data[15] = "CTGTATGCTAAGAGCGAGTGTCATTTCGG";
//    data[16] = "CTGTATGCTAAGAGCGAGTGTCATTTCGG";
//    data[17] = "CTGTATGCTAAGAGCGAGTGTCATTTCGG";
//    data[18] = "CTGTATGCTAAGAGCGAGTGTCATTTCGG";
//    data[19] = "CTGTATGCTAAGAGCGAATTTCGG";
//    data[20] = "CGTATGCTAAGAGCGAGTGTCATTTCGG";
//    data[21] = "CTGTATGCTAAGAGCGAGTGTCGG";
//    int *matrix;
//    start = clock();
//    matrix = get_distance_matrix(data, 22);
//    end = clock();
//    cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
//
//    printf("time: %f s\n", cpu_time_used);
//    int N = 22;
//    for(int i = 0 ; i < N ; i++){
//        printf("\n");
//        for(int j = 0; j < N; j++){
//            printf("%5d", *(matrix + i*N + j));
//        }
//    }
//    printf("\n");
//	system("PAUSE");
//
//    return(0);
//}