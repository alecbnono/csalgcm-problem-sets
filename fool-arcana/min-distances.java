import java.io.*;
import java.util.*;
import java.util.stream.*;
import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'minimumDistances' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts INTEGER_ARRAY a as parameter.
     */

    public static int minimumDistances(List<Integer> a) {
        // Write your code here
        Map<Integer, Integer> map = new HashMap<>();
        int minDistance = Integer.MAX_VALUE;

        for (int i = 0; i < a.size(); i++) {
            int value = a.get(i);
            if (map.containsKey(value)) {
                int distance = i - map.get(value);
                minDistance = Math.min(minDistance, distance);
            }
            map.put(value, i);
        }
        return minDistance == Integer.MAX_VALUE ? -1 : minDistance;
    }

}

// Convert to Public nalang if youll submit
class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = Integer.parseInt(bufferedReader.readLine().trim());

        List<Integer> a = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                .map(Integer::parseInt)
                .collect(toList());

        int result = Result.minimumDistances(a);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}
