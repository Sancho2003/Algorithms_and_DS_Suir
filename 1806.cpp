#include <bits/stdc++.h>

using namespace std;

const int N=50005;
int head[N], I;

struct node
{
    int j,next,t;
}side[N*50];

int cost[N];
map<string,int>mt;
map<string,int>::iterator it;
int f[N], dist[N];
bool in[N];
string s[N];
stack<int>st;


void add(int i,int j,int t)
{
    side[I].j=j;
    side[I].t=t;
    side[I].next=head[i];
    head[i]=I++;
}

int costtime(int i,int j)
{
    for(int x=0;x<10;++x)
    {
        if(s[i][x]!=s[j][x])
        return cost[x];
    }
    return 10;
}

bool spfa(int st,int nd)
{
    memset(in,false,sizeof(in));
    memset(dist,-1,sizeof(dist));
    queue<int>qt;
    qt.push(st);
    in[st]=true;
    dist[st]=0;
    while(!qt.empty())
    {
        int x=qt.front();qt.pop();
        in[x]=false;
        for(int t=head[x];t!=-1;t=side[t].next)
        {
            int j=side[t].j;
            if(dist[j]==-1||dist[j]>dist[x]+side[t].t)
            {
                dist[j]=dist[x]+side[t].t;
                f[j]=x;
                if(!in[j])
                {
                    in[j]=true;
                    qt.push(j);
                    }
            }
        }
    }

    if(dist[nd]==-1) return false;
    return true;
}

int main()
{
    int n;
    while(cin>>n)
    {
        for(int i=0;i<10;++i)
        cin>>cost[i];
        mt.clear();
        for(int i=1;i<=n;++i)
        {
            cin>>s[i];
            mt[s[i]]=i;
        }
        memset(head, -1, sizeof(head));
        I=0;
        for(int i=1;i<=n;++i)
        {
            s[0]=s[i];
            for(int l=0;l<10;++l)
            {
                char ctmp=s[i][l];
                for(char c='0'; c<='9'; ++c)
                {
                    if(ctmp==c)
                    continue;
                    s[i][l]=c;
                    if((it=mt.find(s[i]))!=mt.end())
                    add(i,it->second, costtime(0,it->second));
                }
                s[i][l]=ctmp;
            }
            for(int l=0;l<10;++l)
                for(int r=l+1;r<10;++r)
                {
                    if(s[i][l]==s[i][r])
                        continue;
                    swap(s[i][l],s[i][r]);
                    if(( (it=mt.find(s[i]))) != mt.end() )
                        add(i,it->second, costtime(0,it->second));
                        swap(s[i][l],s[i][r]);
                }
        }
        if(!spfa(1,n))
        cout<<"-1"<<endl;
        else
        {
            while(!st.empty())
            st.pop();
            int k=n;
            while(k!=1)
            {
                st.push(k);
                k=f[k];
            }
            cout<<dist[n]<<endl;
            cout<<(st.size()+1)<<endl;
            cout<<"1";
            while(!st.empty())
            {
                cout<<" "<<st.top();
                st.pop();
            }
            cout<<endl;
        }
    }
    return 0;
}
