#include <stdbool.h>

bool isIsomorphic(char* s, char* t) {
    int mapST[256] = {0};
    int mapTS[256] = {0};

    for (int i = 0; s[i] != '\0'; i++) {
        unsigned char charS = (unsigned char)s[i];
        unsigned char charT = (unsigned char)t[i];

        if (mapST[charS] == 0 && mapTS[charT] == 0) {
            mapST[charS] = charT + 1;
            mapTS[charT] = charS + 1;
        } else if (mapST[charS] != charT + 1 ||
                   mapTS[charT] != charS + 1) {
            return false;
        }
    }

    return true;
}