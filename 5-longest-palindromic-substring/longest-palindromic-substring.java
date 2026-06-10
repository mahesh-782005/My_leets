class Solution {
    public boolean check(String s) {
        if (s.length() <= 1) {
            return true;
        }
        
        int i = 0;
        int j = s.length() - 1;
        int flag = 1;
        while (i < j) {
            if (s.charAt(i) != s.charAt(j)) {
                flag = 0;
                break;
            }
            i++;
            j--;
        }
        
        if (flag == 0) {
            return false;
        }
        return true;
    }

    public String longestPalindrome(String s) {
        int l = s.length();
        if (l == 0) {
            return "";
        } 
        
        int maxlen = 1;
        String res = s.substring(0, 1);
        
        for (int i = 0; i < l; i++) {
            for (int j = i + 1; j <= l; j++) {
                String x = s.substring(i, j);
                if (check(x)) {
                    int len = j - i;
                    if (maxlen < len) {
                        maxlen = len;
                        res = x;
                    }
                }
            }
        }
        return res;
    }
}
