package neu.lydia;

import java.security.KeyStore;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        // write your code here
    }

    //Q1
    public int searchInsert(int[] nums, int target) {
        int locate = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == target) {
                locate = i;
                break;
            } else if (nums[i] > target) {
                locate = i;
                break;
            } else {
                locate = nums.length;
            }
        }
        return locate;

    }


    //Q2
    public int[][] updateMatrix(int[][] mat) {
        int m = mat.length, n = mat[0].length;
        if (m == 0) return mat;
        int[][] f = new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (mat[i][j] == 1) {
                    f[i][j] = Integer.MAX_VALUE - 1;
                    if (i > 0)
                        f[i][j] = Math.min(f[i][j], f[i - 1][j] + 1);
                    if (j > 0)
                        f[i][j] = Math.min(f[i][j], f[i][j - 1] + 1);
                }
            }
        }
        for (int i = m - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                if (i < m - 1)
                    f[i][j] = Math.min(f[i][j], f[i + 1][j] + 1);
                if (j < n - 1)
                    f[i][j] = Math.min(f[i][j], f[i][j + 1] + 1);
            }
        }
        return f;
    }

    //Q3
    public int findMin(int[] nums) {
        int l = 0, r = nums.length - 1, mid;
        while (l < r) {
            mid = (l + r) / 2;
            if (nums[mid] > nums[l] && nums[r] > nums[mid]) {
                return nums[l];
            } else if (mid > 0 && nums[mid] < nums[mid - 1]) {
                return nums[mid];
            } else if (nums[mid] > nums[r]) {
                l = mid + 1;
            } else if(nums[mid]<nums[r]) {
                r = mid - 1;
            }
        }
        return nums[l];
    }

    //Q4
    public int minMeetingRooms(int[][] intervals) {
        if(intervals == null || intervals.length == 0)
            return 0;
        int rooms = 1;
        Arrays.sort(intervals, (m1, m2) -> m1[0] - m2[0]);
        for(int i = 0; i < intervals.length - 1; i++) {
            if(intervals[i+1][0] < intervals[i][1])
                rooms++;
        }
        return rooms;
    }

    //Q5
    public int[] topKFrequent(int[] nums, int k) {
        int[] rst = new int[k];
        HashMap<Integer, Integer> frequency = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            frequency.merge(nums[i], 1, Integer::sum);
        }
        ArrayList<Map.Entry<Integer, Integer>> entryList = new ArrayList<>(frequency.entrySet());
        entryList.sort((o1, o2) -> o2.getValue() - o1.getValue());
        for (int i = 0; i < k; i++) {
            rst[i] = entryList.get(i).getKey();
        }
        return rst;
    }

    //Q6
    public int threeSumClosest(int[] nums, int target) {

        Arrays.sort(nums);
        //System.out.println(Arrays.toString(nums));

        int threeSum = nums[0] + nums[1] + nums[2];

        for (int i = 0; i < nums.length - 2; i++) {
            int left = i+1;
            int right = nums.length - 1;

            while(left < right){
                int temp = nums[i] + nums[left] + nums[right];
                if (Math.abs(temp-target)<Math.abs(threeSum-target)){threeSum = temp;}

                if (temp>target){
                    right--;
                }else if (temp < target){
                    left++;
                }else{
                    return temp;
                }
            }
        }

        return threeSum;
    }

    //Q7
    public int[][] insert(int[][] intervals, int[] newInterval) {
        ArrayList<int[]> res=new ArrayList<>();
        int i=0;
        while(i<intervals.length&&newInterval[0]>intervals[i][1]){
            res.add(intervals[i]);
            i++;
        }
        int left=newInterval[0];
        if(i<intervals.length){
            left=Math.min(intervals[i][0],newInterval[0]);
        }
        int right=newInterval[1];
        while(i<intervals.length&&newInterval[1]>=intervals[i][0]){
            i++;
        }
        if(i>0) right=Math.max(right,intervals[i-1][1]);
        res.add(new int[]{left,right});
        while(i<intervals.length){
            res.add(intervals[i]);
            i++;
        }

        int ans[][]=new int[res.size()][2];
        for(int j=0;j<res.size();j++){
            ans[j]=res.get(j);
        }
        return ans;
    }

    //Q8
    public int eraseOverlapIntervals(int[][] arr) {
        if(arr.length <=1) return 0;
        Arrays.sort(arr,(a,b)->a[1]-b[1]);
        int count=1;
        int end=arr[0][1];
        for(int[] interval:arr){
            if(interval[0]>=end){
                count++;
                end=interval[1];
            }
        }
        return arr.length-count;
    }

    //Q9
    public int[][] intervalIntersection(int[][] firstList, int[][] secondList) {
        List<int[]> list = new ArrayList<>();
        int m = firstList.length;
        int n = secondList.length;
        int i = 0;
        int j = 0;
        while(i < m && j < n){
            int [] tmp = new int[2];
            int a = firstList[i][0];
            int b = firstList[i][1];
            int x = secondList[j][0];
            int y = secondList[j][1];
            tmp[0] = Math.max(a,x);
            tmp[1] = Math.min(b,y);
            if(tmp[1] >= tmp[0])
                list.add(tmp);
            if(y >= b){
                i++;
            }
            else{
                j++;
            }
        }
        return list.toArray(new int[list.size()][]);
    }

    //Q10
    public List<List<Integer>> fourSum(int[] nums, int target) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums);

        for (int i = 0; i < nums.length; i++) {

            if (i > 0 && nums[i - 1] == nums[i]) {
                continue;
            }

            for (int j = i + 1; j < nums.length; j++) {

                if (j > i + 1 && nums[j - 1] == nums[j]) {
                    continue;
                }

                int left = j + 1;
                int right = nums.length - 1;
                while (right > left) {
                    int sum = nums[i] + nums[j] + nums[left] + nums[right];
                    if (sum > target) {
                        right--;
                    } else if (sum < target) {
                        left++;
                    } else {
                        result.add(Arrays.asList(nums[i], nums[j], nums[left], nums[right]));

                        while (right > left && nums[right] == nums[right - 1]) right--;
                        while (right > left && nums[left] == nums[left + 1]) left++;

                        left++;
                        right--;
                    }
                }
            }
        }
        return result;
    }

}
