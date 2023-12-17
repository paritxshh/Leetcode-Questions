//{ Driver Code Starts
import java.io.*;
import java.lang.*;
import java.util.*;

class Item {
    int value, weight;
    Item(int x, int y){
        this.value = x;
        this.weight = y;
    }
}

class GfG {
    
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine().trim());
		while(t-->0){
            String inputLine[] = br.readLine().trim().split(" ");
            int n = Integer.parseInt(inputLine[0]);
            int w = Integer.parseInt(inputLine[1]);
            Item[] arr = new Item[n];
            inputLine = br.readLine().trim().split(" ");
            for(int i=0, k=0; i<n; i++){
                arr[i] = new Item(Integer.parseInt(inputLine[k++]), Integer.parseInt(inputLine[k++]));
            }
            System.out.println(String.format("%.2f", new Solution().fractionalKnapsack(w, arr, n)));
        }
    }
}
// } Driver Code Ends


/*
class Item {
    int value, weight;
    Item(int x, int y){
        this.value = x;
        this.weight = y;
    }
}
*/

class Solution
{
    //Function to get the maximum total value in the knapsack.
    double fractionalKnapsack(int W, Item arr[], int n) 
    {
        // Create an array to store the value-to-weight ratio and the index of the item
        double[] valueWeightRatio = new double[n];
        for (int i = 0; i < n; i++) {
            valueWeightRatio[i] = (double) arr[i].value / arr[i].weight;
        }
        
        // Create an array of indices and sort it based on the value-to-weight ratio
        Integer[] indices = new Integer[n];
        for (int i = 0; i < n; i++) {
            indices[i] = i;
        }
        
        Arrays.sort(indices, Comparator.comparingDouble(index -> valueWeightRatio[index]));
        
        double totalValue = 0.0;
        int remainingCapacity = W;
        
        // Iterate throught the sorted indices and add items to the knapsack
        for (int i = n - 1; i >= 0; i--) {
            int index = indices[i];
            if (arr[index].weight <= remainingCapacity) {
                // Take the whole item if it fits
                totalValue += arr[index].value;
                remainingCapacity -= arr[index].weight;
            } else {
                // Take a fraction of the item if it doesn't fit completely
                double fraction = (double) remainingCapacity / arr[index].weight;
                totalValue += fraction * arr[index].value;
                break; // The Knapsack is full
            }
        }
        
        return totalValue;
    }
}