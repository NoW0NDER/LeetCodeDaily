class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l1=len(s)
        l2=len(t)
        if l1>l2:
          return False
        else:
          j = 0
          for i in range(l1):
            while j<=l2:
              if j==l2:
                return False
              else:
                if t[j]==s[i]:
                  if i==l1-1:
                    return True
                  else:
                    j+=1
                    break
                else:
                  j+=1
        return True
        