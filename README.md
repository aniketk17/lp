# Viva Voce Questions and Answers Based on Lab Manual

## Graph Algorithms

### Kruskal's Algorithm

* **What is the fundamental principle behind Kruskal's algorithm for finding the Minimum Spanning Tree (MST)?**
    It's a greedy algorithm that selects edges in increasing order of their weights, adding an edge only if it doesn't form a cycle with already selected edges.
* **How does Kruskal's algorithm avoid cycles while building the MST?**
    It typically uses a Disjoint Set Union (DSU) data structure to keep track of connected components; an edge is added only if its two vertices belong to different components.
* **What data structure is typically used to efficiently check for cycles in Kruskal's algorithm? Explain its working.**
    A Disjoint Set Union (DSU) or Union-Find data structure is used. It maintains a collection of disjoint sets and supports operations to find the set a vertex belongs to and to unite two sets.
* **What is the time complexity of Kruskal's algorithm? How does it depend on the number of edges and vertices?**
    The time complexity is typically $O(E \log E)$ or $O(E \log V)$ (where E is edges, V is vertices), primarily due to sorting the edges and DSU operations.
* **When would you prefer Kruskal's algorithm over Prim's algorithm, and vice-versa?**
    Kruskal's is often preferred for sparse graphs (fewer edges) or when edges are already sorted or easily sortable. Prim's can be faster for dense graphs when using a Fibonacci heap.
* **Explain the greedy choice made at each step of Kruskal's algorithm.**
    The greedy choice is to always pick the next available edge with the smallest weight that does not form a cycle with the edges already selected.
* **How does the algorithm ensure that the final tree generated is indeed a *minimum* spanning tree?**
    This is proven by the "cut property" (or "safe edge property"), which states that for any cut, if the weight of an edge is strictly smaller than the weights of all other edges connecting the two partitions, then this edge belongs to all MSTs.
* **Can Kruskal's algorithm be used for directed graphs? Why or why not?**
    No, Kruskal's algorithm is designed for undirected graphs because the concept of a spanning tree itself applies to undirected graphs.
* **Describe a real-world application where Kruskal's algorithm could be useful.**
    Designing network layouts (like laying cables for internet or power) to connect multiple locations with minimum total cable length.
* **What happens if the graph has multiple edges with the same weight? Does Kruskal's algorithm still find a unique MST?**
    If there are multiple edges with the same weight, Kruskal's algorithm will still find an MST, but the MST might not be unique; different choices among same-weight edges could lead to different valid MSTs.

### Prim's Algorithm

* **Explain the core idea behind Prim's algorithm for finding the MST.**
    Prim's algorithm grows a single tree (the MST) from an arbitrary starting vertex, greedily adding the cheapest edge that connects a vertex in the growing tree to a vertex outside the tree.
* **How does Prim's algorithm grow the MST? Does it start from a single vertex or an edge?**
    It starts from a single arbitrary vertex and iteratively adds the minimum weight edge connecting a vertex in the current tree to a vertex not yet in the tree.
* **What data structure is commonly used to implement Prim's algorithm efficiently? How does it help?**
    A min-priority queue is commonly used to efficiently find the minimum weight edge to add from the set of available edges connecting vertices inside and outside the current tree.
* **What is the time complexity of Prim's algorithm using different data structures (e.g., adjacency matrix, adjacency list with min-priority queue)?**
    Using an adjacency matrix, it's $O(V^2)$. With an adjacency list and a binary heap, it's $O(E \log V)$. With a Fibonacci heap, it can be $O(E + V \log V)$.
* **Compare and contrast Prim's algorithm with Kruskal's algorithm in terms of their approach and complexity.**
    Prim's grows one connected component (the MST) from a start node, while Kruskal's sorts all edges and adds safe edges, potentially forming a forest that merges into an MST. Complexity varies by implementation but both are efficient greedy algorithms.
* **Explain the greedy strategy employed by Prim's algorithm.**
    At each step, it greedily chooses the edge with the minimum weight that connects a vertex already in the MST to a vertex not yet in the MST, without forming a cycle.
