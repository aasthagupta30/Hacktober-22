#User function Template for python3

class Solution:
    def printTriangle(self, N):
        # Code here
        for i in range(N):
            abc=64
            for j in range(N+i):
                if(j<(N-i-1)):
                    print(" ",end="")
                else:
                    if(j<=N-1):
                        abc+=1
                        print(chr(abc),end="")
                    else:
                        abc-=1
                        print(chr(abc),end="")
                    # print("*",end="")
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
