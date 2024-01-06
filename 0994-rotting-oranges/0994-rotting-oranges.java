class Pair {
    int first;
    int second;
    int time;

    public Pair(int first, int second, int time) {
        this.first = first;
        this.second = second;
        this.time = time;
    }
}
class Solution {
    public int orangesRotting(int[][] grid) {
        int n = grid.length;
        int m = grid[0].length;
        Queue<Pair> q = new LinkedList<>();
        int freshOranges = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == 2) {
                    q.add(new Pair(i, j, 0));
                } else if (grid[i][j] == 1) {
                    freshOranges++;
                }
            }
        }
        int delR[] = {-1, 0, 1, 0};
        int delC[] = {0, 1, 0, -1};
        int time = 0;

        while (!q.isEmpty()) {
            Pair curr = q.poll();
            int r = curr.first;
            int c = curr.second;
            int t = curr.time;
             time=Math.max(t,time);

            for (int i = 0; i < 4; i++) {
                int nR = delR[i] + r;
                int nC = delC[i] + c;
                if (nR >= 0 && nR < n && nC >= 0 && nC < m && grid[nR][nC] == 1) {
                    q.add(new Pair(nR, nC, t + 1));
                    grid[nR][nC] = 2;
                    freshOranges--;
                }
            }
        }
        if (freshOranges == 0) {
            return time;
        } else {
            return -1;
        }
    }
}