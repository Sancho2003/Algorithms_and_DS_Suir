#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

struct Node
{ 
    int u,v,len;
    bool operator <(const Node &th) const
    { 
        return len<th.len;
    }
}; 

int cmp(const void *_a,const void *_b)
{
    Node *a = (Node *)_a;
    Node *b = (Node *)_b;
    return a->len-b->len;
}

Node nodes[15001];
int ans[15001],count=0, p[1001], m, n, lenn, num=0;

int find(int x)
{
    return x==p[x]?x:p[x]=find(p[x]);
}

int main()
{
    cin>>n>>m;
    for(int i=0; i<m; i++)
    {
        cin>>nodes[i].u>>nodes[i].v>>nodes[i].len;
    }
    
    sort (nodes, nodes+m) ;
    
    for(int i=1; i<=n; i++)
        p[i]=i;
    for(int i=0; i<m; i++)
    {
        int tx=find(nodes[i].u);
        int ty=find(nodes[i].v);
        if(tx!=ty)
        {
            lenn=nodes[i].len; 
            ans[num++]=i;
            p[tx]=ty;
        }
        if(num==n-1) break;
    }
    cout<<lenn<<endl<<num<<endl;
    for(int i=0; i<num; i++)
        cout<<nodes[ans[i]].u<<" "<<nodes[ans[i]].v<<endl;
    return 0;
}
