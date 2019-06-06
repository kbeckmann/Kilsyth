#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    FILE *f = fopen(argv[1], "rb");
    unsigned char buf[10240];
    unsigned char prev;
    size_t pos = 0;
    int done = 0;

    if (!f)
        return 1;

    fread(&prev, 1, 1, f);
    pos++;
    while(!done) {
        int ret = fread(buf, sizeof(buf), 1, f);
        if (ret != 1) {
            done = 1;
        }
        for (int i = 0; i < sizeof(buf); i++) {
            if ((prev + 1) % 256 != buf[i]) {
                fprintf(stderr, "Diff at %i {%02x != %02x)\n", pos, buf[i], prev);
                return -1;
            }
            prev = buf[i];
            pos++;
        }
    }

    printf("OK!\n");

    return 0;
}
