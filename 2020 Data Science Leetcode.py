#!/usr/bin/env python
# coding: utf-8

# ### Array

# ### Binary Search

# ### Two Pointer

# ### Dynamic Programming/Recursive

# ### Recursion

# In[ ]:


Input: ["aflower","flow","flight"]
Output: "fl"


# In[35]:


Input=["falower","fblow","cflight"]


# In[8]:


minimum=min([len(string) for string in Input ])
dict1={}
for i in range(minimum+1):
    dict1[i]=[string[:i] for string in Input]


# In[16]:


for key in range(minimum,-1,-1):
    if len(set(dict1[key]))==1:
        print(key)


# In[33]:


def longestCommonPrefix(strs):
    minimum=min([len(str) for str in strs])
    dict1={}
    for i in range(minimum+1):
        dict1[i]= [str[:i] for str in strs]
    L=[]
    for key in range(minimum,-1,-1):
        if len(set(dict1[key]))==1:
            L.append(key)
    return strs[0][:max(L)]


# In[36]:


longestCommonPrefix(Input)


# In[3]:


not 'a'


# ### 581. Shortest Unsorted Continuous Subarray

# Input: [2, 6, 4, 8, 10, 9, 15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

# In[64]:


nums=[2, 6, 4, 8, 10, 9, 15]


# In[4]:


nums2=sorted(nums)
nums2


# In[5]:


a=[i for i in range(len(nums)) if nums[i]!=nums2[i] ]
nums[min(a):max(a)]


# In[7]:


nums[min(a):max(a)+1]


# In[27]:


def retsub(nums):
    nums2=sorted(nums)
    if nums2!=nums:
        a=[i for i in range(len(nums)) if nums[i]!=nums2[i]]
        submax=nums[min(a):max(a)+1]
        return len(submax)
    else:
        return 0


# In[55]:


def retsub(nums):
    nums2=sorted(nums)
    return len(nums[min([i for i in range(len(nums)) if nums[i]!=nums2[i]]):max([i for i in range(len(nums)) if nums[i]!=nums2[i]])+1]) if nums!=nums2 else 0


# In[31]:


get_ipython().run_line_magic('time', '')
retsub([2,6,4,8,10,9,15])


# In[25]:


[2,6,4,8,10,9,15]==sorted([2,6,4,8,10,9,15])


# In[54]:


nums,nums[6::-1]


# In[51]:


is_same = [a == b for a, b in zip(nums, sorted(nums))]
is_same,is_same[::-1]


# In[ ]:


def findUnsortedSubarray(self, nums):
        is_same = [a == b for a, b in zip(nums, sorted(nums))]
        return 0 if all(is_same) else len(nums) - is_same.index(False) - is_same[::-1].index(False)


# In[ ]:





# In[70]:


def findUnsortedSubarray(nums):
    expected_nums=sorted(nums)
    l=[i for i in range(len(nums)) if nums[i]!=expected_nums[i]]
    if len(l)==0:
        return 0
    return max(l)-min(l)+1


# In[71]:


findUnsortedSubarray(nums)


# ### 204. Count Primes

# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

# In[5]:


def findprime(n):
    if n>2:
        s=1
        for i in range(3,n):
            if i%2!=0:
                if sum([1 if i%x==0 else 0 for x in range(3,int(i**0.5)+1) ])==0: #get the prime
                    s+=1
        return s
    else:
        return 0
            


# In[26]:


def countprimes(n):
    if n<3:
        return 0
    primes=[True]*n
    primes[0]=primes[1]=False
    for i in range(2,int(n**0.5)+1):
        if primes[i]:
            primes[i**2:n:i]=[False]*len(primes[i**2:n:i])
    return sum(primes)


# In[212]:


def countPrimes(n):
    if n<3:
        return 0
    else:
        import numpy as np
        odd_n=[x for x in range(3,n,2)]
        L=[]
        for x in odd_n:
            if np.prod([x%i for i in range(2,int(x**0.5)+1)])!=0: #3,5,7 []
                 L.append(1)
        return sum(L)+1
                


# In[218]:


def countPrimes(n):
    if n<=2:
        return 0
    else:
        prime=[True]*n
        prime[0]=prime[1]=False
        for i in range(2,int(n**0.5)+1): #n=143(11*13) could be definitely be updated when we do factors to 12
            if prime[i]:
                prime[i**2:n:i]=[False]*len(prime[i**2:n:i])
        return sum(prime)


# In[219]:


countPrimes(10000)


# ### rotate array

# Given an array, rotate the array to the right by k steps, where k is non-negative.
# 
# Example 1:
# 
# Input: [1,2,3,4,5,6,7] and k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:
# 
# Input: [-1,-100,3,99] and k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]

# In[116]:


input=[-1,-100,3,99]


# In[117]:


def rotateK(nums,k):
    k=k%len(nums)
    nums[:]=nums[-k:]+nums[:-k]
    #nums=nums[-k:]+nums[:-k]
    return nums


# In[118]:


rotateK(input,3)


# In[124]:


input=[1,2,3]
def checkcolon(nums):
    nums[:]=[3,6,3]
    return nums
checkcolon(input),input


# In[ ]:





# ### Valid Palindrome

# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
# 
# Note: For the purpose of this problem, we define empty string as valid palindrome.
# 
# Example 1:
# 
# Input: "A man, a plan, a canal: Panama"
# Output: true
# Example 2:
# 
# Input: "race a car"
# Output: false

# In[133]:


input="A man, a plan, a canal: Panama"


# In[131]:


' '.join(['a','b'])


# In[146]:


'AB'.lower()


# In[147]:


import string
order=''.join([l.lower() for l in input if l!=' ' if l in string.ascii_lowercase or l in string.ascii_uppercase][::-1])
order


# In[33]:


def ispalindrome(s):
    import string
    order=''.join([l.lower() if l in string.ascii_lowercase or l in string.ascii_uppercase else l if l in [str(digit) for digit in range(0,10)] else '' for l in s if l!=' ' ])
    disorder=''.join([l.lower() if l in string.ascii_lowercase or l in string.ascii_uppercase else l if l in [str(digit) for digit in range(0,10)] else '' for l in s if l!=' ' ][::-1])
    print(order,disorder)
    return True if order==disorder else False
    


# def ispalindrome(s):
#     import string
#     order=''.join([l.lower() if l in string.ascii_lowercase or l in string.ascii_uppercase else l if l in range(0,9) else for l in s if l!=' ' ])
#     disorder=''.join([l.lower() if l in string.ascii_lowercase or l in string.ascii_uppercase else l for l in s if l!=' ' ])
#     return True if order==disorder else False

# In[34]:


s='wt3y:'
[i for i in s if i in [str(digit) for digit in range(0,10)]]


# In[48]:


s='wTx%3 y:'
[l.lower() for l in s if l.isalnum()]


# In[52]:


def ispalindrome(s):
    order= ''.join([l.lower() for l in s if l.isalnum()])
    disorder= ''.join([l.lower() for l in s if l.isalnum()][::-1])
    return True if order==disorder else False
    


# In[53]:


ispalindrome('wt3y:')


# In[ ]:





# ### remove duplicates

# In[1]:


def removeDuplicates(nums):
    nums[:]=list(set(nums))
    return len(set(nums))


# In[2]:


input=[-1,0,0,0,0,3,3]
i=0
[input[i] for i in range(removeDuplicates(input))]


# In[7]:


def removeDuplicate(nums):
    if len(nums)==0:
        return []
    else:
        nums[:]=[nums[i] for i in range(len(nums)-1) if nums[i]!=nums[i+1]]+[nums[-1]]
        return nums


# In[6]:


input=[-1,0,0,0,0,3,3]
removeDuplicate(input)


# In[ ]:





# ###  Intern Interview Q

# 2.
# 
# Sample Input: 
#     String: GHDRDRD
#     Sub-string: DRD
# 
# Sample Output: 2

# In[83]:


string='GHDRDRD'


# In[82]:


def count_substring(string, sub_string):
    return sum(string[i:i+len(sub_string)]==sub_string for i in range(len(string)))


# In[84]:


count_substring('GHDRDRD','DRD')


# 3.
# 
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
# 
# Output:  [ ["ate","eat","tea"],  ["nat","tan"],  ["bat"] ]
# 

# In[22]:


input=["eat", "tea", "tan", "ate", "nat", "bat"]
unpacked=[[x for x in word] for word in input]
unpacked2=[sorted([x for x in word]) for word in input]
packed2=[''.join(list) for list in unpacked2]
dictpack={}
for orderWord in packed2:
    if orderWord not in dictpack:
        dictpack[orderWord]=[]
    dictpack[orderWord].append(unpacked[packed2.index(orderWord)])
print(dictpack)


# In[143]:


def groupAnagrams(strs):
    unpacked2=[sorted([x for x in word]) for word in strs]
    packed2=[''.join(list) for list in unpacked2]
    dictpack={}
    for orderWord in packed2:
        if orderWord not in dictpack:
            dictpack[orderWord]=[]
        dictpack[orderWord].append(strs[packed2.index(orderWord)])
    return dictpack.values()


# In[150]:


def groupAnagrams(strs):
    unpacked2=[sorted([x for x in word]) for word in strs]
    packed2=[''.join(list) for list in unpacked2]
    dictpack={}
    for i in range(len(packed2)):
        if packed2[i] not in dictpack:
            dictpack[packed2[i]]=[]
        dictpack[packed2[i]].append(strs[i])
    return dictpack.values()


# In[151]:


input=["eat", "tea", "tan", "ate", "nat", "bat"]
groupAnagrams(input)


# In[ ]:





# ### Find needle in haystack

# Input: haystack = "hello", needle = "ll"
# Output: 2
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1

# In[158]:


def strStr(haystack,needle):
    l=len(needle)
    if l==0:
        return 0
    else:
        a=[1 if haystack[i:i+len(needle)]==needle else 0 for i in range(len(haystack)-l+1)]
        if sum(a)==0:
            return -1
        else:
            return a.index(1)


# In[161]:


haystack = "hello";needle = "ll"
strStr(haystack,needle)


# In[160]:


def strStr(haystack,needle):
    return haystack.find(needle)


# In[164]:


haystack = "hello";needle = ""
strStr(haystack,needle)


# In[ ]:





# ### Count and Say

#  1.     1
#  2.     11
#  3.     21
#  4.     1211
#  5.     111221 
#  6.     312211
#  7.     13112221
#  8.     1113213211
#  9.     31131211131221
# 10.     13211311123113112211

