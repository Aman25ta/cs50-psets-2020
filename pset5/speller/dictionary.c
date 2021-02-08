// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

#define hsize 65536




typedef struct node
{
    char w[LENGTH + 1];
    struct node *next;
}
node;


void d(node *head);

int ds = 0;
node *htable[hsize];
unsigned int h(const char *w)
{
    unsigned int h = 0;
    for (int i = 0, n = strlen(w); i < n; i++)
        h = (h << 2) ^ w[i];
    return h % hsize;
}
bool check(const char *w)
{
    int lent = strlen(w);
    char l[lent + 1];
    for (int i = 0; i < lent; i++)
    {
        l[i] = tolower(w[i]);
    }
    l[lent] = '\0';
    
    int b = h(l);
    node *c = htable[b];
    while (c != NULL)
    {
        if (strcasecmp(c->w, l) != 0)
            c = c->next;
        else
            return true;
    }
    return false;
}
bool load(const char *dictionary)
{
    FILE *dic = fopen(dictionary, "r");
    if (dic == NULL)
    {
        fprintf(stderr, "Cound not open %s.\n", dictionary);
        return false;
    }
    
    char buffer[LENGTH + 1];
    
    while (fscanf(dic, "%s", buffer) != EOF)
    {
        node *temp = malloc(sizeof(node));
        strncpy(temp->w, buffer, sizeof(buffer));
        int index = h(buffer);
        if (htable[index] == NULL)
            htable[index] = temp;
        else
        {
            temp->next = htable[index];
            htable[index] = temp;
        }
        ds ++;
    }
    fclose(dic);
    return true;
}
unsigned int size(void)
{
    return ds;
}

bool unload(void)
{
    for (int i = 0; i < hsize; i++)
    {
        if (htable[i] != NULL)
        {    
            d(htable[i]);
        }
    }
    return true;
}




void d(node *head)
{
    if (head->next != NULL)
    {
        d(head->next);
    }
    free(head);
}