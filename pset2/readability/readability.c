#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

int main(void)
{
    string text = get_string("Text: ");
    int nolet = 0;
    int noword = 1;
    int nosent = 0;
        
    for(int i = 0, n = strlen(text); i < n; i++)
    {
        if(isalpha(text[i]))
        {
            nolet++;
        }


        if(isspace(text[i]))
        {
            noword++;
        }


        if(text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            nosent++;
        }


    }
    
    //the index
    //float L = (100*(float)nolet / (float)noword );
    //float S = (100*(float)nosent / (float)noword );
    //float index = 5.88 * L - 0.296 * S - 15.8;
    int index  =round (0.0589 * (100* nolet / (float)noword ) - 0.296 * (100* nosent / (float)noword ) - 15.8);
    
    if (index < 16 && index >= 0)
    {
        printf("Grade %i\n",index );
    }
    else if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Before Grade 1\n");
    }

    
    //printf("letter(s) %i", nolet);
    //printf("\n");
    //printf("Word(s) %i", noword );
    //printf("\n");
    //printf("Sentance(s) %i", nosent);
    //printf("\n");

}