# In[20]:


def countAndSay(n):
    L='1'
    for _ in range(n-1):
        i=0
        r=''
        while i<len(L)-1:
            if L[i]!=L[i+1]:
                r+=str(i+1)+L[i]
                L=L[i+1:]
                i=0
            else:
                i+=1
        r+=str(len(L))+L[-1]
        L=r
    return L


# In[22]:


countAndSay(10)


# In[23]:


def countAndSay(n):
    s='1'
    L=['1']
    for x in range(n-1): #do how many times more
        ss=''
        i=0
        while i+1<len(s):
            if s[i]!=s[i+1]:
                ss+=str(i+1)+s[i]
                s=s[i+1:]
                i=0
            else:
                i+=1
        ss+=str(len(s))+s[-1]
        L.append(ss)
        s=ss
    return L[-1]      


# In[54]:


def countAndSay(n):
    s='1'
    for _ in range(n-1): #do how many times more
        ss=[]
        i=0
        while i+1<len(s):
            if s[i]!=s[i+1]:
                ss.append(str(i+1))
                ss.append(s[i])
                s=s[i+1:]
                i=0
            else:
                i+=1
        ss.append(str(len(s)))
        ss.append(s[-1])
        s=''.join(ss)
    return s    #return s instead of creating a list 


# In[55]:


countAndSay(10)


# In[41]:


import re
s = '234'
s = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)   #group(0)整体 只替换s的一部分,再打印s
#s = re.sub(r'(.)[1]*', lambda m: str(len(m.group(0))) + m.group(1), s)   #group(0)整体 只替换s的一部分,再打印s
#m=re.search(r'(.)\1*',s)
#m.group(0)
s


# In[18]:


import re
print (re.sub('\s+', ' ', 'hello     there      there'))


# In[ ]:





# ## 7/20 remove element
# Given nums = [3,2,2,3], val = 3

# In[63]:


input=[3,2,2,3] 


# In[68]:


def removeElement(nums,val):
    nums[:]=[x for x in nums if x!=val]
    return len(nums)


# In[70]:


removeElement(input,3)


# ### Search Insert Position
# Input: [1,3,5,6], 5
# Output: 2
# Input: [1,3,5,6], 7
# Output: 4

# In[135]:


def searchInsert(nums, target):
    if target in nums:
        return nums.index(target)
    else:
        nums.append(target) ### 只是一步操作 return None
        return sorted(nums).index(target)


# In[136]:


a=[1,3,4,5]


# In[137]:


searchInsert(a,0)


# ### Maximum Subarray
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# In[1]:


#my code O(n^2)
def maxSubArray(nums):
    l=len(nums)
    dict={i:max([sum(nums[i:e]) for e in range(i+1,l+1)]) for i in range(l)}
    return max(dict.values())
Input=[-2,1,-3,4,-1,2,1,-5,4]
maxSubArray(Input)


# In[14]:


#Kadane’s Algorithm: O(n)  only track the positive continous array
def maxSubArray(nums):
    max_ending=0
    max_sofar=-abs(max(nums))-1
    for i in nums:
        max_ending+=i
        if max_ending>max_sofar:
            max_sofar=max_ending
        max_ending=max(0,max_ending)  #you 0 lai qingli
    return max_sofar
Input=[-1]
maxSubArray(Input)


# ### Return last word
# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
# 
# If the last word does not exist, return 0.
# 
# Note: A word is defined as a character sequence consists of non-space characters only.
# 
# Example:
# 
# Input: "Hello World"
# Output: 5

# In[139]:


#Test success, not accepted.
def lengthOfLastWord(s):
    if ' 'in s:
        s2=s.replace(' ','')
        if not (s2.isalpha() or s2.isnumeric()):
            return 0
        else:
            return len(s.split(' ')[-1])
    else:
        return len(s)  #'a'


# In[144]:


def lengthOfLastWord(s):
    s=s.strip(' ')  #remove learding/trailing empty space
    return len(s.split(' ')[-1])


# In[145]:


s="a"
s='             '
s=' Hello    World '
lengthOfLastWord(s)


# In[137]:


s=' Hello    World '
s.strip('    ').split(' ')


# In[ ]:





# ### Plus One
# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
# 
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
# 
# You may assume the integer does not contain any leading zero, except the number 0 itself.
# 
# Example:
# 
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.

# In[44]:


input=[1,2,3]


# In[51]:


def plusOne(digits):
    num=''
    for x in digits:
        num+=str(x) 
    num=str(int(num)+1)
    digits=[int(x) for x in num]
    return digits


# In[52]:


plusOne(input)


# In[40]:


#use recursive
def plusOnerec(digits):
    if len(digits)==0:    #handle [9]
        digits.extend('1')
    elif digits[-1]==9:
        digits=plusOnerec(digits[:-1])
        digits.extend('0')
    else:
        digits[-1]+=1
    return [int(x) for x in digits ]
plusOnerec([9])


# ### Add Binary
# Given two binary strings, return their sum (also a binary string).
# 
# The input strings are both non-empty and contains only characters 1 or 0.
# 
# Example 1:
# 
# Input: a = "11", b = "1"
# Output: "100"
# Example 2:
# 
# Input: a = "1010", b = "1011"
# Output: "10101"

