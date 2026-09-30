class Solution {
    private static final int MAX_LENGTH = 1_000_000;
    private static final int MAX_ABS_VALUE = 1_000_000;

    /**
     * Returns the smallest positive integer missing from A.
     *
     * This in-place algorithm runs in O(N) time and uses O(1) extra space.
     * It marks values in A in place, so the input array is modified.
     */
    public int solution(int[] A) {
        validateInput(A);
        int length = A.length;

        // Values outside [1, N] cannot affect the answer, which is at most N + 1.
        for (int i = 0; i < length; i++) {
            if (A[i] <= 0 || A[i] > length) {
                A[i] = length + 1;
            }
        }

        // Use the sign at each value's corresponding index as its presence marker.
        for (int i = 0; i < length; i++) {
            int value = A[i];
            if (value < 0) {
                value = -value;
            }
            if (value <= length) {
                int index = value - 1;
                if (A[index] > 0) {
                    A[index] = -A[index];
                }
            }
        }

        for (int i = 0; i < length; i++) {
            if (A[i] > 0) {
                return i + 1;
            }
        }
        return length + 1;
    }

    /**
     * Non-mutating alternative: O(N) time and O(N) extra space.
     */
    public int solutionUsingPresenceArray(int[] A) {
        validateInput(A);
        boolean[] present = new boolean[A.length + 1];

        for (int value : A) {
            if (value > 0 && value <= A.length) {
                present[value] = true;
            }
        }

        for (int value = 1; value < present.length; value++) {
            if (!present[value]) {
                return value;
            }
        }
        return A.length + 1;
    }

    private void validateInput(int[] A) {
        if (A == null) {
            throw new IllegalArgumentException("Input array must not be null.");
        }
        if (A.length < 1 || A.length > MAX_LENGTH) {
            throw new IllegalArgumentException(
                    "Input length must be between 1 and " + MAX_LENGTH + ".");
        }
        for (int value : A) {
            if (value < -MAX_ABS_VALUE || value > MAX_ABS_VALUE) {
                throw new IllegalArgumentException(
                        "Array values must be between -"
                                + MAX_ABS_VALUE
                                + " and "
                                + MAX_ABS_VALUE
                                + ".");
            }
        }
    }
}
