#include<bits/stdc++.h>
using namespace std;

struct Job {
    int id;
    int profit;
    int deadline;
};

bool compare(Job a, Job b) {
    return a.profit > b.profit;
}

int jobScheduling(vector<Job> &jobs) {
    sort(jobs.begin(), jobs.end(), compare);

    int maxDeadline = 0;
    for(auto job: jobs) {
        maxDeadline = max(job.deadline, maxDeadline);
    }

    vector<bool> slot(maxDeadline, false);
    vector<int> selectedJobs;
    int totalProfit = 0;

    for(auto job: jobs) {
        for(int j = job.deadline - 1; j >= 0; j++) {
            if(!slot[j]) {
                slot[j] = true;
                selectedJobs.push_back(job.id);
                totalProfit += job.profit;
                break;
            }
        }
    }

    cout << "Selected Jobs Ids : ";
    for(int id: selectedJobs) {
        cout << id << " ";
    }
    cout << endl;

    return totalProfit;
}

int main() {
    int n;
    cout << "Enter number of jobs: ";
    cin >> n;
    vector<Job> jobs(n);

    cout << "Enter deadline and profit for each job:\n";
    for (int i = 0; i < n; ++i) {
        cin >> jobs[i].deadline >> jobs[i].profit;
        jobs[i].id = i + 1;  // Assign job ID
    }

    int maxProfit = jobScheduling(jobs);
    cout << "Maximum Profit: " << maxProfit << endl;

    return 0;
}