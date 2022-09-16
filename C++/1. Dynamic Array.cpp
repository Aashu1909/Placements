#include<iostream>
using namespace std;
#include<bits/stdc++.h>

vector<int> solve(vector<vector<int>> v)
{
    vector<vector<int>> v1;
    map<int,int> m;

    for(int i=0;i<v.size();i++)
    {
        vector<int> v2;
        v2=v[i];
        v2.erase(unique(v2.begin(),v2.end()),v2.end());
        v1.push_back(v2);
    }
    for(int i=0;i<v1.size();i++)
    {
        for(int j=0;j<v1[0].size();j++)
        {
            m[v1[i][j]]++;
        }
    }
    for(auto it:m)
    {
        if(it.second==v.size())
        {
            v3.push_back(it.first);
        }
    }
    return v3;
}