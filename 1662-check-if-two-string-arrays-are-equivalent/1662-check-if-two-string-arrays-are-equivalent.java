class Solution {
    public boolean arrayStringsAreEqual(String[] word1, String[] word2) {
        return concatenateStrings(word1).equals(concatenateStrings(word2));
    }
    
    private String concatenateStrings(String[] words) {
        StringBuilder res = new StringBuilder();
        for (String word : words) {
            res.append(word);
        }
        
        return res.toString();
    }
}