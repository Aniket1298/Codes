def g(n):
    return (n*(n-1))/2
class Solution(object):
    def threeSumMulti(self, A, target):
        d={}
        for i in range(101):
            d[i]=0
        for i in A:
            d[i]+=1
        ans=0
        M=pow(10,9)+7
        for i in xrange(target+1):
            if i+i+i==target and i<101:
                x=d[i]
                ans+=(x*(x-1)*(x-2))/6
                ans%=M
            for j in xrange(i+1,target+1):
                if i+j+j==target and i<101 and j<101:
                    #print i,j,j,ans
                    ans+=d[i]*g(d[j])
                    ans%=M
                    #print ans
                if j+i+i==target and i<101 and j<101:
                    #print j,i,i,ans
                    ans+=d[j]*g(d[i])
                    ans%=M
                    #print ans
                for k in xrange(j+1,target):
                    if i+j+k==target and i<101 and j<101 and k<101:
                        #print i,j,k,ans
                        ans+=d[i]*d[j]*d[k]
                        ans%=M
                        #print ans
        #print ans,d[target]
        
        return ans