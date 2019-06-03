// #     I recently went through a Google Phone Interview after successfully completing a coding challenge. I wanted to share the question with the leetcode community and get a proper approach for it. I took some time in understanding the question properly as the interviewer's accent and explanation of the question made it difficult to comprehend.

// # Question:
// # Consider a binary tree, where an arbitary node has 2 parents i.e two nodes in the tree have the same child.

// # Identify the defective node with 2 parents.
// # Correct such a node and restore the binary tree properties to that node.
// # My Approach:
// # I took some time in getting to the proper answer. My idea was to traverse the tree in any order(like inorder) and store the visited nodes in a set. If the traversal leads to a node which is already visited, then the node is the defective one.
// # But I messed up the part for finding the parent node and equating the corresponding left or right link to null.

// # Can someone give me a complete approach, preferrably with a working code ? Thanks.
// # @dietpepsi @StefanPochmann
    
    private static Set<TreeNode> visited = new HashSet<>();   

    private static void fixTreeHelper(TreeNode node, TreeNode parent) {
        if (node == null) {
            return;
        }
        if (!visited.contains(node)) {
            visited.add(node);
            fixTreeHelper(node.left, node);
            fixTreeHelper(node.right, node);
        } else {
            if (parent.left == node) {
                parent.left = null;
            } else if (parent.right == node) {
                parent.right = null;
            }
        }
    }