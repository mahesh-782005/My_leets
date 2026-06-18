class Solution {
    public String longestPalindrome(String s) {
        int l=0, maxl =0;
        int i =0, j =0;
        int n = s.length();
        String res = "";
        for(int k =0; k<n;k++){
            i = k;
            j = k;
            while(i>=0 && j<n && s.charAt(j) == s.charAt(i)){
                i--;
                j++;
            }
            l = j-i+1;
            if (l >maxl){
                res = s.substring(i+1, j);
                maxl = l;
            }
        }
        for(int k=1; k<n; k++){
            i = k-1;
            j = k;
            while(i>=0 && j<n && s.charAt(j) == s.charAt(i)){
        
                i--;
                j++;
            }
            l = j-i+1;
            if (l >maxl){
                res = s.substring(i+1, j);
                maxl = l;
            }

        }
        return res;
    }
}