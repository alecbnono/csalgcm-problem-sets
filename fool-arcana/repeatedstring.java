import java.io.*;

class Result {

    /*
     * Complete the 'repeatedString' function below.
     *
     * The function is expected to return a LONG_INTEGER.
     * The function accepts following parameters:
     * 1. STRING s
     * 2. LONG_INTEGER n
     */

    public static long repeatedString(String s, long n) {
        long countA = 0;
        for (char c : s.toCharArray()) {
            if (c == 'a')
                countA++;
        }

        long fullRepeats = n / s.length();
        long remainder = n % s.length();

        long total = countA * fullRepeats;

        for (int i = 0; i < remainder; i++) {
            if (s.charAt(i) == 'a')
                total++;
        }

        return total;
    }

}

class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String s = bufferedReader.readLine();

        long n = Long.parseLong(bufferedReader.readLine().trim());

        long result = Result.repeatedString(s, n);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}
