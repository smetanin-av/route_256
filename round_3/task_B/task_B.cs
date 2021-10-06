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
        var value = Console.ReadLine();
        var counts = new Dictionary<char, int>();
        var builder = new StringBuilder();
        foreach (var symbol in value)
        {
            int count = counts.ContainsKey(symbol) ? counts[symbol] : 0;
            builder.Append(count + 1);
            counts[symbol] = count + 1;
        }

        Console.WriteLine(builder.ToString());
    }
}