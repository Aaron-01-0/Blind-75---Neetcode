def ContainsDuplicate(nums):
  seen - set()
  for num in nums:
    if num in seen:
      return True
    seen.add(num)
  return False

#One Liner
def ContainsDuplicate(nums):
# If the set is shorter than the list, a duplicate was removed!
    return len(set(nums)) != len(nums)
