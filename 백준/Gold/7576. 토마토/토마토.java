import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

class Point{
    int x;
    int y;
    public Point(int x, int y){
        this.x  =x;
        this.y = y;
    }
}
public class Main {
    int answer = 0;
    int[] dx= {1,0,-1,0};
    int[] dy = {0,1,0,-1};
    boolean check  = true;
    public int BFS(int[][] box, int[][] visited, int n, int m){
        int day = 0;
        Queue<Point> q = new LinkedList<>();

        for(int i = 0;i<n;i++){
            for(int j = 0;j<m;j++){
                if(box[i][j]==1){
                    q.add(new Point(i,j));
                    visited[i][j] = 1;
                }
            }
        }
        while(!q.isEmpty()){
            int len = q.size();
//            for(Point x: q){
//                System.out.println(x.x+" "+x.y);
//            }
//            System.out.println(q);
            for(int j=0;j<len;j++){

                Point tmp = q.poll();
                int x = tmp.x;
                int y = tmp.y;

                for(int i=0;i<4;i++){
                    int mx = x+dx[i];
                    int my = y+dy[i];

                    if(mx>=0 && mx<n &&my>=0 &&my<m && box[mx][my]!=-1 && visited[mx][my]==0){
                        visited[mx][my] = 1;
                        q.add(new Point(mx,my));
                        box[mx][my]= 1;
                    }
                }
            }
            day++;
        }

        for(int i = 0;i<n;i++){
            for(int j = 0;j<m;j++){
                if(box[i][j]==0){
                    check = false;
                }
            }
        }
        if(check==false){
            answer = -1;
        }else{
            answer = day-1;
        }


        return answer;
    }
    public static void main(String[] args){
        Main T = new Main();
        Scanner sc = new Scanner(System.in);
        int m = sc.nextInt();
        int n = sc.nextInt();

        int[][] box = new int[n][m];
        int[][] visited = new int[n][m];
        for(int i=0;i<n;i++){
            for(int j = 0;j<m;j++){
                box[i][j] = sc.nextInt();
            }
        }
        System.out.println(T.BFS(box, visited,n,m));

    }
}