* **How does Prim's algorithm ensure that no cycles are formed in the MST?**
    It only adds edges that connect a vertex in the current MST to a vertex *outside* the current MST, so a cycle cannot be formed within the structure being built.
* **Can Prim's algorithm handle graphs with negative edge weights? Explain.**
    Yes, Prim's algorithm works correctly with graphs that have negative edge weights, as long as there are no negative cycles (which isn't an issue for MSTs as they are acyclic).
* **Describe a scenario or application where Prim's algorithm would be a suitable choice.**
    Network design, like finding the cheapest way to connect a set of computers where you start from one and branch out, or in pathfinding algorithms.
* **How does the algorithm terminate?**
    The algorithm terminates when V-1 edges have been added to the MST, or equivalently, when all vertices are included in the MST.

### BFS (Breadth-First Search)

* **What is the main objective of the Breadth-First Search (BFS) algorithm?**
    BFS aims to explore all vertices of a graph or tree by visiting neighbors at the current depth level before moving to neighbors at the next depth level.
* **Explain the order in which BFS explores the vertices of a graph.**
    BFS explores vertices level by level; it visits the starting node, then all its direct neighbors, then their unvisited neighbors, and so on.
* **What data structure is fundamental to the implementation of BFS, and why?**
    A queue is fundamental to BFS because it maintains the order of nodes to be visited, ensuring that nodes closer to the source are explored first (FIFO - First-In, First-Out).
* **What are the steps involved in the BFS algorithm?**
    1.  Start with a source vertex, mark it visited, and enqueue it.
    2.  While the queue is not empty, dequeue a vertex, process it.
    3.  Enqueue all its unvisited adjacent vertices and mark them visited.
* **What is the time and space complexity of BFS?**
    Time complexity is $O(V+E)$ and space complexity is $O(V)$ (where V is vertices, E is edges), as each vertex and edge is explored at most once.
* **Is BFS a complete algorithm (i.e., is it guaranteed to find a solution if one exists)? Is it optimal?**
    Yes, BFS is complete. It is also optimal for finding the shortest path in terms of the number of edges in unweighted graphs.
* **How can BFS be used to find the shortest path between two nodes in an unweighted graph?**
    BFS naturally finds the shortest path in terms of the number of edges because it explores level by level; the first time it reaches the target node, it's via the shortest path.
* **Describe how BFS handles cycles in a graph.**
    BFS handles cycles by keeping track of visited nodes; it only enqueues and processes a node if it hasn't been visited before, thus preventing infinite loops.
* **What are some common applications of the BFS algorithm?**
    Finding shortest paths in unweighted graphs, network broadcasting, finding connected components, and testing bipartiteness.
* **How does BFS differ from Depth-First Search (DFS) in terms of traversal and applications?**
    BFS explores level by level using a queue, finding shortest paths in unweighted graphs. DFS explores as far as possible along each branch using a stack (or recursion), used for tasks like topological sorting or cycle detection.

### DFS (Depth-First Search)

* **What is Depth-First Search (DFS), and how does it traverse a graph or tree?**
    DFS is an algorithm for traversing or searching graph or tree data structures by exploring as far as possible along each branch before backtracking.
* **Explain the recursive approach to implementing DFS.**
    A recursive DFS function visits a vertex, marks it as discovered, and then for each unvisited neighbor, it calls itself (recurses) on that neighbor.
* **What data structure is implicitly used in the recursive implementation of DFS? Can it be implemented iteratively? If so, how?**
    A stack is implicitly used by the system for recursion. Yes, DFS can be implemented iteratively using an explicit stack to keep track of vertices to visit.
* **What is the time and space complexity of DFS?**
    Time complexity is $O(V+E)$ and space complexity is $O(V)$ (where V is vertices, E is edges), as each vertex and edge is explored at most once.
* **How does DFS handle visited nodes to avoid infinite loops in graphs with cycles?**
    DFS uses a 'discovered' or 'visited' array/set to keep track of visited vertices, ensuring that each vertex is processed only once.
* **What are some applications of DFS (e.g., cycle detection, topological sorting, finding connected components)?**
    Applications include cycle detection in graphs, topological sorting for directed acyclic graphs, finding connected components, and solving puzzles like mazes.
