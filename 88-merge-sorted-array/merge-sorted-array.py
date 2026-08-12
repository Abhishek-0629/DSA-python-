class Solution:
    def merge(self, nums1, m, nums2, n):
        left=m-1
        right=n-1
        k=m+n-1
        while right>=0:
            if left>=0 and nums1[left]>nums2[right]:
                nums1[k]=nums1[left]
                left-=1
            else:
                nums1[k]=nums2[right]
                right-=1
            k-=1
        #for i in range(n):
         #   nums1[i+m]=nums2[i]
       # nums1.sort()
        