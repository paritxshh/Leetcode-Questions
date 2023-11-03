class Solution {
    public List<String> buildArray(int[] target, int n) {
        List<String> result = new ArrayList<>();
        int index = 0;

        for (int i = 1; i <= n && index < target.length; i++) {
            result.add("Push");
            if (target[index] != i) {
                result.add("Pop");
            } else {
                index++;
            }
        }

        return result;
    }
}