* **Explain the concept of backtracking in the context of DFS.**
    In DFS, backtracking occurs when the algorithm has explored a branch as far as possible and returns to the previous vertex to explore other unvisited branches.
* **What are pre-order, in-order, and post-order traversals in the context of trees, and how do they relate to DFS?**
    Pre-order (node, left, right), in-order (left, node, right - for binary trees), and post-order (left, right, node) are specific types of DFS traversals for trees. DFS on a graph is closely related to pre-order traversal.
* **How can DFS be used to determine if a graph is connected?**
    Perform DFS from an arbitrary vertex; if all vertices are visited, the graph is connected (for undirected graphs).
* **Compare DFS with BFS in terms of their exploration strategy and typical use cases.**
    DFS explores branch by branch (depth-first) using a stack, suitable for pathfinding, cycle detection. BFS explores level by level (breadth-first) using a queue, suitable for shortest paths in unweighted graphs.

## Artificial Intelligence Techniques

### N-Queens Problem (Backtracking and Branch and Bound)

* **State the N-Queens problem. What is the objective?**
    The N-Queens problem is to place N chess queens on an N×N chessboard such that no two queens threaten each other. The objective is to find such a placement.
* **Explain the concept of backtracking and how it is applied to solve the N-Queens problem.**
    Backtracking involves trying to place queens one by one in columns. If a placement leads to a state where no more queens can be placed safely, the algorithm "backtracks" by removing the last placed queen and trying the next valid position.
* **What are the constraints that need to be satisfied when placing queens on the chessboard?**
    No two queens can be in the same row, same column, or on the same diagonal.
* **How do you check if a queen can be placed safely in a particular cell [row, column]?**
    Check if there's any other queen in the same row, same column, or along both diagonals passing through that cell.
* **What is the state-space tree for the N-Queens problem?**
    The state-space tree represents all possible placements of queens, where each level might correspond to a queen or a column, and branches represent choices for placing a queen.
* **Explain the "bounding" part of the Branch and Bound technique in the context of the N-Queens problem. How does it differ from simple backtracking?**
    In N-Queens, the "bounding" is implicit in backtracking: if a partial solution cannot lead to a valid complete solution (e.g., a queen placement is unsafe), that branch of the search tree is pruned. Branch and Bound often involves an explicit cost/bound function to prune sub-optimal paths, which is less direct here but the principle of pruning unpromising branches is similar.
* **What kind of data structures would you use to represent the chessboard and the positions of the queens?**
    A 2D array can represent the chessboard, or more efficiently, a 1D array where the index represents the column and the value represents the row of the queen. Additional arrays/sets can track occupied rows, diagonals.
* **What is the worst-case time complexity for solving the N-Queens problem using backtracking?**
    The worst-case is roughly $O(N!)$ because, in the worst case, it might explore a large portion of the N permutations for placing queens.
* **Are there values of N for which no solution exists? If so, which ones?**
    Yes, for N=2 and N=3, no solution exists.
* **How many possible solutions exist for the 8-Queens problem?**
    There are 92 possible solutions for the 8-Queens problem.
* **In how many directions can a queen attack other pieces on a chessboard?**
    A queen can attack in 8 directions: horizontally (left, right), vertically (up, down), and diagonally (all four diagonal directions).

### A\* Algorithm (8 Puzzle Problem)

* **What type of search algorithm is A\*? (e.g., uninformed, informed)**
    A\* is an informed search algorithm, also called a best-first search, because it uses problem-specific knowledge (heuristics).
* **What is a heuristic function, and what role does it play in the A\* algorithm?**
    A heuristic function $h(n)$ estimates the cost from the current state 'n' to the goal state. It guides A\* towards the most promising paths.
* **Explain the evaluation function $f(n) = g(n) + h(n)$ used in A\*. What do $g(n)$ and $h(n)$ represent?**
    $f(n)$ is the estimated total cost of the path through node 'n' to the goal. $g(n)$ is the actual cost from the start node to node 'n', and $h(n)$ is the estimated cost from 'n' to the goal.
