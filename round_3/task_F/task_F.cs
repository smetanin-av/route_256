using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;

class Program
{
    static void Main(string[] args)
    {
        var numbers = Console
            .ReadLine()
            .Split(' ')
            .Select(RomanToArabic)
            .ToArray();

        var first = numbers[0];
        var second = numbers[1];

        if (first < second)
        {
            Console.WriteLine(-1);
        }
        else if (first == second)
        {
            Console.WriteLine(0);
        }
        else
        {
            Console.WriteLine(1);
        }
    }
}