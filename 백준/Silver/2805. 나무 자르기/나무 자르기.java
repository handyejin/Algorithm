import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public long count(int capacity, int[] arr){
        long treeLength=0;
        for (int x: arr){
            if(x-capacity>0){
                treeLength += (x-capacity);
            }
//            System.out.println(treeLength);
        }
        return treeLength;
    }
    public int solution(int n, int m, int[] arr){
        int answer=0;
        int lt = 1;
        int rt = Arrays.stream(arr).max().getAsInt();

        int mid;
        long treeLength;
        while(lt<=rt){
            mid = (lt+rt)/2;
            treeLength = count(mid, arr);
//            System.out.println("capacity:"+mid+"treeLength:"+treeLength);
            if(treeLength>=m){
                answer = mid;
                lt = mid+1;
            }else{
                rt = mid-1;
            }
        }
        return answer;
    }
    public static void main(String[] ars){
        Main T = new Main();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] arr = new int[n];
        for(int i=0;i<n;i++){
            arr[i] = sc.nextInt();
        }
        System.out.print(T.solution(n,m,arr));

    }
}
