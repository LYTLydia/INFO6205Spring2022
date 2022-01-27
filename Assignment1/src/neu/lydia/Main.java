package neu.lydia;

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
}


