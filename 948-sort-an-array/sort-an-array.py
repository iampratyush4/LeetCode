class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(nums,low,high):
            if low>=high: return
            mid=(low+high)//2
            merge(nums,low,mid)
            merge(nums,mid+1,high)
            mergesort(nums,low,mid,high)
        def mergesort(nums,low,mid,high):
            ans=[]
            i=low
            j=mid+1
            while i<=mid and j<=high:
                if nums[i]<nums[j]:
                    ans.append(nums[i])
                    i+=1
                else:
                    ans.append(nums[j])
                    j+=1
            while i<=mid:
                ans.append(nums[i])
                i+=1
            while j<=high:
                ans.append(nums[j])
                j+=1
            for i in range(len(ans)):
                nums[low+i]=ans[i]
        merge(nums,0,len(nums)-1)
        return nums
        
        