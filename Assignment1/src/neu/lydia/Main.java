package neu.lydia;

import java.util.*;

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
        while (left < right) {
            int mid = (left + right + 1) / 2;
            int count = 0;
            for (int citation : citations) {
                if (citation >= mid) {
                    count++;
                }
            }

            if (count >= mid) {
                left = mid;
            } else right = mid - 1;
        }

        return left;

    }


    public int[] intersection(int[] nums1, int[] nums2) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        int j = 0, k = 0;
        for (int i = 0; i < nums1.length; i++) {
            if (map.containsKey(nums1[i]) == false) {
                map.put(nums1[i], j);
                j++;
            }
        }
        int[] arr = new int[j];
        for (int g = 0; g < nums2.length; g++) {
            if (map.containsKey(nums2[g])) {
                arr[k] = nums2[g];
                map.remove(nums2[g]);
                k++;
            }
        }
        int[] p = new int[k];
        for (int i = 0; i < k; i++) {
            p[i] = arr[i];
        }
        return p;

    }

    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        int low = 0;
        int high = arr.length - 1;
        while (high - low >= k) {
            if (x - arr[low] > arr[high] - x) {
                low++;
            }else {
                high--;
            }
        }

        List<Integer> result = new ArrayList<>();
        for (; low <= high ; low++) {
            result.add(arr[low]);
        }
        return result;

    }


    public String reorganizeString(String s) {

        int[] al = new int[26];
        char[] ch = s.toCharArray();
        for (char c : ch) {
            al[c - 'a']++;
        }
        int idx = 0;
        int max = Integer.MIN_VALUE;
        int len = ch.length;
        for (int i = 0; i < 26; i++) {
            if (al[i] > max) {
                max = al[i];
                idx = i;
                if (max > (len + 1) / 2) {
                    return "";
                }
            }
        }
        char[] res = new char[len];
        int cnt = 0;
        while (al[idx]-- > 0) {
            res[cnt] = (char) (idx + 'a');
            cnt += 2;
        }
        for (int i = 0; i < 26; i++) {
            while (al[i]-- > 0) {
                if (cnt >= len) {
                    cnt = 1;
                }
                res[cnt] = (char) (i + 'a');
                cnt += 2;
            }
        }
        return new String(res);

    }





    public String customSortString(String S, String T) {
        int[] A = new int[26];
        for (int i=0;i<T.length();i++){
            A[T.charAt(i)-'a']+=1;
        }
        StringBuilder sb = new StringBuilder(T.length());
        for (int i=0;i<S.length();i++){
            char tmp=S.charAt(i);
            while (A[tmp-'a']-->0){
                sb.append(tmp);
            }
        }
        for (int i=0;i<26;i++){
            while (A[i]-->0){
                sb.append((char)('a'+i));
            }
        }
        return sb.toString();
    }



    public List<Integer> pancakeSort(int[] arr) {
        int length = arr.length;
        List<Integer> list = new ArrayList<>(length);
        int max = length;
        while (true) {
            for (int i = 0; i < length; i++) {
                if (arr[i] == max) {
                    if (i == --max) {
                        continue;
                    }
                    int st = 0;
                    int end = i;
                    if (st < end){
                        list.add(i + 1);
                    }
                    while (st < end) {
                        int item = arr[st];
                        arr[st++] = arr[end];
                        arr[end--] = item;
                    }
                    st = 0;
                    end = max;
                    while (st < end) {
                        int item = arr[st];
                        arr[st++] = arr[end];
                        arr[end--] = item;
                    }
                    list.add(max + 1);
                }
            }
            if (max == 0) {
                break;
            }
        }
        return list;
    }


    public int[] frequencySort(int[] nums) {
        int[] temp = new int[201];
        for (int num : nums) {
            temp[num + 100] += 201;
        }
        for (int i = 0; i < temp.length; i++) {
            temp[i] += 200 - i;
        }
        Arrays.sort(temp);
        int[] ret = new int[nums.length];
        int idx = 0;
        for (int i = 0; i < temp.length; i++) {
            if (temp[i] > 0) {
                int count = temp[i] / 201;
                int num = temp[i] % 201;
                for (int j = 0; j < count; j++) {
                    ret[idx++] = 100 - num;
                }
            }
        }
        return ret;

    }


    public List<String> topKFrequent(String[] words, int k) {
        HashMap<String,Integer> map=new HashMap<String,Integer>();
        for(int i=0;i<words.length;i++){
            map.put(words[i],map.getOrDefault(words[i],0)+1);
        }
        PriorityQueue<String> queue = new PriorityQueue<>(new Comparator<String>() {
            @Override
            public int compare(String s1, String s2) {
                if (map.get(s1) == map.get(s2)) {
                    return s1.compareTo(s2);
                }
                if (map.get(s1) > map.get(s2)) {
                    return -1;
                } else {
                    return 1;
                }
            }
        });
        for (String s : map.keySet()) {
            queue.add(s);
        }
        ArrayList<String> strings = new ArrayList<>();
        for(int i=0;i<k;i++){
            strings.add(queue.poll());
        }
        return strings;
    }



}





