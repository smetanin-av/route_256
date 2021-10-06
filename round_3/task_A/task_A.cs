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
        var words = Console.ReadLine().Split(' ');
        for (var index = 0; index < words.Length; index++)
        {
            var word = words[index];
            words[index] = Capitalize(word);
        }

        var sentence = String.Join(" ", words);
        Console.WriteLine(sentence);
    }

    static string Capitalize(string value)
    {
        if (String.IsNullOrEmpty(value))
        {
            return value;
        }

        var first = value[0].ToString().ToUpper();
        var rest = value.Substring(1).ToLower();
        return String.Concat(first, rest);
    }
}