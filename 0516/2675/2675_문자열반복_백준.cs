// <TIL>
// 1. C# 실행하는 방법
// 1-1 dotnet new console, dotnet run
// 2. 입력, 출력하는 방법

using System;
using System.Collections.Generic;

namespace _2675
{
    class Program
    {
        static void Main(string[] args)
        {
            int T = int.Parse(Console.ReadLine());
            // 입력은 Console.ReadLine()
            // int.Parse = JS : parseInt, python : int()
            for (int testCase = 1; testCase < T + 1; testCase++)
            {
                string[] temp = Console.ReadLine().Split(' ');
                // List<string>을 쓰면 python 처럼 사용할 수 있을것같다.
                int r = int.Parse(temp[0]);
                string s = temp[1];
                for (int i = 0; i < s.Length; i++)
                {
                    for (int j = 0; j < r; j++)
                    {
                        Console.Write(s[i]);
                    }
                }
                Console.WriteLine();
            }
        }
    }
}
