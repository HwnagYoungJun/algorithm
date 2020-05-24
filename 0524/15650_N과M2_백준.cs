using System;
using System.Collections.Generic;
using System.Text;
using System.Linq;

namespace _0524
{
    class Program
    {
        static StringBuilder stringBuilder;
        static int N, M;
        static int[] numList;
        static List<int> target;
        static void myCom(int n, int r, int k, int[] arr, List<int> result)
        {
            if (result.Count == r)
            {
                result.Reverse();
                stringBuilder.AppendLine("");
                foreach(int num in result)
                {
                    stringBuilder.Append($" {num}");
                }
                return;
            }
            if (k >= n)
            {
                return;
            }
            myCom(n, r, k + 1, arr, result);
            List<int> forConcat = new List<int>();
            forConcat.Add(arr[k]);
            List<int> temp = result.Concat(forConcat).ToList();
            myCom(n, r, k + 1, arr, temp);
        }
        static void Main(string[] args)
        {
            stringBuilder = new StringBuilder();
            var temp = Console.ReadLine().Split();
            N = int.Parse(temp[0]);
            M = int.Parse(temp[1]);
            numList = new int[N];
            for (int i = 0; i < N; i++)
            {
                numList[i] = i + 1; 
            }
            target = new List<int>();
            myCom(N, M, 0, numList, target);
            var tempString = stringBuilder.ToString();
            string q = new String(tempString.ToCharArray().Reverse().ToArray());
            Console.WriteLine(q);
        }
    }
}