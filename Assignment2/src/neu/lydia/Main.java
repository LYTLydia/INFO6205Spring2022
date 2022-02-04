package neu.lydia;

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

}
