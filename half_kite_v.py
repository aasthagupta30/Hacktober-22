#User function Template for python3

class Solution:
    def printTriangle(self, N):
        # Code here
        for i in range(N):
            for j in range(N):
                if(i>=j):
                    print("* ",end="")
            print()
        n=N-1
        for i in range(n):
            for j in range(n):
                if((i+j)<=n-1):
                    print("* ",end="")
            print()


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
