class Solution {
public:
    int climbStairs(int n) {
        map<int,int> mappy;
        return recur(n, mappy);
    }
    int recur(int n, map<int,int> mappy){
        if (n==1){
            return 1;
        }
        if (n==2){
            return 2;
        }
        if (mappy.count(n)){
            return mappy[n];
        }
        int ans = 0;
        ans += recur(n-1, mappy) + recur(n-2, mappy);
        return ans;
    }
};
