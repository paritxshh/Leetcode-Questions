class Solution {
    public String reorganizeString(String s) {
        int[] charCount = new int[26];
        for (char c : s.toCharArray()) {
            charCount[c - 'a']++;
        }
        
        PriorityQueue<int[]> maxHeap = new PriorityQueue<>((a, b) -> b[1] - a[1]);
        for (int i = 0; i < 26; i++) {
            if (charCount[i] > 0) {
                maxHeap.offer(new int[]{i, charCount[i]});
            }
        }
        
        StringBuilder res = new StringBuilder();
        int[] prev = null;
        
        while (!maxHeap.isEmpty()) {
            int[] curr = maxHeap.poll();
            
            if (prev != null && prev[1] > 0) {
                maxHeap.offer(prev);
            }
            
            res.append((char) (curr[0] + 'a'));
            curr[1]--;
            prev = curr;
        }
        
        if (res.length() == s.length()) {
            return res.toString();
        } else {
            return "";
        }
    }
}