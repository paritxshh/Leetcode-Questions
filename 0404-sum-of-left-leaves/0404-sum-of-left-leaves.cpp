/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int sumOfLeftLeaves(TreeNode* root) {
        if (!root)
            return 0;
        
        int leftSum = 0;
        
        // Check if the left child of the current node is a leaf
        if (root->left && !root->left->left && !root->left->right)
            leftSum += root->left->val;
        
        // Recursively calculate the sum of left leaves in the left and right subtrees
        leftSum += sumOfLeftLeaves(root->left);
        leftSum += sumOfLeftLeaves(root->right);
        
        return leftSum;
    }
};