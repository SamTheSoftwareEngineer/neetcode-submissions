class Solution {
    public boolean isPalindrome(String s) {
            StringBuilder filtered = new StringBuilder();

            // Filter out non-alphanumeric chars and convert to lowercase
            for (char c : s.toCharArray()) {
                if (Character.isLetterOrDigit(c)) {
                    filtered.append(Character.toLowerCase(c));
                }
            }

            int l = 0;
            int r = filtered.length() - 1;

            while (l < r) {
                if (filtered.charAt(l) != filtered.charAt(r)){
                    return false;
                } else {
                    l++;
                    r--;
                }
            }
        return true;
    }
}
