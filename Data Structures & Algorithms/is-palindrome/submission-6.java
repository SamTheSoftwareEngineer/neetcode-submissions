class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder original = new StringBuilder();

        for (char c : s.toCharArray()) {
            if (Character.isLetterOrDigit(c)) {
                original.append(Character.toLowerCase(c));
            }
        }

        // Comparison 
        String originalString = original.toString();
        String reversedString = original.reverse().toString();

        return originalString.equals(reversedString);
    }
}
