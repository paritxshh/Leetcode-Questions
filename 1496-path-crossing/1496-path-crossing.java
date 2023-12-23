class Solution {
    public boolean isPathCrossing(String path) {
        int i = 0, j = 0;
        Set<String> vis = new HashSet<>();
        vis.add("0,0");
        
        for (int k = 0, n = path.length(); k < n; ++k) {
            switch (path.charAt(k)) {
                case 'N' -> --i;
                case 'S' -> ++i;
                case 'E' -> ++j;
                case 'W' -> --j;
            }
            
            String currentPos = i + "," + j;
            if (!vis.add(currentPos)) {
                return true;
            }
        }
        
        return false;
    }
}