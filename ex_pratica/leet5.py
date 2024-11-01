class Solution(object):
    def findMedianSortedArrays(nums1, nums2):
        i = 0
        j = 0
        while i<len(nums1):
            nums1[i] = int(nums1[i])
            i+=1
        while j<len(nums2):
            nums2[j] = int(nums2[j])
            j+=1
        nums1.extend(nums2) #difere do append pois além de adicionar na lista, já junta os elementos também (não fica um segundo array dentro de outro array (merge))
        nums1 = sorted(nums1)
        x = len(nums1)
        y = int((x/2))
        if(x%2==0):
            nums1[y-1] = float(nums1[y-1])
            nums1[y] = float(nums1[y])
            return (nums1[y-1]+nums1[y])/2
        else:
            nums1[y] = float(nums1[y])
            return float(nums1[y])

nums1 = input("Insira o primeiro array desejado (números separados por vírgula): ")
nums2 = input("Insira o segundo array desejado: ")
nums1 = nums1.split(", ")
nums2 = nums2.split(", ")
print(f'{Solution.findMedianSortedArrays(nums1, nums2):.5f}')