class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n=len(nums)
        size=4*n
        
        prod=[1]*size
        cnt=[[0]*k for _ in range(size)]
        
        def build(node,l,r):
            if l==r:
                prod[node]=nums[l]%k
                cnt[node][prod[node]]=1
                return
            
            mid=(l+r)//2
            
            build(node*2,l,mid)
            build(node*2+1,mid+1,r)
            
            left_prod=prod[node*2]
            right_prod=prod[node*2+1]
            
            prod[node]=(left_prod*right_prod)%k
            
            for i in range(k):
                cnt[node][i]+=cnt[node*2][i]
            
            for i in range(k):
                new_value=(left_prod*i)%k
                cnt[node][new_value]+=cnt[node*2+1][i]
        
        def update(node,l,r,pos,value):
            if l==r:
                prod[node]=value%k
                cnt[node]=[0]*k
                cnt[node][prod[node]]=1
                return
            
            mid=(l+r)//2
            
            if pos<=mid:
                update(node*2,l,mid,pos,value)
            else:
                update(node*2+1,mid+1,r,pos,value)
            
            left_prod=prod[node*2]
            right_prod=prod[node*2+1]
            
            prod[node]=(left_prod*right_prod)%k
            
            cnt[node]=[0]*k
            
            for i in range(k):
                cnt[node][i]+=cnt[node*2][i]
            
            for i in range(k):
                new_value=(left_prod*i)%k
                cnt[node][new_value]+=cnt[node*2+1][i]
        
        def query(node,l,r,start):
            if l>=start:
                return prod[node],cnt[node]
            
            mid=(l+r)//2
            
            if start>mid:
                return query(node*2+1,mid+1,r,start)
            
            left_prod,left_cnt=query(node*2,l,mid,start)
            
            if start>r:
                return left_prod,left_cnt
            
            right_prod,right_cnt=query(node*2+1,mid+1,r,start)
            
            new_cnt=[0]*k
            
            for i in range(k):
                new_cnt[i]+=left_cnt[i]
            
            for i in range(k):
                new_value=(left_prod*i)%k
                new_cnt[new_value]+=right_cnt[i]
            
            new_prod=(left_prod*right_prod)%k
            
            return new_prod,new_cnt
        
        build(1,0,n-1)
        
        result=[]
        
        for query_data in queries:
            index,value,start,x=query_data
            
            update(1,0,n-1,index,value)
            
            p,c=query(1,0,n-1,start)
            
            result.append(c[x])
        
        return result