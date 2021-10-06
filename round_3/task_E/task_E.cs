using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;

class Program
{
    static Dictionary<char, int> _ROMAN_to_ARABIC = new Dictionary<char, int>
    {
        { 'M', 1000 },
        { 'D', 500 },
        { 'C', 100 },
        { 'L', 50 },
        { 'X', 10 },
        { 'V', 5 },
        { 'I', 1 },
        { 'N', 0 }
    };


    static int RomanToArabic(string number)
    {
        var arabic = 0;
        int? previous = null;
        foreach (var digit in number.ToUpper().Reverse())
        {
            var current = _ROMAN_to_ARABIC[digit];
            if (previous == null || current >= previous)
            {
                arabic += current;
            }
            else
            {
                arabic -= current;
            }
            previous = current;
        }
        return arabic;
    }

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