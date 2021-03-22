using System;
using System.Collections.Generic;

namespace _1002
{
    class _5567_결혼식_백준
    {
        static int n, m;
        static Dictionary<int, List<int>> relation;
        static void BFS()
        {

        }

        static void Main(string[] args)
        {
            // input
            n = int.Parse(Console.ReadLine());
            m = int.Parse(Console.ReadLine());
            relation = new Dictionary<int, List<int>>();
            for (int i = 0; i < 5; i++)
            {
                var temp = Console.ReadLine().Split();
                var friend1 = int.Parse(temp[0]);
                var friend2 = int.Parse(temp[1]);
                relation[friend1].Add(friend2);
                relation[friend2].Add(friend1);
            }

        }
    }
}