# 0 + 0 = 0
# 1 + 0 = 1
# 1 + 1 = 10 (binary for 2)
# 1 + 1 + 1 = 11 (binary for 3)

# In[63]:


def addBinary(a,b):
    ad= [int(d) for d in a]
    bd=[int(d) for d in b]
    lenab=max(len(ad),len(bd))
    if len(ad)<lenab:
        ad=[0]*(lenab-len(ad))+ad
    else:
        bd=[0]*(lenab-len(bd))+bd
    ad.reverse()
    bd.reverse()
    L=[]
    tem=0
    for i in range(lenab):
        digit=ad[i]+bd[i]+tem
        if digit==2:
            tem=1
            digit=0
        elif digit==3:
            tem=1
            digit=1
        else:
            tem=0
        L.append(str(digit))
    L.append(str(tem))
    L.reverse()
    output=str(int(''.join(L))) #deal with '00'
    return output


# In[64]:


addBinary('1010','1011')


# In[54]:


a="10100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101"
b="110101001011101110001111100110001010100001101011101010000011011011001011101111001100000011011110011"


# In[55]:


addBinary(a,b)


# In[ ]:





# ### Sqrt(x)
# 
# Implement int sqrt(int x).
# 
# Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
# 
# Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
# 
# Example 1:
# 
# Input: 4
# Output: 2
# Example 2:
# 
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since 
#              the decimal part is truncated, 2 is returned.

# In[85]:


#time error
def mySqrt(x):
    L=[]
    for i in range(0,x+1):
        if i**2<=x:
            L.append(i)
        else:
            break
    return max(L)


# In[96]:


#binary search
def mySqrt(x):
    if x==1:
        return 1
    l,r=0,x
    while l<=r:
        mid=(l+r)//2
        if mid**2<=x<(mid+1)**2:
            return mid
        elif mid**2>x:
            r=mid
        else:
            l=mid


# In[95]:


mySqrt(0)


# ### Climbing Stairs
# 
# You are climbing a stair case. It takes n steps to reach to the top.
# 
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# 
# Note: Given n will be a positive integer.
# 
# Example 1:
# 
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:
# 
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

# # Recursive 
# # Bottom up 
# # Top Down

# In[4]:


def climbStairs(n):
    if n==0 or n== 1:
        return 1
    return climbStairs(n-1)+climbStairs(n-2)


# In[17]:


def climbStairs(n):
    if n==1:
        return 1
    res=[0 for x in range(n)]
    res[0],res[1]=1,2
    for i in range(2,n):
        res[i]=res[i-1]+res[i-2]
    return res[-1]


# In[16]:


climbStairs(35)


# ### Remove Duplicates from Sorted List
# 
# Given a sorted linked list, delete all duplicates such that each element appear only once.
# 
# Example 1:
# 
# Input: 1->1->2
# Output: 1->2
#     
# Example 2:
# 
# Input: 1->1->2->3->3
# Output: 1->2->3

# In[22]:


input=[1,1,2]
input=[1,1,2,3,3]


# In[28]:


def deleteDuplicates(head):
    L=[]
    for x in head:
        if x not in L:
            L.append(x)
    return L


# In[ ]:


def deleteDuplicates(head):
    for x in head:
        if x 


# In[29]:


deleteDuplicates(input)


# In[ ]:





# ### Merge Sorted Array
# 
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
# 
# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
# Example:
# 
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# 
# Output: [1,2,2,3,5,6]

# In[56]:


#do without built in function
#build a sort function myself!
def merge(nums1,m,nums2,n):
    L=nums1[:m]+nums2[:n]
    sortList=[]
    i=0
    while len(L)>1:
        if sum([1 if x<=L[i] else 0 for x in L[i+1:] ])==0:
            sortList.append(L[i])
            L=L[:i]+L[i+1:]
            i=0#必须回到0，重新开始扫
        elif i==len(L)-1:
            sortList.append(L[i])
            L=L[:i]
        else:
            i+=1
    sortList.append(L[0])
    return sortList


# In[53]:


nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
merge(nums1,3,nums2,3)


# ### Single Number

# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
# Input: [2,2,1]
# Output: 1

# In[85]:


def singleNumber(nums): #runtime error
    i=0
    while i<len(nums)-1:
        if nums[i] in nums[1:]:
            nums=[x for x in nums if x!=nums[i]]
        else:
            i+=1
    if len(nums)==0:
        return 0
    else:
        return nums[0]


# In[84]:


def singleNumber(nums):
    if len(nums)==1:
        return nums[0]
    nums=sorted(nums)
    i=0
    while i<len(nums)-1:
        if nums[i]!=nums[i+1]:
            return nums[i]
        else:
            i+=2
    if nums[-1]==nums[-2]:
        return 0
    else:
        return nums[-1]


# In[103]:


def singleNumber(nums):
    dict={}
    for num in nums:
        dict[num]=dict.get(num,0)+1
    for key,val in dict.items():
        if val==1:
            return key


# In[107]:


def singleNumber(nums):
    set1=set(nums)
    return sum(set1)*2-sum(nums)


# In[104]:


a=[2,2,1,1,3,3,4,4,5,5]
singleNumber(a)


# In[106]:


2*[2,1]


# ### Two Sum II - Input array is sorted

