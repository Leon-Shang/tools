# import pyautogui 

# for i in range(5):
#     print(pyautogui.position())
#     current_position = pyautogui.position()
#     pyautogui.moveTo(500, 300, duration=0.25)
#     pyautogui.moveTo(current_position)
#     pyautogui.scroll(-200)
# class Solution:
#     def char_counts(self, _str):
#         result = [0 for i in range(200)]
#         for char in _str:
#             result[ord(char)] += 1   
#         result = [str(i) for i in result]
#         return ''.join(result) 
#     def groupAnagrams(self, strs):
#         result = {}
#         if strs[0] == '':
#             return [[""]]
#         for _str in strs:
#             char_count = self.char_counts(_str)
#             if char_count in result:
#                 result[char_count].append(_str)  
#             else:
#                 result[char_count] = [_str]
#         return list(result.values())
    
# s = Solution()

# print(s.groupAnagrams(["",""]))

# c = set([1,2])
# a = {
#     1:1,
#     0:2,
# }

# print(a.keys())


# class Solution:
#     def longestConsecutive(self, nums) -> int:
#         nums_set = set(nums)
#         res = 0
#         while len(nums_set) > 0:
            
#             nums_list = list(nums_set)
#             num = nums_list[0]
#             length = 1
#             nums_set.remove(num)
#             print(num)
#             while num-1 in nums_set:
#                 nums_set.remove(num-1)
#                 length+=1
#                 num -= 1
#             num = nums_list[0]
#             while num+1 in nums_set:
#                 nums_set.remove(num+1)
#                 length += 1
#                 num += 1
#             res = max(res, length)

#         return res

# nums = [0,1,0,3,12]    
# count_zero = 0
# for i in range(len(nums)):
#     if nums[i] == 0:
#         count_zero += 1
#     else:
#         nums[i-count_zero] = nums[i]
# for i in range(count_zero):
#     nums[-(i+1)] = 0
# print(nums)



# left_index = 0
# right_index = -1
# res = []
# n_total = len(nums)
# for i in range(n_total-2):
#     l = nums[left_index]
#     r = nums[right_index]
#     print(left_index)
#     if l + r > 0:
#         if r == nums[right_index+1] and -left_index+right_index+n_total+1>3:
#             right_index -= 1
#             continue
#         for l_tem_index in range(left_index, n_total+right_index-1):
#             l_tem = nums[l_tem_index]
#             if l_tem == nums[l_tem_index-1] and l_tem != 0:
#                 continue
#             if l_tem + nums[l_tem_index+1] + r > 0:
#                 break
#             for middle_index in range(l_tem_index+1, n_total+right_index):
#                 m = nums[middle_index]
#                 if l_tem + m + r == 0:
#                     res.append([l_tem, m, r])
#                     break
#                 if l_tem + m + r > 0:
#                     break
#         right_index -= 1
#     else:
#         if l == nums[left_index+1] and -left_index+right_index+n_total+1>3:
#             left_index += 1
#             continue
#         for r_tem_index in range(right_index, -n_total+left_index+1, -1):
#             r_tem = nums[r_tem_index]
#             if r_tem == nums[r_tem_index+1] and r_tem != 0:
#                 continue
#             if r_tem + nums[r_tem_index-1] + l < 0:
#                 break
#             for middle_index in range(r_tem_index-1, -n_total+left_index, -1):
#                 m = nums[middle_index]
#                 if r_tem + m + l == 0:
#                     res.append([r_tem, m, l])
#                     break
#                 if r_tem + m + l < 0:
#                     break
#         left_index += 1
# nums = [-1,0,1,2,-1,-4]
# nums = sorted(nums)
# # print(nums)


# # nums =sorted([-1,0,1,2,-1,-4]) 
# def threeSum(nums):
#     n=len(nums)
#     res=[]
#     if(not nums or n<3):
#         return []
#     nums.sort()
#     res=[]
#     for i in range(n):
#         if(nums[i]>0):
#             return res
#         if(i>0 and nums[i]==nums[i-1]):
#             continue
#         L=i+1
#         R=n-1
#         while(L<R):
#             if(nums[i]+nums[L]+nums[R]==0):
#                 res.append([nums[i],nums[L],nums[R]])
#                 while(L<R and nums[L]==nums[L+1]):
#                     L=L+1
#                 while(L<R and nums[R]==nums[R-1]):
#                     R=R-1
#                 L=L+1
#                 R=R-1
#             elif(nums[i]+nums[L]+nums[R]>0):
#                 R=R-1
#             else:
#                 L=L+1
#     return res


# print(threeSum(nums))
# print(list(range(0, -10, -1)))
# for i in range(0, -10, -1):
#     print(i)