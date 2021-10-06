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
        var bills = Console
            .ReadLine()
            .Split(' ')
            .Select(int.Parse)
            .ToArray();

        var cashbox = new Dictionary<int, int>()
        {
            { 1000, 0 },
            { 2000, 0 },
            { 5000, 0 }
        };
        var has_changes = true;

        foreach (var bill in bills)
        {
            if (bill == 2000)
            {
                if (cashbox[1000] >= 1)
                {
                    cashbox[1000] -= 1;
                }
                else
                {
                    has_changes = false;
                }
            }
            else if (bill == 5000)
            {
                if (cashbox[2000] >= 2)
                {
                    cashbox[2000] -= 2;
                }
                else if (cashbox[2000] == 1 && cashbox[1000] >= 2)
                {
                    cashbox[2000] -= 1;
                    cashbox[1000] -= 2;
                }
                else if (cashbox[1000] >= 4)
                {
                    cashbox[1000] -= 4;
                }
                else
                {
                    has_changes = false;
                }
            }

            if (has_changes)
            {
                cashbox[bill] += 1;
            }
            else
            {
                break;
            }
        }

        Console.WriteLine(has_changes.ToString());
    }
}