# In[ ]:


Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.


# In[30]:


def twoSum(numbers,target):
    a=[[1+numbers.index(x), 1+1+numbers.index(x)+numbers[numbers.index(x)+1:].index(y)] for x in numbers for y in numbers[numbers.index(x)+1:] if x+y==target]
    return a[0]


# In[31]:


numbers=[2,7,11,15]
target = 9
twoSum(numbers,target)


# In[39]:


def twoSum(numbers,target):
    min,max=numbers[0],numbers[-1]
    while min+max!=target:
        if min+max>target:
            max=numbers[numbers.index(max)-1]
        else:
            min=numbers[numbers.index(min)+1]
    if min==max:
        return [numbers.index(min)+1,numbers.index(min)+1+numbers[numbers.index(min)+1:].index(max)+1] 
    return [numbers.index(min)+1,numbers.index(max)+1]     


# In[41]:


#two-pointer
def twoSum(numbers,target):
    l,r=0,len(numbers)-1
    while l<r:
        if numbers[l]+numbers[r]==target:
            return l+1,r+1
        elif numbers[l]+numbers[r]>target:
            r=r-1
        else:
            l=l+1


# In[63]:


#dictionary 
def twoSum(numbers,target):
    dic={}
    for i,num in enumerate(numbers):
        if target-num in dic:
            return(dic[target-num]+1,i+1)
        dic[num]=i
#only need search 1/2(at most)

#2nd 会有重名问题[0,0,3,4] target0
def twoSum(numbers,target):
    dic={num:i for i,num in enumerate(numbers)}
    for num in numbers:
        if target-num in dic:
            return [dic[num]+1,dic[target-num]+1]


# In[74]:


#binary search
def twoSum(numbers,target):
    for i in range(len(numbers)):
        l,r=i+1,len(numbers)-1
        while l<=r:
            mid=(l+r)//2
            if numbers[i]+numbers[mid]==target:
                return [i+1,mid+1]
            elif numbers[i]+numbers[mid]>target:
                r=mid-1
            else:
                l=mid+1


# In[75]:


numbers=[2,7,11,15]
target = 9
twoSum(numbers,target)


# ### Palindrome Number

# In[ ]:


Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.


# In[92]:


def Palindrome(x):
    if x<0:
        return False
    else:
        x=str(x)
        digList=[digit for digit in x]
        revdig=''.join(reversed(digList))
        if x==revdig:
            return True
        else:
            return False


# In[97]:


#Palidrome reverse a integer
def Palidrome(x):
    if x<0:
        return False
    else:
        p,res=x,0
        while p:
            res=res*10+p%10
            p=p//10
        if res==x:
            return True
        else:
            return False


# In[93]:


Palindrome(121)


# ### 13. Roman to Integer

# In[ ]:


Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.


Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
    
Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


# In[4]:


def romanToInt(s):
    dic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    intvalue=0
    i=0
    while i<len(s)-1:
        if dic[s[i]]<dic[s[i+1]]:
            intvalue=intvalue-dic[s[i]]
        else:
            intvalue=intvalue+dic[s[i]]
        i+=1
    return intvalue+dic[s[-1]] #the rule is if the previous digit less than the latter one, it should be deducted


# In[5]:


roman="MCMXCIV"
romanToInt(roman)


# ### 14.Longest Common Prefix

# In[ ]:


Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


# In[37]:


def longestCommonPrefix(strs):
    if len(strs)==0:
        return ''
    else:
        #dic={len(word):word for word in strs}
        #shortest_term=dic[min(dic.keys())]
        shortest_term=min(strs,key=len)
        i=0
        while sum([1 for word in strs if shortest_term[:i+1]==word[:i+1]])==len(strs) and i<=len(strs):
            i+=1
        return shortest_term[:i]


# In[39]:


strs=["dog","racecar","car"]
shortest = min(strs,key=len)
shortest


# In[36]:


input=[""]
longestCommonPrefix(input)


# ### 169. Majority Element

# In[ ]:


Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2


# In[43]:


def majorityElement(nums):
    dic={}
    for x in nums:
        if x not in dic:
            dic[x]=1
        else:
            dic[x]+=1
    for x in dic:
        if dic[x]==max(dic.values()):
            return x


# In[44]:


input=[2,2,1,1,1,2,2]
majorityElement(input)


# ### 172. Factorial Trailing Zeroes

# Given an integer n, return the number of trailing zeroes in n!.
# 
# Example 1:
# 
# Input: 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.
# Example 2:
# 
# Input: 5
# Output: 1
# Explanation: 5! = 120, one trailing zero.

# In[62]:


def trailingZeros(n):#time limit
    a=1
    for i in range(1,n+1):
        a=a*i
    trail=0
    while a%10==0:
        trail+=1
        a=a/10
    return trail


# In[68]:


def trailingZeros(n):
    result=0
    while n>0:
        result+=n//5 #generate new 0 like(25,125)
        n=n//5
    return result


# In[69]:


trailingZeros(5)


# ### Valid Parentheses

# In[ ]:


Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Input: "()"
Output: true

Input: "()[][]"
Output: true

Input: "(]"
Output: false
    
Input: "([)]"
Output: false

Input: "{[]}"
Output: true


# In[103]:


