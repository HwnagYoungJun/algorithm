using System;
using System.Collections.Generic;
namespace _2468
{
    class Program
    {
        struct Pos
        {
            public int x;
            public int y;
            
            public Pos(int x, int y)
            {
                this.x = x;
                this.y = y;
            }
        }
        static void BFS(int x, int y, int rain, int[,] map, int[,] visit)
        {
            Queue<Pos> deq = new Queue<Pos>();
            deq.Enqueue(new Pos(x, y));
            visit[y, x] = 1;
            Pos d;
            int nx, ny;
            while (deq.Count != 0) {
                d = deq.Dequeue();
                for (int w = 0; w < 4; w++)
                {
                    ny = d.y + dy[w];
                    nx = d.x + dx[w];
                    if (ny < 0 || ny >= n || nx < 0 || nx >= n) continue;
                    if (visit[ny, nx] == 1) continue;
                    if (map[ny, nx] <= rain) continue;
                    visit[ny, nx] = 1;
                    deq.Enqueue(new Pos(nx, ny));
                }
            }
        }

        static int n, maxHeight, safeArea, result;
        static int[,] map, visit;
        static int[] dy = {-1, 1, 0, 0};
        static int[] dx = {0, 0, -1, 1};
        static void Main(string[] args)
        {
            n = int.Parse(Console.ReadLine());
            maxHeight = -1;
            map = new int[n, n];
            for (int i = 0; i < n; i++)
            {
                var inputs = Console.ReadLine().Split();
                for (int j = 0; j < n; j++)
                {
                    map[j, i] = int.Parse(inputs[j]);
                    maxHeight = Math.Max(maxHeight, map[j, i]);
                }
            }

            safeArea = 0;
            for (int rain = 0; rain < maxHeight; rain++)
            {
                result = 0;
                visit = new int[n, n];
                for (int y = 0; y < n; y++)
                {
                    for (int x = 0; x < n; x ++)
                    {   
                        if (map[y, x] <= rain) continue;
                        if (visit[y, x] == 1) continue;
                        result++;
                        BFS(x, y, rain, map, visit);
                    }
                }
                safeArea = Math.Max(result, safeArea);
            }
            Console.WriteLine(safeArea);
        }
    }
}
