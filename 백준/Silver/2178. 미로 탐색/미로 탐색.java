import java.io.BufferedReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
class Point{
    int x,y;
    public Point(int x, int y){
        this.x = x;
        this.y = y;
    }

}
public class Main {
    static int[][] miro;
    static int[][] visited;

    int[] dx = {1,0,-1,0};
    int[] dy = {0,1,0,-1};

    public void BFS(int n, int m){
        Queue<Point> q = new LinkedList<>();
        q.add(new Point(0,0));
        int cnt =1;
        visited[0][0] = 1;
        while(!q.isEmpty()){
            Point p = q.poll();

            int x = p.x;
            int y = p.y;
            cnt++;
//            if(x==n-1 && y ==m-1){
//                return cnt;
//            }
            for(int i=0;i<4;i++){
                int mx= x+dx[i];
                int my = y+dy[i];
                if(mx>=0 && mx<n &&my>=0&&my<m){
                    if(visited[mx][my]==0 && miro[mx][my]!=0){
                        visited[mx][my] = 1;
                        q.add(new Point(mx,my));
                        miro[mx][my] = miro[x][y]+1;
                    }
                }
            }
        }
    }
    public static void main(String[] args){
        Main T = new Main();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        miro = new int[n][m];
        visited = new int[n][m];

        for(int i=0;i<n;i++){
            String row = sc.next();
            for(int j=0;j<m;j++){
                miro[i][j] = row.charAt(j)-'0';
            }
        }
        T.BFS(n,m);

//        System.out.println(T.BFS(n,m));
        System.out.println(miro[n-1][m-1]);
    }
}