def isValid(s):
    if s=='':
        return True
    else:
        parlist=['()','[]','{}']
        while '()'in s or '[]'in s or '{}'in s:
            if '()' in s:
                s=s.replace('()','')
            elif '[]' in s:
                s=s.replace('[]','')
            else:
                s=s.replace('{}','')
        if s=='':
            return True
        else:
            return False


# In[108]:


def isValid(s):
    if s=='':
        return True
    stack=[]
    dic={'(':')','[':']','{':'}'}
    for i in s:
        if i in dic:
            stack.append(i)
        elif len(stack)==0 or dic[stack.pop()]!=i:#先出)
            return False
    if stack==[]:
        return True


# In[109]:


isValid("{[]}")


# In[116]:


import numpy as np
foursec=0
for _ in range(1000000):
    if sum([1 if np.random.random()<0.5 else 0 for i in range(4)])==4:
        foursec+=1
foursec/1000000


# ### 190. Reverse Bits

# Reverse bits of a given 32 bits unsigned integer.
# 
# 
# Input: 00000010100101000001111010011100
# Output: 00111001011110000010100101000000
# Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
# 
# Input: 11111111111111111111111111111101
# Output: 10111111111111111111111111111111
# Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10101111110010110010011101101001.

# In[140]:


def reverseBits(n):
    """
    Input decimal-->binary-->reversed-->decimal
    """
    oribin='{0:032b}'.format(n)
    print(oribin)
    #reversebin=int(''.join(reversed(oribin)),2)
    return oribin[::-1]


# In[144]:


def reverseBits(n):
    oribin='{0:032b}'.format(n)#-->binary
    revoribin=oribin[::-1]#reversed binary
    decimal=0
    for i in range(len(oribin)):
        decimal+=int(oribin[i])*2**i
    return decimal
              


# ### 191.Number of 1 Bits

# In[ ]:


Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).

Input: 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

Input: 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.

Input: 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.


# In[151]:


def hammingWeight(n):
    """
    type n: int(decimal)
    """
    oribin=bin(n)
    return sum([1 for d in oribin if d!='0'])


# ### 198.House Robber

# In[ ]:


You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.


Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.


# In[171]:


def rob(nums):
    """
    return max money can steal
    """
    i=len(nums)
    robL=[]
    while i>=0:
        if rob(nums[:i-2])+nums[i]>=rob(nums[:i-1]):#rob last house
            robL.append(i)
            i=i-2
        else:
            i=i-1
    return sum(robL)


# In[177]:


#recursive
def rob(nums):
    """
    return max money can steal
    """
    if len(nums)==0:
        return 0
    if len(nums)<=2:
        return max(nums)
    res=[0]*len(nums)
    res[0],res[1]=nums[0],max(nums[0],nums[1])
    for i in range(2,len(nums)):
        res[i]=max(res[i-2]+nums[i],res[i-1])#from 0 to i house, accumulated max money has stole
    return res[-1]


# In[176]:


nums=[2,7,9,3,1]
rob(nums)


# ### 70. Climbing Stairs 2nd time

# In[ ]:


You are climbing a stair case. It takes n steps to reach to the top.

get_ipython().set_next_input('Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top');get_ipython().run_line_magic('pinfo', 'top')

Note: Given n will be a positive integer.
    
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


# In[182]:


def climbStairs(n):
    """
    f(n)=f(n-1)+f(n-2)
    """
    if n<=1:
        return n
    res=[0]*n
    res[0],res[1]=1,2
    for i in range(2,n):
        res[i]=res[i-1]+res[i-2]
    return res[-1]


# ### 7. Reverse Integer

# In[ ]:


Input: 123
Output: 321

Input: -123
Output: -321

Input: 120
Output: 21


# In[188]:


def reverse(x):
    if x<0:
        return -reverse(-x)
    else:
        rev=0
        while x>0:
            rev=rev*10+x%10
            x=x//10
    return rev
    #return rev if -(2**31)-1<rev< 2**31 else 0 #cheat code to meet 'Given a 32-bit signed integer'


# In[190]:


reverse(1534236469)


# ### 202. Happy Number

# In[ ]:


Write an algorithm to determine if a number is "happy".

Starting with any positive integer, replace the number by the sum of the squares of its digits, 
and repeat the process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1. 
Those numbers for which this process ends in 1 are happy numbers.

Input: 19
Output: true
Explanation: 
1**2 + 9**2 = 82
8**2 + 2**2 = 68
6**2 + 8**2 = 100
1**2 + 0**2 + 0**2 = 1


# In[35]:


def isHappy(n):
    if n==1:
        return True
    else:
        import numpy as np
        historySum=[]
        sum=n
        while sum!=1:
            sum=np.sum([int(digit)**2 for digit in str(sum)])
            if sum==1:
                return True
            elif sum in historySum:
                return False
            else:
                historySum.append(sum)


# In[41]:


pow(19%10,2)


# ### 167. Two Sum II - Input array is sorted 2nd

# In[ ]:


Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.


# In[46]:


#two-pointer
def twoSum(numbers,target):
    l,r=0,len(numbers)-1
    while l<r:
        if numbers[l]+numbers[r]==target:
            return [l,r]
        elif numbers[l]+numbers[r]>target:
            r-=1
        else:
            l+=1


# In[57]:


