import streamlit as st

st.set_page_config(page_title="C++ STL vs Java Collections CheatSheet For DSA", layout="wide")

# Custom CSS for styling
st.markdown("""
<style>
    .main {background-color: #0E1117; color: white;}
    .code-container {
        background-color: #000000;
        padding: 20px;
        border-radius: 10px;
        margin: 15px 0;
        font-family: 'Courier New', monospace;
    }
    .header {color: #4CAF50; border-bottom: 2px solid #4CAF50;}
    .stExpander > div {background-color: #1a1a1a !important;}
</style>
""", unsafe_allow_html=True)

data = [
    {
        "title": "Arrays",
        "cpp": """#include <iostream>
using namespace std;

int main() {
    // Static array initialization
    int cppArr[5] = {1,2,3,4,5};
    
    // Access/modify elements
    cppArr[2] = 10;
    
    cout << "C++ Array: ";
    for(int i=0; i<5; i++) {
        cout << cppArr[i] << " ";
    }
    return 0;
}""",
        "java": """public class Main {
    public static void main(String[] args) {
        // Array declaration & initialization
        int[] javaArr = {1,2,3,4,5};
        
        // Access/modify elements
        javaArr[2] = 10;
        
        System.out.print("Java Array: ");
        for(int num : javaArr) {
            System.out.print(num + " ");
        }
    }
}""",
        "differences": [
            "C++ arrays are low-level constructs with fixed size",
            "Java arrays are objects with length property",
            "C++ allows stack allocation, Java arrays are always heap objects",
            "Java performs bounds checking, C++ does not"
        ]
    },
    {
    "title": "Vectors (C++) vs ArrayList (Java)",
    "cpp": """#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> vec;
    
    // Add elements
    vec.push_back(10);
    vec.push_back(20);
    vec.push_back(30);
    
    // Access elements
    cout << "Element at 1: " << vec[1] << endl;
    
    // Iterate
    cout << "Vector elements: ";
    for(int num : vec) {
        cout << num << " ";
    }
    
    // Capacity operations
    vec.reserve(100);
    vec.shrink_to_fit();
    return 0;
}""",
    "java": """import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<Integer> list = new ArrayList<>();
        
        list.add(10);
        list.add(20);
        list.add(30);
        
        System.out.println("Element at 1: " + list.get(1));
        
        System.out.print("ArrayList elements: ");
        for(int num : list) {
            System.out.print(num + " ");
        }
        
        list.ensureCapacity(100);
        list.trimToSize();
    }
}""",
    "differences": [
        "C++ vectors store elements in contiguous memory",
        "Java ArrayLists store object references",
        "C++ vectors can contain primitives directly",
        "Java requires boxing/unboxing for primitives",
        "Growth strategy: C++ doubles capacity vs Java +50%",
        "C++ has vector<bool> specialization",
        "Java provides List interface methods"
    ]
},
    {
        "title": "HashSets/HashTables",
        "cpp": """#include <iostream>
#include <unordered_set>
using namespace std;

int main() {
    unordered_set<string> cppSet;
    
    // Insert elements
    cppSet.insert("Apple");
    cppSet.insert("Banana");
    
    // Check existence
    if(cppSet.find("Apple") != cppSet.end()) {
        cout << "Apple found!" << endl;
    }
    return 0;
}""",
        "java": """import java.util.HashSet;

public class Main {
    public static void main(String[] args) {
        HashSet<String> javaSet = new HashSet<>();
        
        javaSet.add("Apple");
        javaSet.add("Banana");
        
        if(javaSet.contains("Apple")) {
            System.out.println("Apple found!");
        }
    }
}""",
        "differences": [
            "C++ uses unordered_set, Java uses HashSet",
            "Java HashSet is synchronized in legacy classes",
            "C++ provides bucket interface for low-level control",
            "Java handles null values, C++ requires valid hashes"
        ]
    },
    
    {
        "title": "LinkedLists",
        "cpp": """#include <iostream>
#include <list>
using namespace std;

int main() {
    list<int> cppList;
    
    // Add elements
    cppList.push_back(10);
    cppList.push_front(5);
    
    // Iterate using iterators
    cout << "C++ List: ";
    for(auto it = cppList.begin(); it != cppList.end(); ++it) {
        cout << *it << " ";
    }
    return 0;
}""",
        "java": """import java.util.LinkedList;

public class Main {
    public static void main(String[] args) {
        LinkedList<Integer> javaList = new LinkedList<>();
        
        javaList.addLast(10);
        javaList.addFirst(5);
        
        System.out.print("Java List: ");
        for(Integer num : javaList) {
            System.out.print(num + " ");
        }
    }
}""",
        "differences": [
            "C++ uses std::list (doubly linked list)",
            "Java LinkedList implements Deque interface",
            "C++ provides constant time size() in C++11+",
            "Java maintains size as instance variable"
        ]
    },
    {
        "title": "Stacks",
        "cpp": """#include <iostream>
#include <stack>
using namespace std;

int main() {
    stack<int> s;
    s.push(10);
    s.push(20);
    
    cout << "Top: " << s.top() << endl;
    s.pop();
    cout << "Size: " << s.size() << endl;
    return 0;
}""",
        "java": """import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        Stack<Integer> stack = new Stack<>();
        stack.push(10);
        stack.push(20);
        
        System.out.println("Top: " + stack.peek());
        stack.pop();
        System.out.println("Size: " + stack.size());
    }
}""",
        "differences": [
            "C++ uses std::stack (adaptor container)",
            "Java Stack extends Vector (considered legacy)",
            "C++ top() vs Java peek()",
            "Java Stack is synchronized while C++ is not"
        ]
    },
    {
        "title": "Queues",
        "cpp": """#include <iostream>
#include <queue>
using namespace std;

int main() {
    queue<int> q;
    q.push(10);
    q.push(20);
    
    cout << "Front: " << q.front() << endl;
    q.pop();
    cout << "Empty? " << (q.empty() ? "Yes" : "No") << endl;
    return 0;
}""",
        "java": """import java.util.LinkedList;
import java.util.Queue;

public class Main {
    public static void main(String[] args) {
        Queue<Integer> q = new LinkedList<>();
        q.add(10);
        q.offer(20);
        
        System.out.println("Front: " + q.peek());
        q.remove();
        System.out.println("Empty? " + q.isEmpty());
    }
}""",
        "differences": [
            "C++ uses std::queue (adaptor container)",
            "Java Queue is interface with LinkedList implementation",
            "C++ front() vs Java peek()",
            "Java has add()/offer() distinction for capacity"
        ]
    },
    {
        "title": "Deque",
        "cpp": """#include <iostream>
#include <deque>
using namespace std;

int main() {
    deque<int> dq;
    dq.push_front(10);
    dq.push_back(20);
    
    cout << "Front: " << dq.front() 
         << " Back: " << dq.back() << endl;
    return 0;
}""",
        "java": """import java.util.ArrayDeque;

public class Main {
    public static void main(String[] args) {
        ArrayDeque<Integer> dq = new ArrayDeque<>();
        dq.addFirst(10);
        dq.addLast(20);
        
        System.out.println("Front: " + dq.getFirst() 
            + " Back: " + dq.getLast());
    }
}""",
        "differences": [
            "C++ deque allows random access",
            "Java ArrayDeque has no null elements",
            "C++ uses push_front/pop_front",
            "Java uses addFirst/removeFirst"
        ]
    },
    {
        "title": "Trees",
        "cpp": """#include <iostream>
using namespace std;

struct Node {
    int data;
    Node *left, *right;
    Node(int val) : data(val), left(nullptr), right(nullptr) {}
};

void preorder(Node* root) {
    if(!root) return;
    cout << root->data << " ";
    preorder(root->left);
    preorder(root->right);
}

int main() {
    Node* root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(3);
    preorder(root);
    return 0;
}""",
        "java": """class Node {
    int data;
    Node left, right;
    Node(int val) { data = val; }
}

public class Main {
    static void preorder(Node root) {
        if(root == null) return;
        System.out.print(root.data + " ");
        preorder(root.left);
        preorder(root.right);
    }
    
    public static void main(String[] args) {
        Node root = new Node(1);
        root.left = new Node(2);
        root.right = new Node(3);
        preorder(root);
    }
}""",
        "differences": [
            "C++ uses pointers, Java uses references",
            "Memory management (manual vs GC)",
            "Null handling (nullptr vs null)",
            "Java needs class definition in same file"
        ]
    },
    {
        "title": "Heaps",
        "cpp": """#include <iostream>
#include <queue>
using namespace std;

int main() {
    // Max-heap
    priority_queue<int> maxHeap;
    maxHeap.push(3);
    maxHeap.push(1);
    maxHeap.push(4);
    
    cout << "Top: " << maxHeap.top() << endl;
    
    // Min-heap
    priority_queue<int, vector<int>, greater<>> minHeap;
    minHeap.push(3);
    minHeap.push(1);
    minHeap.push(4);
    
    cout << "Top: " << minHeap.top() << endl;
    return 0;
}""",
        "java": """import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) {
        // Min-heap (default)
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        minHeap.add(3);
        minHeap.add(1);
        minHeap.add(4);
        System.out.println("Top: " + minHeap.peek());
        
        // Max-heap
        PriorityQueue<Integer> maxHeap = 
            new PriorityQueue<>((a, b) -> b - a);
        maxHeap.add(3);
        maxHeap.add(1);
        maxHeap.add(4);
        System.out.println("Top: " + maxHeap.peek());
    }
}""",
        "differences": [
            "C++: Default max-heap, Java: Default min-heap",
            "Java uses Comparator for ordering",
            "C++ needs explicit container and comparator",
            "Java PriorityQueue is unbounded"
        ]
    },
    {
        "title": "Graphs",
        "cpp": """#include <iostream>
#include <vector>
using namespace std;

int main() {
    // Adjacency list
    vector<vector<int>> graph = {
        {1, 2},
        {0, 2},
        {0, 1}
    };
    
    // BFS
    vector<bool> visited(3, false);
    queue<int> q;
    q.push(0);
    visited[0] = true;
    
    while(!q.empty()) {
        int node = q.front();
        q.pop();
        cout << node << " ";
        for(int neighbor : graph[node]) {
            if(!visited[neighbor]) {
                visited[neighbor] = true;
                q.push(neighbor);
            }
        }
    }
    return 0;
}""",
        "java": """import java.util.*;

public class Main {
    public static void main(String[] args) {
        List<List<Integer>> graph = new ArrayList<>();
        graph.add(Arrays.asList(1, 2));
        graph.add(Arrays.asList(0, 2));
        graph.add(Arrays.asList(0, 1));
        
        boolean[] visited = new boolean[3];
        Queue<Integer> q = new LinkedList<>();
        q.add(0);
        visited[0] = true;
        
        while(!q.isEmpty()) {
            int node = q.remove();
            System.out.print(node + " ");
            for(int neighbor : graph.get(node)) {
                if(!visited[neighbor]) {
                    visited[neighbor] = true;
                    q.add(neighbor);
                }
            }
        }
    }
}""",
        "differences": [
            "C++ uses vector of vectors",
            "Java uses List of Lists",
            "Queue implementations differ",
            "Memory management approaches"
        ]
    },
    {
        "title": "Tries",
        "cpp": """#include <iostream>
using namespace std;

struct TrieNode {
    bool isEnd;
    TrieNode* children[26];
    TrieNode() : isEnd(false) {
        fill_n(children, 26, nullptr);
    }
};

void insert(TrieNode* root, string word) {
    for(char c : word) {
        int idx = c - 'a';
        if(!root->children[idx])
            root->children[idx] = new TrieNode();
        root = root->children[idx];
    }
    root->isEnd = true;
}

int main() {
    TrieNode* root = new TrieNode();
    insert(root, "apple");
    return 0;
}""",
        "java": """class TrieNode {
    boolean isEnd;
    TrieNode[] children;
    TrieNode() {
        isEnd = false;
        children = new TrieNode[26];
    }
}

public class Main {
    static void insert(TrieNode root, String word) {
        for(char c : word.toCharArray()) {
            int idx = c - 'a';
            if(root.children[idx] == null)
                root.children[idx] = new TrieNode();
            root = root.children[idx];
        }
        root.isEnd = true;
    }
    
    public static void main(String[] args) {
        TrieNode root = new TrieNode();
        insert(root, "apple");
    }
}""",
        "differences": [
            "C++ uses pointers, Java uses references",
            "Memory management approaches",
            "Null handling differences",
            "Java needs explicit array initialization"
        ]
    },
    {
        "title": "Bit Manipulation",
        "cpp": """#include <iostream>
using namespace std;

int main() {
    int num = 5; // 0101
    // Set 3rd bit
    num |= (1 << 2);
    // Clear 1st bit
    num &= ~(1 << 0);
    // Toggle 2nd bit
    num ^= (1 << 1);
    
    cout << "Result: " << num << endl; // 0110 = 6
    return 0;
}""",
        "java": """public class Main {
    public static void main(String[] args) {
        int num = 5; // 0101
        // Set 3rd bit
        num |= (1 << 2);
        // Clear 1st bit
        num &= ~(1 << 0);
        // Toggle 2nd bit
        num ^= (1 << 1);
        
        System.out.println("Result: " + num); // 0110 = 6
    }
}""",
        "differences": [
            "Syntax identical for basic operations",
            "C++ has bitset container",
            "Java uses signed integers for bit operations",
            "Different handling of unsigned operations"
        ]
    }
]

def main():
    st.title("C++/Java Collections Comparison Guide")
    st.markdown("---")
    
    for item in data:
        with st.container():
            st.markdown(f"### {item['title']}")
            
            # Code Columns
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**C++ Implementation**")
                st.markdown(f"```cpp\n{item['cpp']}\n```", unsafe_allow_html=True)
            
            with col2:
                st.markdown("**Java Implementation**")
                st.markdown(f"```java\n{item['java']}\n```", unsafe_allow_html=True)
            
            # Differences expander
            with st.expander("📚 Key Differences Explanation"):
                for diff in item["differences"]:
                    st.markdown(f"- {diff}")
            
            st.markdown("---")
    
    st.markdown('Created by <a href="https://www.linkedin.com/in/programming-vikrant/" target="_blank" style="color: #4CAF50; text-decoration: none;">Vikrant</a>', 
            unsafe_allow_html=True)

if __name__ == "__main__":
    main()