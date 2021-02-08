#include <stdio.h>
#include <cs50.h>

int main (void)
{
        int n;
    //Getting size for pyramid
    do
    {
        n = get_int("Size: ");
    }
    while (n < 1 || n > 8);
    //creating height and width for half pyramids using spaces
    for (int i = 0; i < n; i = i+1)
    {
        for (int j = 0; j < n; j = j+1)
        {
            if (i + j < n - 1)
                printf(" ");
            else
                printf("#");  
        }
            printf("  ");
            for (int j = 0; j < n; j = j+1)
                {
                    if (n - i < j + 2)
                        printf("#");
                }       
                printf("\n");
    }
}