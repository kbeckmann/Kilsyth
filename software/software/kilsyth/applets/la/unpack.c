#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(int argc, char *argv[])
{
    FILE *f_in = fopen(argv[1], "rb");
    FILE *f_out = fopen(argv[2], "wb");
    char buf_in[1024*1024];
    char buf_out[4*1024*1024];
    char c = 0;
    int i = 0;
    size_t n;

    while ((n = fread(buf_in, 1, sizeof(buf_in), f_in)) != 0) {
        int j = 0;
        for (i = 0; i < n; i++) {
            c = buf_in[i];
            buf_out[j++] = (c     ) & 0x03;
            buf_out[j++] = (c >> 2) & 0x03;
            buf_out[j++] = (c >> 4) & 0x03;
            buf_out[j++] = (c >> 6) & 0x03;
        }

        fwrite(buf_out, 1, n * 4, f_out);
    }

    fclose(f_in);
    fclose(f_out);
    return 0;
}