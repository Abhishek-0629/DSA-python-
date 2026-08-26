class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        result = ""
        min_length = float('inf')
      
        # Use sliding window for better efficiency
        for start in range(n):
            ones_count = 0
            for end in range(start, n):
                if s[end] == '1':
                    ones_count += 1
              
                # When we have exactly k ones
                if ones_count == k:
                    current_length = end - start + 1
                    current_substring = s[start:end + 1]
                  
                    # Update result based on length and lexicographical order
                    if (current_length < min_length or 
                        (current_length == min_length and 
                         (not result or current_substring < result))):
                        result = current_substring
                        min_length = current_length
                    break  # Found k ones, no need to extend further
              
                # Early termination if we exceed k ones
                elif ones_count > k:
                    break
      
        return result