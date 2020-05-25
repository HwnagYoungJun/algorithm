// 1. C# 연습
// 2. 탐색 기초문제

using System;
using System.Collections.Generic;
namespace _1012
{
    class Program
    {
        static int T, M, N, K;
        static int[] dr = {-1, 1, 0, 0};
        static int[] dc = {0, 0, -1, 1};
        static void takeWarm(int x, int y, int[,] grape)
        {
            Queue<int> X = new Queue<int>();
            Queue<int> Y = new Queue<int>();
            X.Enqueue(x);
            Y.Enqueue(y);
            grape[x, y] = 1;

            while (X.Count != 0)
            {
                int row = Y.Dequeue();
                int col = X.Dequeue();
                for (int w = 0; w < 4; w++)
                {
                    int nr = row + dr[w];
                    int nc = col + dc[w];
                    if (nr < 0 || nr >= N || nc < 0 || nc >= M) continue;
                    if (grape[nc, nr] == 1)
                    {
                        grape[nc, nr] = 0;
                        X.Enqueue(nc);
                        Y.Enqueue(nr);
                    } 
                }
            }


        }
        static void Main(string[] args)
        {
            T = int.Parse(Console.ReadLine());

            for (int testCase = 0; testCase < T; testCase++) {

                var temp = Console.ReadLine().Split();
                // .Split(" ") 처럼써서 JS처럼해도 된다. Defalt는 space한칸
                M = int.Parse(temp[0]);
                N = int.Parse(temp[1]);
                K = int.Parse(temp[2]);
                int[,] map = new int[M, N];

                for (int i = 0; i < K; i++) 
                {
                    var xy = Console.ReadLine().Split();
                    int c = int.Parse(xy[0]);
                    int r = int.Parse(xy[1]);
                    map[c, r] = 1;
                }

                int warm = 0;
                for (int row = 0; row < N; row++)
                {
                    for (int col = 0; col < M; col++)
                    {
                        if (map[col, row] == 0) continue;
                        takeWarm(col, row, map);
                        warm++;
                    }
                }
                Console.WriteLine(warm);
            }
        }
        
    }
}
