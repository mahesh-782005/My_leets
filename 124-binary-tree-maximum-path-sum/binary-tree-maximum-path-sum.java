/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int m =Integer.MIN_VALUE;
    int maxsum(TreeNode root){
        if(root == null){
            return 0;
        }
        int l =Math.max(0, maxsum(root.left));
        int r = Math.max(0,maxsum(root.right));
        int s = l+r+root.val;
        if(s>m){
            m =s;
        }
        if (m<l+root.val){
            m= l+root.val;
        }
        if(m<r+root.val){
            m= r+root.val;
        }
        return root.val+Math.max(l,r);
    }
    public int maxPathSum(TreeNode root) {
        maxsum(root);
        return m;  
    }
}