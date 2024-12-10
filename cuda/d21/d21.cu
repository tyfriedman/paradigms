#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <cuda_runtime.h>

const int N = 1000;
const int MAX_LINE_LENGTH = 11;

/* a utility function to calculate the hash of part of a string */
/* given the inputs str: "abcdefg", start: 3, end: 6 */
/* this function will return the hash for "def" which is 193489332 */
__device__ unsigned int djb2_hash(const char *str, int start, int end) {
    unsigned int hash = 5381;
    int c;
    int i = start;
    str += start;
    while (i < end && (c = *str++)) {
        hash = ((hash << 5) + hash) + c; /* hash * 33 + c */
        i++;
    }
    return hash;
}

__global__ void djb2_hash_kernel(const char *input, int *inputLens, unsigned int *output) {
    int idx = blockIdx.x * blockDim.x + threadIdx.x;

    // this function should call djb2_hash() to calculate the hash for each input
    // remember, you do NOT need a loop here, a SINGLE LINE is sufficient
    // this is a SIMT situation, do not use a loop
    output[idx] = djb2_hash(input, 0, inputLens[idx]);
}


int main()
{    
    /*
     Your strategy here should be to:
     1) create memory space to put the text on the host
     2) read the file into that memory space, with each line as a string (input)
     3) store the length of each string in a separate int array (inputLens)
     4) put the strings into one giant string
     5) copy the "giant string" to the GPU
     6) run the djb2_hash_kernel
     7) get the output from the device back into the host (h_output)
     8) print the output to the screen (the for loop I provide below)
     */
    char lines[N][MAX_LINE_LENGTH];
    char *input = (char *)malloc(N * MAX_LINE_LENGTH * sizeof(char));
    int *inputLens = (int *)malloc(N * sizeof(int));
    
    FILE *file = fopen("random_strings.txt", "r");
    
    char buffer[MAX_LINE_LENGTH + 1];
    for (int i = 0; i < N; i++) {
        if (fgets(buffer, sizeof(buffer), file) != NULL) {
            int len = strlen(buffer);
            if (buffer[len - 1] == '\n') {
                buffer[len - 1] = '\0';
            }
            strcpy(input + (i * MAX_LINE_LENGTH), buffer);
            strcpy(lines[i], buffer);
            inputLens[i] = len;
        }
    }
    fclose(file);
    
    char *d_input;
    int *d_inputLens;
    unsigned int *d_output;
    cudaMalloc((void **)&d_input, N * MAX_LINE_LENGTH * sizeof(char));
    cudaMalloc((void **)&d_inputLens, N * sizeof(int));
    cudaMalloc((void **)&d_output, N * sizeof(unsigned int));
    cudaMemcpy(d_input, input, N * MAX_LINE_LENGTH * sizeof(char), cudaMemcpyHostToDevice);
    cudaMemcpy(d_inputLens, inputLens, N * sizeof(int), cudaMemcpyHostToDevice);
    
    djb2_hash_kernel<<<8, 125>>>(d_input, d_inputLens, d_output);

    unsigned int *output = (unsigned int *)malloc(N * sizeof(unsigned int));
    cudaMemcpy(output, d_output, N * sizeof(unsigned int), cudaMemcpyDeviceToHost);

    for (int i = 0; i < N; i++)
    {
        printf("%d: string %s hash %u\n", i, lines[i], output[i]);
    }
    
    free(input);
    free(inputLens);
    free(output);
    cudaFree(d_input);
    cudaFree(d_inputLens);
    cudaFree(d_output);

    return 0;
}
