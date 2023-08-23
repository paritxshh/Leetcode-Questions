Problem Statement:
- Given a string 's', you need to reorganize the string such that no two adjacent characters are the same. If it is not possible to reorganize the string, return 
  an empty string.

Approach:

1. Count the frequency of each character in the string and store it in the 'charCount' array. Index 'i' of 'charCount' represents the character 'a' + i.

2. Create a max heap (priority queue) 'maxHeap' to store character frequencies in descending order.
   - The max heap will be based on the frequency of characters.
   - We use an array of size 2, where the first element is the character index (0 to 25) and the second element is the frequency of that character.

3. Populate the max heap with characters and their frequencies. Characters with non-zero frequency are added to the heap.

4. Initialize an empty 'StringBuilder' called 'result' to store the reorganized string.

5. Loop while the max heap is not empty:
   - Poll the character with the highest frequency from the heap.
   - If there was a previously polled character ('prev') and its frequency is still greater than 0, re-add it to the heap.
   - Append the current character to the 'result'.
   - Decrease the frequency of the current character by 1 and update the 'prev' to the current character.

6. After the loop, check if the length of the result is equal to the length of the input string s. If they are equal, return the reorganized string; otherwise, 
  return an empty string.

Key Points:

1. The max heap helps in ensuring that the characters with the highest frequency are processed first.
   
2. The algorithm makes sure that no two adjacent characters in the result are the same by re-adding the previously polled character back to the heap.
