class Solution {
    func reverseWords(_ s: String) -> String {
        let words = s.split(separator: " ")
        return words.reversed().joined(separator: " ")
    }
}