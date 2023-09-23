class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s == null || s.length() == 0) {
            return 0;
        }

        int maxLength = 0;
        int startIndex = 0;
        HashMap<Character, Integer> charIndexMap = new HashMap<>();

        for (int endIndex = 0; endIndex < s.length(); endIndex++) {
            char currentChar = s.charAt(endIndex);

            if (charIndexMap.containsKey(currentChar)) {
                startIndex = Math.max(startIndex, charIndexMap.get(currentChar) + 1);
            }

            charIndexMap.put(currentChar, endIndex);
            maxLength = Math.max(maxLength, endIndex - startIndex + 1);
        }

        return maxLength;
    }
}