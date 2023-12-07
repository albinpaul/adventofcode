#include <bits/stdc++.h>
using namespace std;
template<class T>
void show(vector<T> v){
    for(auto e: v){
        cout << e << " ";
    }
    cout << endl;
}
int main(){
    string line;
    vector<pair<string, int>> cards;
    while(getline(cin, line)) {
        bool card = true;
        string temp;
        int num = 0;
        for(char c: line){
            if(c == ' '){
                card = false;
                continue;
            }
            if(card) {
                temp += c;
            } else {
                num = num * 10 + c - '0';
            }
        }
        cards.push_back({temp, num});
    }
    vector<char> CARDS = {'A','K','Q','T','9','8','7','6','5','4','3','2', 'J'};
    reverse(CARDS.begin(), CARDS.end());
    unordered_map <char, int> MAPPINGS;
    for(int i=0; i<CARDS.size(); i++){
        MAPPINGS[CARDS[i]] = i;
    }

    auto getCount = [](string &inp) {
        unordered_map<char, int> counts;
        vector<int> result(6, 0);
        int jCount = 0;
        for(char c: inp){
            if(c == 'J'){
                jCount++;
                continue;
            }
            counts[c]++;
        }

        for(auto [k, v]: counts){
            result[v]++;
        }
        bool done = false;
        for(int i=5; i>=0; i--){
            if(result[i] > 0) {
                result[i]--;
                result[i + jCount]++;
                done = true;
                break;
            }
        }
        if(!done && jCount){
            result[jCount]++;
        }
        reverse(result.begin(), result.end());
        return result;
    };
    sort(cards.begin(), cards.end(), [&](auto &a, auto &b) {
        auto aV = getCount(a.first);
        auto bV = getCount(b.first);
        if(aV != bV){
            for(int i=0; i<6; i++){
                if(aV[i] != bV[i]){
                    return aV[i] < bV[i];
                }
            }
            assert(false);
            return false;
        }
        int len = a.first.size();
        for(int i = 0; i < len; i++){
            if(a.first[i] != b.first[i]){
                return MAPPINGS[a.first[i]] < MAPPINGS[b.first[i]];
            }
        }
        assert(false);
        return false;
    });

    long long ans = 0;
    int id = 1;
    for(auto item: cards){
        show(getCount(item.first));
        cout << item.first << " " << id << " " << item.second << " " << id << endl;
        ans += 1LL * item.second * id;
        assert(ans > 0);
        id++;
    }
    cout << ans << endl;
    return 0;
}