* **What does it mean for a heuristic to be "admissible"? Why is admissibility important for A\*?**
    An admissible heuristic never overestimates the actual cost to reach the goal. Admissibility (along with consistency for graph search) is crucial for A\* to guarantee finding an optimal solution.
* **What does it mean for a heuristic to be "consistent" (or monotonic)? How does it relate to admissibility?**
    A heuristic is consistent if for every node n and every successor n' of n, $h(n) \le cost(n, n') + h(n')$. A consistent heuristic is always admissible.
* **Is A\* guaranteed to find the optimal solution? If so, under what conditions?**
    Yes, A\* is guaranteed to find an optimal solution if the heuristic function $h(n)$ is admissible (and consistent for graph search).
* **Is A\* a complete algorithm?**
    Yes, A\* is complete, meaning it will find a solution if one exists, unless there are infinitely many nodes with $f \le f(Goal)$.
* **What are the time and space complexity of the A\* algorithm?**
    In the worst case, time and space complexity can be exponential, $O(b^d)$, where b is the branching factor and d is the depth of the solution. It keeps all generated nodes in memory.
* **Describe a common heuristic function used for the 8-puzzle problem (e.g., number of misplaced tiles, Manhattan distance). Which is generally better and why?**
    Common heuristics are the number of misplaced tiles or the Manhattan distance (sum of the horizontal and vertical distances of each tile from its goal position). Manhattan distance is generally better (more informed) as it usually provides a closer estimate to the actual cost.
* **How does A\* manage its open and closed lists (or frontier and explored sets)?**
    The open list (frontier) contains nodes that have been generated but not yet expanded, typically sorted by $f(n)$. The closed list (explored set) contains nodes that have already been expanded.
* **Compare A\* with Greedy Best-First Search.**
    A\* uses $f(n) = g(n) + h(n)$, aiming for optimality by considering cost from start ($g(n)$) and estimate to goal ($h(n)$). Greedy Best-First Search only uses $h(n)$, aiming for a quick solution which may not be optimal.
* **What are the advantages and disadvantages of using heuristic search?**
    Advantages: Can find solutions much more efficiently than uninformed searches by guiding the search. Disadvantages: The effectiveness heavily depends on the quality of the heuristic; a poor heuristic might not improve performance much or could even mislead. Heuristics might not always find the best solution if not admissible (for A\*).

### Expert System

* **What is an expert system? What is its primary purpose?**
    An expert system is a computer program using AI to simulate the judgment and behavior of a human expert in a particular field. Its purpose is often to complement human experts.
* **What are the main components of an expert system? Explain each briefly (Knowledge Base, Inference Engine, User Interface).**
    1.  Knowledge Base: Stores facts and rules about a specific domain.
    2.  Inference Engine: Applies the knowledge from the knowledge base to solve problems using reasoning methods.
    3.  User Interface: Allows end-users to interact with the system to get answers.
* **What is a "knowledge base" in an expert system? How is knowledge typically represented?**
    The knowledge base is where the information (facts, rules, procedures) the expert system draws upon is stored. Knowledge can be represented using if-then rules, frames, semantic nets, or symbolic patterns.
* **What is an "inference engine"? What are the common reasoning methods it uses (e.g., forward chaining, backward chaining)?**
    The inference engine processes information from the knowledge base to solve a problem, often using rules. Common methods are forward chaining (data-driven) and backward chaining (goal-driven).
* **Explain forward chaining with an example.**
    Forward chaining starts with known facts and applies rules to deduce new facts, continuing until a goal is reached or no more rules can be applied. Ex: Predicting stock market movement based on current economic indicators.
* **Explain backward chaining with an example.**
    Backward chaining starts with a hypothesis (goal) and works backward, looking for rules and facts that support the hypothesis. Ex: Medical diagnosis based on a set of symptoms.
* **What is "knowledge engineering"?**
    Knowledge engineering is the process of building and maintaining an expert system, including acquiring knowledge from experts and representing it in the system.
* **What are the advantages of using expert systems?**
    Advantages include accuracy (less prone to human error), permanence of knowledge, logical deduction capability, cost control, and ability to consolidate knowledge from multiple experts.
* **What are the limitations or challenges of expert systems?**
    Limitations include linear thinking (lack of true problem-solving ability beyond programmed rules), lack of intuition or common sense, lack of emotion, and being only as good as their knowledge base (vulnerable to inaccuracies).
* **Can you name some application areas of expert systems?**
    Financial services (asset management, predictions), mechanical engineering (troubleshooting), healthcare (medical diagnosis), and customer service.
* **How does an expert system improve its performance over time?**
    Modern expert systems can use machine learning to improve performance over time by learning from new data and experiences, similar to how humans do. The knowledge base can also be expanded.
* **What role does an "explanation module" play in an expert system?**
    An explanation module shows users how the system arrived at its conclusion or recommendation, increasing transparency and trust.

### Chatbot

* **What is a chatbot? What is its main function?**
    A chatbot is a computer program designed to simulate human conversation through text or voice, often for customer service or information retrieval.
* **What are the underlying technologies that power chatbots, especially AI-based ones?**
    AI-based chatbots are powered by technologies like Natural Language Processing (NLP), Machine Learning (ML), and audio analysis.
* **What is Natural Language Processing (NLP) and how is it relevant to chatbots?**
    NLP is a field of AI that enables computers to understand, interpret, and generate human language. It's crucial for chatbots to process user input and generate appropriate responses.
* **What are the different types of chatbots? (e.g., rule-based, AI/Machine Learning-based). Explain the differences.**
    Rule-based chatbots follow predefined scripts and rules. AI/ML-based chatbots use machine learning to understand context, learn from interactions, and handle more complex conversations.
* **How do rule-based chatbots function? What are their limitations?**
    Rule-based chatbots respond to specific keywords or command patterns based on programmed rules. They are limited to predefined scenarios and cannot handle complex or unanticipated queries effectively.
* **How do Machine Learning-based chatbots work? How do they improve over time?**
    ML-based chatbots use algorithms to understand user intent, process language more flexibly, and learn from past conversations to become more intelligent and handle diverse queries.
* **What are the key steps involved in designing and developing a chatbot?**
    Steps include: 1. Identify goals and needs. 2. Choose a builder/platform. 3. Design conversation flow. 4. Test and collect data. 5. Train and refine based on feedback.
* **What are some common use cases or applications for chatbots?**
    Common use cases include customer service (resolving queries), information provision, lead generation, and automating tasks in CRM systems.
* **What are the benefits of using chatbots for businesses or customer interaction?**
    Benefits include 24/7 customer service, cost savings, time savings, improved efficiency, and consistent responses.
* **What are some challenges in developing effective chatbots?**
    Challenges include handling complex or ambiguous queries, understanding user sentiment, maintaining context over long conversations, and ensuring natural, human-like interaction.
* **How do you evaluate the performance or accuracy of a chatbot?**
    Performance can be evaluated based on metrics like resolution rate, user satisfaction, task completion rate, accuracy of responses, and escalation rate to human agents.
* **Why is Python often used for chatbot development?**
    Python is popular for chatbot development due to its extensive libraries for AI and NLP (like NLTK, SpaCy), readability, large community support, and ease of integration.

## Salesforce Development

### Salesforce Apex Programming

* **What is Apex in Salesforce? What is its primary purpose?**
    Apex is a strongly typed, object-oriented programming language developed by Salesforce. Its primary purpose is to allow developers to add business logic to system events and build third-party SaaS applications on the Salesforce platform.
* **What are the key features of the Apex programming language?**
    Key features include being case-insensitive, supporting DML operations, using SOQL and SOSL for queries, ability to create unit tests, and executing in a multi-tenant environment with governor limits.
* **Is Apex case-sensitive or case-insensitive?**
    Apex is a case-insensitive language.
* **What are DML operations in Apex? Can you give some examples?**
    DML (Data Manipulation Language) operations are used to manipulate sObject records. Examples include INSERT, UPDATE, UPSERT, and DELETE.
* **How do you query data in Apex? (Mention SOQL and SOSL).**
    Data is queried in Apex using SOQL (Salesforce Object Query Language) for retrieving records from a single object or related objects, and SOSL (Salesforce Object Search Language) for text-based searches across multiple objects.
* **What are Governor Limits in Salesforce Apex? Why are they important? What happens if they are exceeded?**
    Governor Limits are runtime limits enforced by Salesforce to ensure that Apex code does not monopolize shared resources in the multi-tenant environment. If a limit is exceeded, the transaction typically fails, and an error is thrown to prevent impact on other users.
* **When should a developer choose to write Apex code instead of using Salesforce's declarative (point-and-click) tools?**
    Apex should be used when business logic is too complex for declarative tools, such as creating web services, implementing custom validation beyond standard rules, or complex DML logic.
* **Can Salesforce objects be used as data types in Apex? Give an example.**
    Yes, Salesforce sObjects can be used as data types. For example, `Account acc = new Account();` where `Account` is a standard Salesforce object.
* **Explain the flow of action when Apex code is executed (from developer saving code to end-user action).**
    When a developer saves Apex code, it's compiled into instructions and saved as metadata. When an end-user event triggers the Apex code, the platform server retrieves these compiled instructions and runs them through the Apex interpreter.
* **How does Apex handle updates with new Salesforce releases?**
    Apex code is automatically upgraded with every Salesforce release, ensuring compatibility with new platform versions.
* **What is the role of unit tests in Apex development?**
    Unit tests in Apex are crucial for verifying code functionality, ensuring code coverage (Salesforce requires at least 75% for deployment), and enabling automated testing and regression prevention.
* **How can Apex be used to create web services?**
    Apex can be used to create web services that integrate Salesforce with other applications by exposing Apex methods as REST or SOAP APIs.

### Salesforce Custom Application

* **What is the primary function of a Salesforce app?**
    The primary function of a Salesforce app is to manage customer data and provide a user interface to access and interact with records stored in objects.
* **What are the basic components of a Salesforce custom application (e.g., objects, tabs, fields)?**
    Basic components include objects (tables to store data), tabs (to display object data), fields (attributes of objects), and relationships between objects.
* **What is an "object" in Salesforce? How does it relate to a database table?**
    An object in Salesforce is like a table in a database, used to store specific types of information or records. For example, a "Students Data" object stores student records.
* **What are "fields" and "records" in the context of Salesforce objects?**
    Fields are attributes or columns of an object (e.g., Name, Email ID for a Student object). Records are individual instances or rows within an object (e.g., a specific student's details).
* **What are "tabs" in a Salesforce application? How are custom tabs created?**
    Tabs provide users with a way to view and access the records of an object within an app. Custom tabs can be created for custom objects to make them accessible in the UI.
* **Explain the concept of "object relationships" in Salesforce. Why are they important?**
    Object relationships link different objects together, allowing data from one object to be related to data in another. They are important for creating a structured data model and representing real-world connections (e.g., a student belonging to a college).
* **Can you describe different types of object relationships in Salesforce (e.g., Master-Detail, Lookup)?**
    Common types include Master-Detail (tightly coupled parent-child), Lookup (loosely coupled), Self-Relationship (linking an object to itself), and Junction Relationship (many-to-many).
* **What is a Master-Detail relationship? What are its characteristics?**
    A Master-Detail relationship is a parent-child relationship where the master object controls certain behaviors of the detail object, like record deletion (cascade delete) and security. The detail record cannot exist without a master.
* **What is a Lookup relationship? How does it differ from a Master-Detail relationship?**
    A Lookup relationship links two objects but is less restrictive than Master-Detail. Records can exist independently, and security/deletion are not automatically cascaded.
* **What is a Junction Relationship (Many-To-Many)? How is it typically implemented in Salesforce?**
    A Many-To-Many relationship allows multiple records of one object to be related to multiple records of another. It's implemented using a third "junction object" that has two master-detail relationships with the two objects being linked.
* **What are Salesforce Profiles, and what role do they play in application access and visibility?**
    Salesforce Profiles control what users can see and do within the Salesforce application, including object permissions, field-level security, tab visibility, and app access.
* **Briefly describe the steps to create a custom application in Salesforce.**
    Steps generally involve defining custom objects, creating custom fields for those objects, establishing relationships between objects, creating tabs for objects, and then assembling these into a custom app with a specific navigation and visibility for users.
