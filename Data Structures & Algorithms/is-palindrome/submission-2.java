class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder filtered = new StringBuilder();

    // Filter out non-alphanumeric and convert to lowercase
    for (char c : s.toCharArray()) {
        if (Character.isLetterOrDigit(c)) {
            filtered.append(Character.toLowerCase(c));
        }
    }

    // Compare string with its reverse
    String filteredStr = filtered.toString();
    String reversedStr = filtered.reverse().toString();

    return filteredStr.equals(reversedStr);
    }
}
