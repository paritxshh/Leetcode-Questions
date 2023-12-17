# Fractional Knapsack
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given <em>weights</em> and <em>values</em> of <strong>N</strong> items, we need to put these items in a knapsack of capacity <strong>W</strong> to get the <em>maximum</em> total value in the knapsack.<br><strong>Note:</strong> Unlike 0/1 knapsack, you are allowed to break&nbsp;the item.&nbsp;</span></p>
<p>&nbsp;</p>
<p><span style="font-size: 18px;"><strong>Example 1:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:
</strong>N = 3, W = 50
values[] = {60,100,120}
weight[] = {10,20,30}
<strong>Output:
</strong>240.00<strong>
Explanation:<br></strong>Take the item with value 60 and weight 10, value 100 and weight 20 and split the third item with value 120 and weight 30, to fit it into weight 20. so it becomes (120/30)*20=80<br>so, the total weight becomes 60+100+80.0=240.0<strong><br></strong>Thus, Total maximum value of item
we can have is 240.00 from the given
capacity of sack. 
</span></pre>
<p><span style="font-size: 18px;"><strong>Example 2:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:
</strong>N = 2, W = 50
values[] = {60,100}
weight[] = {10,20}
<strong>Output:
</strong>160.00<strong>
Explanation:<br></strong>Take both the items completely, without breaking.
Total maximum value of item
we can have is 160.00 from the given
capacity of sack.</span></pre>
<p>&nbsp;</p>
<p><span style="font-size: 18px;"><strong>Your Task</strong> :<br>Complete the function&nbsp;<em><strong>fractionalKnapsack</strong>()</em> that receives maximum capacity , array of structure/class&nbsp;and size n and returns a double value representing the maximum value in knapsack.<br><strong>Note:&nbsp;</strong>The details of structure/class is defined in the comments above the given function.</span></p>
<p><br><span style="font-size: 18px;"><strong>Expected Time Complexity</strong> : O(NlogN)<br><strong>Expected Auxilliary Space</strong>: O(1)</span></p>
<p><br><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 &lt;= N &lt;= 10<sup>5</sup><br>1 &lt;= W &lt;= 10<sup>5</sup></span></p></div>