#binary search
def twoSum(numbers,target):
    length=len(numbers)-1
    for i in range(len(numbers)):
        l,r=i+1,length
        while l<=r:
            mid=(l+r)//2
            if numbers[i]+numbers[mid]>target:
                r=mid-1
            elif numbers[i]+numbers[mid]<target:
                l=mid+1
            else:
                return [i+1,mid+1]


# In[58]:


twoSum([2,7,11,15],9)


# ### 26. Remove Duplicates from Sorted Array 2nd time

# In[ ]:


Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.


Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.


# In[69]:


def removeDuplicates(nums):
    dic={x:1 for x in nums}
    nums[:]=sorted([x for x in dic.keys()])
    return len(nums)


# In[70]:


nums = [0,0,1,1,1,2,2,3,3,4]
removeDuplicates(nums)


# ### 205. Isomorphic Strings

# In[ ]:


Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Input: s = "egg", t = "add"
Output: true

Input: s = "foo", t = "bar"
Output: false

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.


# In[29]:


def isIsomorphic(s,t):
    dic1={}
    for i in range(len(s)):
        if s[i] in dic1:
            dic1[s[i]].append(i)
        else:
            dic1[s[i]]=[i]
    dic2={}
    for i in range(len(s)):
        if t[i] in dic2:
            dic2[t[i]].append(i)
        else:
            dic2[t[i]]=[i]
    
    return [x for x in dic1.values()] == [x for x in dic2.values()]


# In[43]:


def isIsomrphic(s,t):
    return [s.find(x) for x in s]==[t.find(x) for x in t]


# In[47]:


isIsomorphic("abba","abab")


# ### 217. Contains Duplicate

# In[ ]:


Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.


Input: [1,2,3,1]
Output: true

Input: [1,2,3,4]
Output: false

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true


# In[52]:


def containDuplicate(nums): #Time Limit
    i=0
    while i<len(nums)-1:
        if sorted(nums)[i]==sorted(nums)[i+1]:
            return True
        else:
            i+=1
    return False


# In[106]:


def containDuplicates(nums):
    s=set()
    for x in nums:
        if x not in s:
            s.add(x)
        else:
            return True
    return False


# In[113]:


def containDuplicates(nums):
    L=[]
    for x in nums:
        if x not in L:
            L.append(x)
        else:
            return True
    return False


# In[108]:


def containsDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    return len(nums)>len(set(nums))


# In[114]:


nums=[1,2,3,4]
containDuplicates(nums)


# ### 219. Contains Duplicate II

# In[ ]:


Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.


Input: nums = [1,2,3,1], k = 3
Output: true

Input: nums = [1,0,1,1], k = 1
Output: true

Input: nums = [1,2,3,1,2,3], k = 2
Output: false


# In[129]:


def containNearbyDuplicate(nums,k):#Time Limit
    i=0
    while i<len(nums):
        tnums=nums[0:i]+nums[i+1:]
        if len(set(tnums))==len(set(nums)):#duplicate
            m=i+1
            while m<len(nums):
                if nums[m]==nums[i] and m-i<=k:
                    return True
                else:
                    m+=1
        i+=1 #move on
    return False


# In[138]:


#using index-->enumerate
#do saving -->dic instead of 

def containNearbyDuplicate(nums,k):
    dic={}
    for i,v in enumerate(nums):
        if v in dic and i-dic[v]<=k:
            return True
        dic[v]=i #important!#always store the latest index if having same value
    return False


# In[137]:


nums = [1,2,3,1,2,3]
k = 2
containNearbyDuplicate(nums,k)


# ### 231. Power of Two

# In[ ]:


Given an integer, write a function to determine if it is a power of two.

Input: 1
Output: true 
Explanation: 2**0 = 1

Output: true
Explanation: 2**4 = 16


# In[147]:


def isPowerOfTwo(n):
    if n<=0:
        return False
    else:
        while n>1:
            if n%2!=0:
                return False
            else:
                n=n/2
    return True


# In[148]:


isPowerOfTwo(1)


# ### insert 5

# In[150]:


def returninsertfive(n):
    """
    n:int
    """
    if n<0:
        n=-1*n
        s=str(n)
        L=[]
        for i in range(len(s)+1):
            l=[d for d in s]
            l.insert(i,'5')
            L.append(int(''.join(l)))
        return min(L)*(-1)
    else:
        s=str(n)
        L=[]
        for i in range(len(s)+1):
            l=[d for d in s]
            l.insert(i,'5')
            L.append(int(''.join(l)))
        return max(L)


# In[151]:


returninsertfive(1)


# In[157]:


a='123'
l=[x for x in a]
l.insert(3,5)
l


# ### 258. Add Digits

# In[ ]:


Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.


# In[5]:


def addDigits(num):
    while num>=10:
        num=sum([int(d) for d in str(num)])
    return num


# In[6]:


addDigits(38)


# In[22]:


###recursion!!!


# In[20]:


def addDigits2(num):
    if 0<=num<=9:
        return num  ###actually only return here!
    tmp=0
    while num:
        tmp+=num%10
        num=num//10
    return addDigits2(tmp) #here only do things like addDigits2(1888)-->addDigits(25)-->addDigits2(7)


# In[21]:


addDigits2(38)


# ### 263. Ugly Number

# In[ ]:


Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Input: 6
Output: true
Explanation: 6 = 2 × 3

