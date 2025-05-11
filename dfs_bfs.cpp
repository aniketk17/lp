#include<bits/stdc++.h>
using namespace std;

class Graph {
    vector<vector<int>> adj;
    int v;

public:
    Graph(int v) {
        this->v = v;
        adj.resize(v);
    }

    void addEdge(int u, int v) {
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    void dfs(int node, vector<int> &visited) {
        cout << node << " ";
        visited[node] = 1;
        for(auto neighbour : adj[node]) {
            if(!visited[neighbour]) {
                dfs(neighbour, visited);
            }
        }
    }

    void dfsIterative(int src) {
        stack<int> st;
        vector<int> visited(v, 0);
        st.push(src);

        while(!st.empty()) {
            int node = st.top();
            st.pop();
            if (!visited[node]) {
                cout << node << " ";
                visited[node] = 1;
                for(auto neighbour : adj[node]) {
                    if(!visited[neighbour]) {
                        st.push(neighbour);
                    }
                }
            }   
        }
    }

    void bfsRecursive(queue<int> &q, vector<int> &visited) {
        if(q.empty()) return;
        int node = q.front(); q.pop();
        cout << node << " ";

        for(auto neighbour : adj[node]) {
            if(!visited[neighbour]) {
                q.push(neighbour);
                visited[neighbour] = 1;
            }
        }

        bfsRecursive(q, visited);
    }

    void bfs(int node, vector<int> &visited) {
        queue<int> q;
        visited[node] = 1;
        q.push(node);
        bfsRecursive(q, visited);
    }

    void bfsIterative(int src) {
        vector<int> visited(v, 0);
        queue<int> q;
        q.push(src);
        visited[src] = 1;

        while(!q.empty()) {
            int node = q.front(); q.pop();
            cout << node << " ";
            for(auto neighbour : adj[node]) {
                if(!visited[neighbour]) {
                    q.push(neighbour);
                    visited[neighbour] = 1;
                }
            }
        }
    }
};

int main() {
    int v, e;
    cout << "Enter number of vertices: ";
    cin >> v;
    cout << "Enter number of edges: ";
    cin >> e;

    Graph g(v);
    cout << "Enter edges (u,v):" << endl;

    for(int i = 0; i < e; i++) {
        int u, v;
        cin >> u >> v;
        g.addEdge(u, v);
    }

    int start;
    cout << "Enter starting vertex: ";
    cin >> start;

    vector<int> visitedDFS(v, 0);
    cout << "Recursive DFS: ";
    g.dfs(start, visitedDFS);
    cout << endl;

    cout << "Iterative DFS: ";
    g.dfsIterative(start);
    cout << endl;

    vector<int> visitedBFS(v, 0);
    cout << "Recursive BFS: ";
    g.bfs(start, visitedBFS);
    cout << endl;

    cout << "Iterative BFS: ";
    g.bfsIterative(start);
    cout << endl;

    return 0;
}
