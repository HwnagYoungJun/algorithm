using System;
using System.Collections.Generic;
using System.Text;

namespace a
{
    class Program
    {

        static StringBuilder sb;
        static int t, n, noFriend;
        static int[] student, areadyTeam;
        static List<int> team;

        static void dfs(int st)
        {
            areadyTeam[st] = 1;
            team.Add(st);
            int nextStudent = student[st];
            if (areadyTeam[nextStudent] == 1)
            {   
                if (team.Contains(nextStudent))
                {
                    int first = team.IndexOf(nextStudent);
                    int last = team.Count;
                    noFriend -= (last - first);
                    return;
                }
            }
            else
            {
                dfs(nextStudent);
            }
        }
        static void Main(string[] args)
        {
            sb = new StringBuilder();
            t = int.Parse(Console.ReadLine());
            for (int teseCase = 1; teseCase < t + 1; teseCase++)
            {
                n = int.Parse(Console.ReadLine());
                student = new int[n + 1];
                var temp = Console.ReadLine().Split();
                for (int i = 1; i < n + 1; i++)
                {
                    student[i] = int.Parse(temp[i - 1]);
                }
                noFriend = n;
                areadyTeam = new int[n + 1];
                for (int i = 1; i < n + 1; i++)
                {  
                    if (areadyTeam[i] == 1)
                    {
                        continue;
                    }
                    team = new List<int>();
                    dfs(i);
                }
                Console.WriteLine(noFriend);
            }
        }
    }
}
