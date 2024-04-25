import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
    public void DFS(int n, int v, int[][] graph, int[] visited){
        System.out.print(v+" ");
        for(int i = 1;i<=n;i++){
            if(visited[i]==0 && graph[v][i]==1){
                visited[i] = 1;
                DFS(n, i, graph, visited);
            }
        }
    }
    public void BFS(int n, int v, int[][] graph, int[] visited){
        Queue<Integer> q = new LinkedList<>();
        q.add(v);
        visited[v] = 1;

        while(!q.isEmpty()){
            int tmp = q.poll();
            System.out.print(tmp+" ");

            for(int i =1;i<=n;i++){
                if(visited[i]==0 && graph[tmp][i]==1){
                    visited[i]=1;
                    q.add(i);
                }
            }
        }


    }
    public static void main(String[] args){
        Main T = new Main();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int v = sc.nextInt();

        int[][] graph= new int[n+1][n+1];
        int[] visited = new int[n+1];
        for(int i=0;i<m;i++){
            int a = sc.nextInt();
            int b = sc.nextInt();
            graph[a][b] = 1;
            graph[b][a] = 1;
        }
        visited[v] =1;
        T.DFS(n,v,graph,visited);
        System.out.println();
        Arrays.fill(visited,0);
        T.BFS(n,v,graph,visited);

    }
}
