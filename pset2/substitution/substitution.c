#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>
#include <math.h>


        //i realise i could have used letters such as i m or n in the variables instead of ia an ib, but my initial plan was to take each
        //charecter and assign it to the appropriate letter such as a=char1 b=char2 and so on but this was shorter in the end



int main(int argc, string argv[])
{
    int nolet = 0;
    
    
    
    //if input is not there or more than one word is given
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
    //no. of letters
    for(int ia = 0, na = strlen(argv[1]); ia < na; ia++)
    {
        if(isalpha(argv[1][ia]))
        {
            nolet++;
        }
        
    }
    //if less than 26 letters
    if(nolet != 26 )
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }
        

    if(nolet == 26)
    {
        //checking multiple usage of letters and if any other chars other than a-z are there
        string A = argv[1];
        for (int qa = 0; qa < 26; qa++)
        {
            if (A[qa] < 'A' || (A[qa] > 'Z' && A[qa] < 'a') || A[qa] > 'z')
            {
                printf("Key must contain 26 characters.\n");
                return 1;
            }
            
        
        for (int wa = (qa - 1); wa >= 0; wa--)
            {
                if (A[wa] == A[qa])
                {
                    printf("Key must contain 26 characters.\n");
                    return 1;
                }  
                if (A[wa] == A[qa] + 32)
                {
                    printf("Key must contain 26 characters.\n");
                    return 1;
                }
                if (A[wa] == A[qa] - 32)
                {
                    printf("Key must contain 26 characters.\n");
                    return 1;
                }
                    
            }
        for (int la = (qa + 1); la < 26; la++)
            {
                if (A[la] == A[qa])
                {
                    printf("Key must contain 26 characters.\n");
                    return 1;
                }
                if (A[la] == A[qa]  + 32)
                {
                    printf("Key must contain 26 characters.\n");
                    return 1;
                }
                if (A[la] == A[qa] - 32)
                {
                    printf("Key must contain 26 characters.\n");
                    return 1;
                }
            }
        }
        string plaintext = get_string("plaintext: ");
        int plainlen = strlen(plaintext);
        //substituting after the input checks out
        for (int ib = 0; ib < plainlen; ib++)
        {

            if (isupper(plaintext[ib]))
            {
                plaintext[ib] = toupper(A[plaintext[ib] - 65]);
            }
            else if (islower(plaintext[ib]))
            {
                plaintext[ib] = tolower(A[plaintext[ib] - 97]);
            }
        }

        printf("ciphertext: %s\n", plaintext);
        return 0;
    }
}




