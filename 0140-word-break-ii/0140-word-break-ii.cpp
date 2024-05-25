class Trie {
public:
    Trie* children[26] = {nullptr};
    bool isEnd = false;

    void insert(const string& word) {
        Trie* node = this;
        for (char c : word) {
            int index = c - 'a';
            if (node->children[index] == nullptr) {
                node->children[index] = new Trie();
            }
            node = node->children[index];
        }
        node->isEnd = true;
    }

    bool search(const string& word) {
        Trie* node = this;
        for (char c : word) {
            int index = c - 'a';
            if (node->children[index] == nullptr) {
                return false;
            }
            node = node->children[index];
        }
        return node->isEnd;
    }
};

class Solution {
private:
    Trie trie;
    unordered_map<string, vector<vector<string>>> memo;

    vector<vector<string>> dfs(const string& s) {
        if (memo.find(s) != memo.end()) {
            return memo[s];
        }
        
        vector<vector<string>> res;
        if (s.empty()) {
            res.push_back({});
            return res;
        }

        for (int i = 1; i <= s.size(); ++i) {
            string prefix = s.substr(0, i);
            if (trie.search(prefix)) {
                vector<vector<string>> suffixBreaks = dfs(s.substr(i));
                for (vector<string>& suffix : suffixBreaks) {
                    suffix.insert(suffix.begin(), prefix);
                    res.push_back(suffix);
                }
            }
        }

        memo[s] = res;
        return res;
    }

    string join(const vector<string>& words, const string& delimiter) {
        string result;
        for (size_t i = 0; i < words.size(); ++i) {
            if (i > 0) result += delimiter;
            result += words[i];
        }
        return result;
    }

public:
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        for (const string& word : wordDict) {
            trie.insert(word);
        }

        vector<vector<string>> res = dfs(s);
        vector<string> result;
        for (const vector<string>& words : res) {
            result.push_back(join(words, " "));
        }
        return result;
    }
};