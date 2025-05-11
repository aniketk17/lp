#include <bits/stdc++.h>
using namespace std;

int primeMst(vector<vector<pair<int, int>>> &adj, int V) {
    vector<int> key(V, INT_MAX);     // Stores the minimum weight to reach each vertex
    vector<bool> mst(V, false);      // Marks if vertex is included in MST
    vector<int> parent(V, -1);       // Stores the parent of each vertex in MST

    key[0] = 0;

    for (int i = 0; i < V; i++) {
        int mini = INT_MAX, u = -1;

        // Find the minimum key vertex not included in MST
        for (int v = 0; v < V; v++) {
            if (!mst[v] && key[v] < mini) {
                mini = key[v];
                u = v;
            }
        }

        mst[u] = true;

        for (auto &[v, w] : adj[u]) {
            if (!mst[v] && w < key[v]) {
                key[v] = w;
                parent[v] = u;
            }
        }
    }

    int totalCost = 0;
    cout << "Edges in the MST:\n";
    for (int i = 1; i < V; i++) {
        cout << parent[i] << " - " << i << " with weight " << key[i] << "\n";
        totalCost += key[i];
    }

    return totalCost;
}

int main() {
    int V = 5;
    vector<vector<pair<int, int>>> adj(V);

    // Example graph
    adj[0].push_back({1, 2});
    adj[1].push_back({0, 2});

    adj[0].push_back({3, 6});
    adj[3].push_back({0, 6});

    adj[1].push_back({2, 3});
    adj[2].push_back({1, 3});

    adj[1].push_back({3, 8});
    adj[3].push_back({1, 8});

    adj[1].push_back({4, 5});
    adj[4].push_back({1, 5});

    adj[2].push_back({4, 7});
    adj[4].push_back({2, 7});

    int mstCost = primeMst(adj, V);
    cout << "Total cost of MST: " << mstCost << endl;

    return 0;
}

// linear search - o(v^2)
// using pq - ((v+e)log V)