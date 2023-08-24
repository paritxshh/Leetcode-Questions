class Solution {
    public List<String> fullJustify(String[] words, int maxWidth) {
        List<String> ans = new ArrayList<>();
        List<StringBuilder> row = new ArrayList<>();
        int rowletters = 0;
        
        for (final String word : words) {
            if (rowletters + row.size() + word.length() > maxWidth) {
                final int spaces = maxWidth - rowletters;
                if (row.size() == 1) {
                    for (int i = 0; i < spaces; ++i)
                        row.get(0).append(" ");
                } else {
                    for (int i = 0; i < spaces; ++i)
                        row.get(i % (row.size() - 1)).append(" ");
                }
                final String joinedrow = row.stream().map(StringBuilder::toString).collect(Collectors.joining(""));
                ans.add(joinedrow);
                row.clear();
                rowletters = 0;
            }
            row.add(new StringBuilder(word));
            rowletters += word.length();
        }
        
        final String lastrow = row.stream().map(StringBuilder::toString).collect(Collectors.joining(" "));
        StringBuilder sb = new StringBuilder(lastrow);
        final int spacestobeadded = maxWidth - sb.length();
        for (int i = 0; i < spacestobeadded; ++i)
            sb.append(" ");
        
        ans.add(sb.toString());
        return ans;
    }
}