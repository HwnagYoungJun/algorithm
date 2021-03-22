using System;
using System.Collections.Generic;
using System.Text;

namespace _15649
{
    class Program
    {
        static int N, M;
        static int[] result; 
        static bool[] visit;
        static StringBuilder sb;       
        static void myPerm(int N, int M, int K, int[] result, bool[] visit)
        {
            if (K == M)
            { 
                foreach (int i in result)
                {
                    sb.Append(i + " ");
                }
                sb.Append('\n');
                return;
            }
            for (int j = 1; j < N + 1; j++)
            {
                if (visit[j]) continue;
                visit[j] = true;
                result[K] = j;
                myPerm(N, M, K + 1, result, visit);
                visit[j] = false;
            }
        }

        static void Main(string[] args)
        {
            var temp = Console.ReadLine().Split();
            N = int.Parse(temp[0]);
            M = int.Parse(temp[1]);
            result = new int[M];
            visit = new bool[N + 1];
            sb = new StringBuilder(); 
            myPerm(N, M, 0, result, visit);
            Console.WriteLine(sb.ToString());
        }
    }
}
