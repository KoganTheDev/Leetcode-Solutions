int climbStairs(int n) {
    int OPT[n + 1];

    // Handle edge cases
    if (n == 0) return 0;
    if (n == 1) return 1;

    // Set base cases.
    OPT[0] = 1;
    OPT[1] = 1;

    // Sum up the amout of ways one can go uppstairs by summing the element in OPT[i-1] and OPT[i-2]
    for (int i = 2; i <= n; i++){
        OPT[i] = OPT[i-1] + OPT[i-2];
    }

    return OPT[n];
}