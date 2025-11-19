#include <stdio.h>
#include <ctype.h>


/*
 *
 * Implementando um hash table em c
 *
 */

#define MAX_INPUT 20

typedef struct {
    char *key;
    char *value;
} Map;

/*
typedef struct {
    Map map;
    Map *prevmap;
} LinkMap;
*/

int hashing(char *input);
int insertMap(Map map);
float getLoadFactor(Map *map);

Map hashtable[100];

int main(void) {
    Map ex = {
        "erik", 
        "o mais lindo do mundo"
    };

    printf("Hash de 'erik' é %d\n", hashing(ex.key));

    int index = insertMap(ex);

    printf("O valor de 'erik' é '%s'\n", hashtable[index].value);
    printf("LoadFactor é %.2f\n", getLoadFactor(hashtable)); 

    return 0;
}

int hashing(char *input) {
    int i, hash, j;

    hash = j = i = 0;

    do {
        j = isupper(input[i]) ? input[i] - 'A' + 1 : input[i] - 'a' + 1;
        hash = hash + j;

        ++i;
    } while (isalpha(input[i]) && input[i] != '\0');
/*
    for (i=0; i < MAX_INPUT - 1; ++i) {
        int j = input[i];
        if ('a'<= j <='z' || 'A'<= j <='Z')
            hash = hash + j;
    }
*/
    return hash;
}

int insertMap(Map map) {
    int index = hashing(map.key);
    hashtable[index] = map;

    return index;
}

float getLoadFactor(Map *map) {
    int entries;
    int i;

    entries = 0;
    for (i=0; i < 100;++i) {
        if (map[i].key!=NULL)
            ++entries;
    }

    return (float)entries/i;
}
