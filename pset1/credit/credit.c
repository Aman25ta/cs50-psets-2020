#include <stdio.h>
#include <cs50.h>

int main(void)
{
    long n;
    do
    {
       n = get_long("Number: ");
    }
    while (n <= 0);
    long countDigits = 0;
    long valid = n;
    while (valid > 0)
    {
        valid = valid / 10;
        countDigits++;
    }

    if (countDigits != 13 && countDigits != 15 && countDigits != 16)
    {
        printf("INVALID\n");
    }

    int digit1  =   (((n % 100) / 10) * 2);
    int digit2  =   (((n % 10000) / 1000) * 2);
    int digit3  =   (((n % 1000000) / 100000) * 2);
    int digit4  =   (((n % 100000000) / 10000000) * 2);
    int digit5  =   (((n % 10000000000) / 1000000000) * 2);
    int digit6  =   (((n % 1000000000000) / 100000000000) * 2);
    int digit7  =   (((n % 100000000000000) / 10000000000000) * 2);
    int digit8  =   (((n % 10000000000000000) / 1000000000000000) * 2);
    int digit9  =   (n % 10);
    int digit10 =   ((n % 1000) / 100);
    int digit11 =   ((n % 100000) / 10000);
    int digit12 =   ((n % 10000000) / 1000000);
    int digit13 =   ((n % 1000000000) / 100000000);
    int digit14 =   ((n % 100000000000) / 10000000000);
    int digit15 =   ((n % 10000000000000) / 1000000000000);
    int digit16 =   ((n % 1000000000000000) / 100000000000000);

    int check1  =   ((digit1 % 10) + (digit1 / 10));
    check1      =   check1 + (digit2 % 10) + (digit2 / 10);
    check1      =   check1 + (digit3 % 10) + (digit3 / 10);
    check1      =   check1 + (digit4 % 10) + (digit4 / 10);
    check1      =   check1 + (digit5 % 10) + (digit5 / 10);
    check1      =   check1 + (digit6 % 10) + (digit6 / 10);
    check1      =   check1 + (digit7 % 10) + (digit7 / 10);
    check1      =   check1 + (digit8 % 10) + (digit8 / 10);
    check1      =   check1 + (digit9 % 10) + (digit9 / 10);
    check1      =   check1 + (digit10 % 10) + (digit10 / 10);
    check1      =   check1 + (digit11 % 10) + (digit11 / 10);
    check1      =   check1 + (digit12 % 10) + (digit12 / 10);
    check1      =   check1 + (digit13 % 10) + (digit13 / 10);
    check1      =   check1 + (digit14 % 10) + (digit14 / 10);
    check1      =   check1 + (digit15 % 10) + (digit15 / 10);
    check1      =   check1 + (digit16 % 10) + (digit16 / 10);

    //if none
    if (check1 % 10 != 0)
    {
        printf("INVALID\n");
    }
    //if amex
    int amex = (n / 10000000000000);

    if (countDigits == 15)
    {
        if (amex != 34 && amex != 37)
        {
            printf("INVALID\n");
        }
        else
        {
            printf("AMEX\n");
        }

    }
    //visa for 13 digits
    if (countDigits == 13)
    {
        printf("VISA\n");
    }
    //visa for 16 digits


    if (countDigits == 16)
    {
        if ((digit8 / 2) == 4)
        {
            printf("VISA\n");
        }
        else
        {
            //mastercard check
            int mastercard = (n / 100000000000000);

            if (mastercard != 51 && mastercard != 52 && mastercard != 53 && mastercard != 54
                && mastercard != 55)
            {
                printf("INVALID\n");
            }
            else
            {
                printf("MASTERCARD\n");
            }
        }
    }


}