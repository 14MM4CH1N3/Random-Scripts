/*
Made this as I was testing cracking in my penetration testing class
and I needed all 1.6 million permutations of a word to try in SSH 
bruteforcing (I forgot the word), should work with any word but takes exponetially
longer as the strings used get longer
*/

#include <stdio.h>
#include <string.h>

void swap_letter(char *a, char *b) {
    char temp = *a;
    *a = *b;
    *b = temp;
}

void make_permutations(FILE *file, char *string, int start, int end) {
    if (start == end) {
        fprintf(file, "%s\n", string);
        return;
    }
    for (int i = start; i <= end; i++) {
        swap_letter(string+start, string+i);
        make_permutations(file, string, start+1, end);
        swap_letter(string+start, string+i);
    }
}

int main() {
    char string[] = "<your-string-here>";
    int length = strlen(string);
    FILE *file = fopen("permutations.txt", "w");
    make_permutations(file, string, 0, length-1);
    fclose(file);
    return 0;
}