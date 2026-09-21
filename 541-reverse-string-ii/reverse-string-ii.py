class Solution:

  def reverseStr(self, s: str, k: int) -> str:
    s_list = list(s)  # 1. String ko mutable list banaya 📝
    n = len(s_list)

    # 2. Har 2k characters ke block par jump karo 🏃
    for i in range(0, n, 2 * k):
      left = i  # 👈 Block ka pehla index
      right = min(i + k - 1, n - 1)  # 👉 Pehle k chars ka aakhri index

      # 3. Two-pointer swapping 🔄
      while left < right:
        s_list[left], s_list[right] = s_list[right], s_list[left]
        left += 1
        right -= 1

    return "".join(s_list)  # 4. Final string return ki 🧵