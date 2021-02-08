#include<stdio.h>
#include<stdlib.h>
#include<stdint.h>
#include<cs50.h>


#define size 512
typedef uint8_t BYTE;



int main(int argc, char *argv[])
{
    //printf("check\n");

    if (argc != 2)
    {
        printf("Usage: ./recover (name of file)\n ");
    }

    string infile = argv[1];



    FILE *file = fopen(infile, "r");
    if (file == NULL)
    {
        printf("Could not open %s.\n", infile);
        return 1;
    }
BYTE buffer[size];
int i;
i = 0;
FILE* img;
char pchar[8];

while (fread(buffer, sizeof(buffer), 1, file) == 1)
    {

        if(buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            if (i > 0)
            {

                fclose(img);
                sprintf(pchar,"%03d.jpg", i);
                i += 1;
                img = fopen(pchar, "w");
                fwrite(buffer, sizeof(buffer), 1, img);
            }
            if (i == 0)
            {
                sprintf(pchar,"%03d.jpg", i);
                i += 1;

                img = fopen(pchar, "w");

                fwrite(buffer, sizeof(buffer), 1, img);
            }



        }
        else if (i > 0)
        {

            fwrite(buffer, sizeof(buffer), 1, img);
        }


    }


    fclose(img);
    fclose(file);
    return 0;


}
