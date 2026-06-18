class Solution {
    public int maxArea(int[] height) {
        int n = height.length;
        int i =0, j = n-1;
        int maxarea =0, area =0;
        int l,h;
        while(i<j){
            l = j-i;
            if(height[i]<height[j]){
                h = height[i];
                i+=1;
            }
            else{
                h = height[j];
                j-=1;
            }
            area = l*h;
            if (area >maxarea){
                maxarea = area;
            }
        }
        return maxarea;
    }
}