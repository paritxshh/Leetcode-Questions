The strategy used to solve LeetCode problem 806 - "Number of Lines To Write String" - is broken down in the following paragraphs.

1. Set up variables:
   - Initialise the lineWidth and lines variables to record the current line's width and the total number of lines used.

2. Repeat the String Iteratively:
   - Use a for-each loop to iterate through each character in the input string s.

3. Determine Character and Line Widths:
   - Use the widths array to determine the current character's width. The character 'a' corresponds to array index zero, 'b' to array index one, and so on.
   - Verify whether increasing the line width by the width of the current character will result in a width that is greater than 100 pixels.

4. Manage Line Width and Lines:
   - Increase the number of lines and set lineWidth back to the width of the current character if adding it would make it wider than the maximum width (100 pixels).
   - Simply add the width to lineWidth if doing so won't cause it to exceed the allowed width.

5. Return the result:
   - Return an array with the total number of lines (lines) and the width of the last line (lineWidth) after processing each character in the string.
  

By using this method, the restriction of a line's maximum width of 100 pixels is maintained while allowing for the addition of characters to lines. The final output is an array that includes both the last line's width and the total number of lines used.
