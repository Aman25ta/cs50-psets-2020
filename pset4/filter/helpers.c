#include "helpers.h"
#include <math.h>
#include <stdio.h>



int limit(int RGB);

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    
    float Grey;
    for (int i = 0; i < width; i++)
    {
        for (int j = 0; j < height; j++)
        {
            // averages the color intensity and then applies the same value to all the colors to get gray
            Grey = round((image[j][i].rgbtBlue + image[j][i].rgbtGreen + image[j][i].rgbtRed) / 3.000);

            image[j][i].rgbtBlue = Grey;
            image[j][i].rgbtGreen = Grey;
            image[j][i].rgbtRed = Grey;
        }
    }
    
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    
    int sepiaBlue;
    int sepiaRed;
    int sepiaGreen;
    for (int i = 0; i < width; i++)
    {
        for (int j = 0; j < height; j++)
        {
            
            //with formula given
            sepiaBlue = limit(round(0.272 * image[j][i].rgbtRed + 0.534 * image[j][i].rgbtGreen + 0.131 * image[j][i].rgbtBlue));
            sepiaGreen = limit(round(0.349 * image[j][i].rgbtRed + 0.686 * image[j][i].rgbtGreen + 0.168 * image[j][i].rgbtBlue));
            sepiaRed = limit(round(0.393 * image[j][i].rgbtRed + 0.769 * image[j][i].rgbtGreen + 0.189 * image[j][i].rgbtBlue));

            image[j][i].rgbtBlue = sepiaBlue;
            image[j][i].rgbtGreen = sepiaGreen;
            image[j][i].rgbtRed = sepiaRed;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < (width / 2); j++)
        {
            RGBTRIPLE im = image[i][j];
            image[i][j] = image[i][width - (j + 1)];
            image[i][width - (j + 1)] = im;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }

    for (int i = 0, red, green, blue, counter; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            red = green = blue = counter = 0;

            if (i >= 0 && j >= 0)
            {
                red += copy[i][j].rgbtRed;
                green += copy[i][j].rgbtGreen;
                blue += copy[i][j].rgbtBlue;
                counter++;
            }
            if (i >= 0 && j - 1 >= 0)
            {
                red += copy[i][j-1].rgbtRed;
                green += copy[i][j-1].rgbtGreen;
                blue += copy[i][j-1].rgbtBlue;
                counter++;
            }
            if ((i >= 0 && j + 1 >= 0) && (i >= 0 && j + 1 < width))
            {
                red += copy[i][j+1].rgbtRed;
                green += copy[i][j+1].rgbtGreen;
                blue += copy[i][j+1].rgbtBlue;
                counter++;
            }
            if (i - 1 >= 0 && j >= 0)
            {
                red += copy[i-1][j].rgbtRed;
                green += copy[i-1][j].rgbtGreen;
                blue += copy[i-1][j].rgbtBlue;
                counter++;
            }
            if (i - 1 >= 0 && j - 1 >= 0)
            {
                red += copy[i-1][j-1].rgbtRed;
                green += copy[i-1][j-1].rgbtGreen;
                blue += copy[i-1][j-1].rgbtBlue;
                counter++;
            }
            if ((i - 1 >= 0 && j + 1 >= 0) && (i - 1 >= 0 && j + 1 < width))
            {
                red += copy[i-1][j+1].rgbtRed;
                green += copy[i-1][j+1].rgbtGreen;
                blue += copy[i-1][j+1].rgbtBlue;
                counter++;
            }
            if ((i + 1 >= 0 && j >= 0) && (i + 1 < height && j >= 0))
            {
                red += copy[i+1][j].rgbtRed;
                green += copy[i+1][j].rgbtGreen;
                blue += copy[i+1][j].rgbtBlue;
                counter++;
            }
            if ((i + 1 >= 0 && j - 1 >= 0) && (i + 1 < height && j - 1 >= 0))
            {
                red += copy[i+1][j-1].rgbtRed;
                green += copy[i+1][j-1].rgbtGreen;
                blue += copy[i+1][j-1].rgbtBlue;
                counter++;
            }
            if ((i + 1 >= 0 && j + 1 >= 0) && (i + 1 < height && j + 1 < width))
            {
                red += copy[i+1][j+1].rgbtRed;
                green += copy[i+1][j+1].rgbtGreen;
                blue += copy[i+1][j+1].rgbtBlue;
                counter++;
            }

            image[i][j].rgbtRed = round(red / (counter * 1.0));
            image[i][j].rgbtGreen = round(green / (counter * 1.0));
            image[i][j].rgbtBlue = round(blue / (counter * 1.0));
        }
    }

    return;
}


int limit(int RGB)
{
    if (RGB > 255)
    {
        RGB = 255;
    }
    return RGB;
}