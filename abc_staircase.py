#User function Template for python3

class Solution:
    def printTriangle(self, N):
        # Code here
        abc=64
        for i in range(N):
            abc+=1
            for j in range(N):
                if(i>=j):
                    print(chr(abc),end="")
            print()
        return


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input().strip())
        ob = Solution()
        ob.printTriangle(N)
# } Driver Code Ends
