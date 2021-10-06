using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;

class Program
{
    static long IpAddressToLong(string address)
    {
        var result = 0L;
        foreach (var part in address.Split('.'))
        {
            result *= 256;
            result += int.Parse(part);
        }
        return result;
    }


    static void Main(string[] args)
    {
        var addresses = Console.ReadLine().Split(' ');
        var first = IpAddressToLong(addresses[0]);
        var second = IpAddressToLong(addresses[1]);
        var diff = Math.Abs(second - first);
        Console.WriteLine(diff);

    }
}