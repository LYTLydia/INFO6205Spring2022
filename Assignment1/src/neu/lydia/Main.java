package neu.lydia;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        // write your code here
    }

    public void swap(int[]nums,int i,int j)
    {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

    public void sortColors(int[] nums) {
        int red = 0, blue = nums.length - 1;
        int i = 0;
        while (i <= blue) {
            if(nums[i] == 0){
                swap(nums,i++,red++);
            }
            else if(nums[i]==2){
                swap(nums,i,blue--);
            }
            else{
                i++;
            }

        }
    }





    public static List<Integer> majorityElement(int[] nums) {
        int amount = nums.length / 3;
        Arrays.sort(nums);
        List<Integer> list = new ArrayList<>();
        int m = 0, n = 0;
        while (n < nums.length) {
            if (nums[m] != nums[n]) {
                if (n - m > amount) list.add(nums[m]);
                m = n;
            }
            n++;
        }
        if (n - m > amount) list.add(nums[m]);
        return list;
    }



    public int hIndex(int[] citations) {
        int length = citations.length;
        int left = 0;
        int right = length;
        while(left<right){
            int mid=(left+right+1)/2;
            int count = 0;
            for(int citation: citations){
                if(citation>=mid){
                    count++;
                }
            }

            if(count>=mid){
                left=mid;
            }
            else right = mid-1;
        }

        return left;

    }










}





