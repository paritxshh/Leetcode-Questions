​The approach to solve LeetCode problem 1513 - "Number of Substrings With Only 1s" involves iterating through the input string and keeping track of the count of 
consecutive 1s encountered. Whenever a '0' is encountered, the current count is reset to zero. For each encountered '1', the count is updated and added to the 
overall count of valid substrings.

Here's a step-by-step breakdown of the approach:

1. Initialize variables:
   - 'count': This variable will keep track of the total number of valid substrings composed of only 1s.
   - 'currcount': This variable will keep track of the current count of consecutive 1s encountered.

2. Iterate through each character in the input string:
   - If the character is '1', increment the 'currcount' and add its value to the 'count'.
   - If the character is '0', reset the 'currcount' to zero since the consecutive sequence of 1s is broken.

3. During the iteration, take care to perform the addition of 'currcount' to count modulo some large number (e.g., 1000000007) to prevent integer overflow.

4. Return the final 'count' as the result.


This approach ensures that as you iterate through the input string, you keep track of the current consecutive sequence of 1s and update the count of valid substrings 
accordingly. The use of modulo helps in handling large counts and avoiding integer overflow.