Input: 14
Output: false 
Explanation: 14 is not ugly since it includes another 


# In[36]:


def isUgly(num): 
    """
    :type num:int
    :rtype:bool
    """
    if num<=0:
        return False
    while num%2==0 or num%3==0 or num%5==0:
        if num%2==0:
            num=num/2
        elif num%3==0:
            num=num/3
        else:
            num=num/5
    return num==1
    


# In[41]:


def isUgly(num):  #Better solution
    """
    :type num:int
    :rtype:bool
    """
    if num<=0:
        return False
    for x in [2,3,5]:
        while num%x==0:
            num=num/x
    return num==1
            


# In[42]:


isUgly(0)


# ### 268. Missing Number

# In[ ]:


Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Input: [3,0,1]
Output: 2

Input: [9,6,4,2,3,5,7,0,1]
Output: 8


# In[61]:


def missingNumber(nums):
    expected_nums=[x for x in range(len(nums)+1)]
    return sum(expected_nums)-sum(nums)


# In[59]:


def missingNumber(nums):
    for i,v in enumerate(sorted(nums)):
        if i!=v:
            return i


# In[63]:


nums=[0,1]
missingNumber(nums)


# ### 283. Move Zeroes

# In[ ]:


Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.


Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.


# In[233]:


def moveZeros(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    i=0
    zeronums=sum([1 for x in nums if x==0])
    while i<len(nums)-zeronums:
        if nums[i]==0:
            del nums[i] #remove by element
            nums.append(0)
        else:
            i+=1
    return nums


# In[234]:


nums=[0,1,0,3,12]
moveZeros(nums)


# ### 326. Power of Three

# In[ ]:


Given an integer, write a function to determine if it is a power of three.

Input: 27
Output: true

Input: 0
Output: false

Input: 9
Output: true


# In[242]:


def isPowerOfThree(n):
    if n<=0:
        return False
    else:
        while n>1:
            if n%3==0:
                n=n/3
            else:
                return False
        return True


# In[244]:


isPowerOfThree(81)


# ### 342. Power of Four

# In[246]:


def isPowerOfFour(num):
    if num<=0:
        return False
    else:
        while num>1:
            if num%4==0:
                num=num/4
            else:
                return False
        return True


# ### 344. Reverse String

# In[ ]:


Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.


Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]


# In[4]:


def reverseString(s):
    s[:]=s[::-1]
    return s


# In[23]:


#recusion
def reverseString(s):
    if len(s)==1:
        return s
    else:
        l=len(s)
        return reverseString(s[l//2:])+reverseString(s[:l//2])


# In[24]:


s=["h","e","l","l","o"]
reverseStringt(s)


# ### 278. First Bad Version

# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
# 
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
# 
# You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
# 
# Example:
# 
# Given n = 5, and version = 4 is the first bad version.
# 
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
# 
# Then 4 is the first bad version. 

# In[2]:


def firstBadversion(n):
    l,r=1,n
    while l<=r:
        mid=(l+r)//2
        if isBadVersion(mid):
            r=mid-1
        else:
            l=mid+1
    return l


# ### 448. Find All Numbers Disappeared in an Array

# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
# 
# Find all the elements of [1, n] inclusive that do not appear in this array.
# 
# Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
# 
# Example:
# 
# Input:
# [4,3,2,7,8,2,3,1]
# 
# Output:
# [5,6]

# In[25]:


def findDisappeardNumbers(nums):
    L=[]
    for i,v in enumerate(nums):
        if i+1!=v:
            if i+1 not in nums:
                L.append(i+1)
    return L


# In[66]:


def findDisappeardNumbers(nums):
    for i in range(len(nums)):
        index=abs(nums[i])-1
        nums[index]=-abs(nums[index])
    return [i+1 for i in range(len(nums)) if nums[i]>0]


# In[67]:


nums=[4,3,2,7,8,2,3,1]
findDisappeardNumbers(nums)


# In[64]:


abs(-13)


# ### 345. Reverse Vowels of a String

# In[ ]:


Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"


# In[72]:


def reverseVowels(s):
    vowels=['a','e','i','o','u','A','E','I','O','U']
    reverse_vowels=[l for l in s if l in vowels][::-1]
    L=[]
    i=0
    for l in s:
        if l not in vowels:
            L.append(l)
        else:
            L.append(reverse_vowels[i])
            i+=1
    return ''.join(L)


# In[2]:


#two pointer
def reverseVowels(s):
    s=list(s)
    vowels=['a','e','i','o','u','A','E','I','O','U']
    l,r=0,len(s)-1
    while l<r:
        if s[l] not in vowels:
            l+=1
        if s[r] not in vowels:
            r-=1
        if s[l]in vowels and s[r] in vowels:
            #print(l,r)
            s[l],s[r]=s[r],s[l]
            l+=1
            r-=1
           
    return ''.join(s)


# In[3]:


reverseVowels('leetcode')#race a car


# ### 349. Intersection of Two Arrays

# In[ ]:


Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]


# In[9]:


def intersection(nums1, nums2):
    return list(set([x for x in nums1 if x in nums2]))


# In[16]:


def intersection(nums1, nums2):
    return list(set(nums1)&set(nums2))


# In[17]:


nums1 = [1,2,2,1]
nums2 = [2,2]
intersection(nums1,nums2)


# In[ ]:




