class Solution:
    # 目前还是错的，且题目要求log(m+n)
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        if nums1 == []:
            return findMed(nums2)
        if nums2 == []:
            return findMed(nums1)

        med1 = findMed(nums1)
        med2 = findMed(nums2)
        print(med1)
        print(med2)
        if len(nums1) == 1 and len(nums2) == 1:
            return (med1+med2)/2.0
        if len(nums1) == 1 or len(nums2) == 1:
            return findMed(sorted(nums1+nums2))
        if med1 < med2:
            nums1 = nums1[int(len(nums1)/2) :]
            print(nums1)
            if len(nums2) % 2 == 1:
                nums2 = nums2[0:int(len(nums2)/2)+1]
            else:
                nums2 = nums2[0:int(len(nums2) / 2)]
            print(nums2)
            return self.findMedianSortedArrays(nums1,nums2)
        elif med1 > med2:
            if len(nums1) % 2 == 1:
                nums1 = nums1[0:int(len(nums1) / 2)+1]
            else:
                nums1 = nums1[0:int(len(nums1) / 2)]
            print(nums1)
            nums2 = nums2[int(len(nums2)/2) :]
            print(nums2)
            return self.findMedianSortedArrays(nums1, nums2)
        else:
            return med1


def findMed(a):
    length = len(a)
    if length % 2 == 0:
        return (a[int(length/2)]+a[int(length/2)-1])/2.0
    else:
        return a[int(length/2)]

list1 = [3]
list2 = [-2,-1]
print(Solution().findMedianSortedArrays(nums1=list1,nums2=list2))