#include <bits/stdc++.h>
using namespace std;

// https://en.cppreference.com/w/cpp/container/list

struct Node {
    int value;
    Node *prev = nullptr;
    Node *next = nullptr;

    Node(int value) : value(value) {}
};

struct LinkedList {
    Node *head = nullptr;
    Node *tail = nullptr; // To push_back fast

    LinkedList &push_back(int value) {
        if (!head) {
            head = tail = new Node(value);
            return *this;
        }

        tail->next = new Node(value);
        tail->next->prev = tail;
        tail = tail->next;

        return *this; // To allow chain operations
    }

    LinkedList &push_front(int value) {
        if (!head) {
            head = tail = new Node(value);
            return *this;
        }

        head->prev = new Node(value);
        head->prev->next = head;
        head = head->prev;

        return *this;
    }

    LinkedList &pop_back() {
        if (!head) {
            cout << "Cannot pop from empty list\n";
            return *this;
        }

        // I've first tried these 3 faulty lines!
        // tail = tail->prev;
        // delete tail->next;
        // tail->next = nullptr;

        Node *tmp = tail;
        tail = tail->prev;
        delete tmp;

        if (tail)
            tail->next = nullptr;
        else
            head = nullptr;

        return *this;
    }

    LinkedList &pop_front() {
        if (!head) {
            cout << "Cannot pop from empty list\n";
            return *this;
        }

        // I've first tried these 3 faulty lines!
        // head = head->next;
        // delete head->prev;
        // head->prev = nullptr;

        Node *tmp = head;
        head = head->next;
        delete tmp;

        if (head)
            head->prev = nullptr;
        else
            tail = nullptr;

        return *this;
    }

    friend ostream &operator<<(ostream &o, const LinkedList &l) {
        if (!l.head) {
            o << "(empty)" << "\n";
            return o;
        }

        Node *cur = l.head;
        while (cur) {
            o << cur->value;
            cur = cur->next;
            o << " \n"[!cur];
        }

        return o;
    }

    ~LinkedList() {
        while (head) {
            Node *tmp = head;
            head = head->next;
            delete tmp;
        }
    }
};

int main() {
    // Eliniz alışsın :))
    ios::sync_with_stdio(0);
    cin.tie(0);

    LinkedList l;

    while (1) {
        string op;
        cin >> op;

        if (op == "push_back") {
            int value;
            cin >> value;
            l.push_back(value);
        } else if (op == "push_front") {
            int value;
            cin >> value;
            l.push_front(value);
        } else if (op == "pop_back") {
            l.pop_back();
        } else if (op == "pop_front") {
            l.pop_front();
        } else if (op == "print") {
            cout << l; // This uses "\n", not endl, thus doesn't flush
            // cout.flush(); // To see the list immediately
        } else {
            cout << "Oops, invalid command!\n";
        }
    }
}