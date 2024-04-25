import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public int count(long capacity, int[] arr){
        int cnt=0;
        int[] tmp = new int[arr.length];

        for(int i=0;i<arr.length;i++){
            tmp[i]= arr[i];
        }

        for(int i=0;i<arr.length;i++){
            while(tmp[i]-capacity>=0){
                tmp[i] = (int) (tmp[i]-capacity);
                cnt++;
            }
        }
        return cnt;
    }
    public long solution(int k, int n, int[] arr){
        long answer=0;
        long lt = 1;
        long rt = Arrays.stream(arr).max().getAsInt();
        long mid ;
        int cnt;

        while(lt<=rt){
            mid = (lt+rt)/2;
            cnt = count(mid,arr);
//            System.out.println("cnt:"+cnt+"capacity:"+mid);
            if(cnt<n){
                rt = mid-1;
            }else if(cnt>=n){
                lt = mid+1;
                answer = mid;
            }
        }
        return answer;
    }

    public static void main(String[] args){
        Main T = new Main();
        Scanner sc = new Scanner(System.in);
        int k = sc.nextInt();
        int n = sc.nextInt();

        int[] arr = new int[k];
        for(int i=0;i<k;i++){
            arr[i] = sc.nextInt();
        }
        System.out.println(T.solution(k,n,arr));
    }
}
