#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

int main(int argc, char *argv[])
{
    int f = open(argv[1], O_RDONLY);
    unsigned char buf[1<<20];
    uint16_t *buf16 = (uint16_t *) buf;
    unsigned int prev = 0;
    size_t pos = 0;
    int done = 0;
    int bps = 8; // bits per sample
    int overflow = 256;

    if (!f) {
        fprintf(stderr, "Can't open file %s\n", argv[1]);
        return -1;
    }

    if (argc >= 3) {
        if (!sscanf(argv[2], "%d", &bps)) {
            fprintf(stderr, "Usage: %s <file.bin> [8/16] [overflow value]\n", argv[0]);
            return -1;
        }
        overflow = 1 << bps;
    }

    if (argc >= 4) {
        if (!sscanf(argv[3], "%d", &overflow)) {
            fprintf(stderr, "Usage: %s <file.bin> [8/16] [overflow value]\n", argv[0]);
            return -1;
        }
    }

    read(f, &prev, bps / 8);
    pos++;
    int loops = sizeof(buf) / (bps / 8);
    while(!done) {
        int ret = read(f, buf, sizeof(buf));
        if (ret != sizeof(buf)) {
            done = 1;
            printf("EOF\n");
        }
        for (int i = 0; i < loops; i++) {
            unsigned int current;
            if (bps == 8) {
                current = buf[i];
            } else {
                current = buf16[i];
            }
            unsigned int check = (prev + 1) % overflow;
            if (check != current) {
                if (bps == 8)
                    fprintf(stderr, "Diff at %i {%02x != %02x)\n", pos, current, check);
                else
                    fprintf(stderr, "Diff at %i {%04x != %04x)\n", pos, current, check);
                return -1;
            }
            prev = current;
            pos++;
        }
    }

    printf("OK!\n");

    return 0;
}
