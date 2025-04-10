"""
HOW TO RUN
- Create virtual environment
    python3 -m venv venv
- Activate it
    source venv/bin/activate
- install packages 
    pip install networkx matplotlib
- Run python or python3 dfa.py
"""
import networkx as nx
import matplotlib.pyplot as plt

class DFA:
    def __init__(self, pattern):
        self.pattern = pattern #this gonna be the substring
        #define the states, one for each prefix of the pattern + initial state
        #so like q0= empty prefix, q1= symbol one, ... qn= full thing
        self.states = list(range(len(pattern) + 1))
        self.alphabet = set()
        self.transition = {} # to transition states in dfa 
        self.start_state = 0 # to make sure dfa always syatys at state q0
        self.accept_states = {len(pattern)} #only if substring in string is there a match

    def build_transition_function(self):
        # dfa implimintation 
        #Builds sigma(state, symbol) 
        # from to lecture notes (Section 2.1): Formal definition of sigma 

        for state in self.states:
            for a in self.alphabet:
                prefix = self.pattern[:state] + a # matching the subset, current prefix + new character aka set 
                next_state = 0
                # this is gonna look for the longest subset of the pattern that is a set of this new string
                for i in range(min(len(self.pattern), len(prefix)), 0, -1):
                    if prefix.endswith(self.pattern[:i]):
                        next_state = i
                        break  
                self.transition[(state, a)] = next_state #sertting the dfa transition states

    def process(self, string):
        #constructs the full alphabet from the subset and the input string
        self.alphabet = set(self.pattern + string)
        self.build_transition_function()

        state = self.start_state
        trace = [state]
        #simulate dfa computation as described in lecture notes Section 2.2
        for symbol in string:
            if (state, symbol) not in self.transition:
                state = 0  
            else:
                state = self.transition[(state, symbol)]
            trace.append(state)
            #accept immediately if there is a full match
            if state in self.accept_states:
                return trace, True
        return trace, False


    def show_trace(self, string):
        trace, accepted = self.process(string)
        print("Input:", string)
        print("Trace:", " → ".join(f"q{q}" for q in trace))
        print("Result:", "Accepted" if accepted else "Rejected")

    def draw(self):
        G = nx.DiGraph()
        for (state, symbol), next_state in self.transition.items():
            G.add_edge(f"q{state}", f"q{next_state}", label=symbol)

        pos = nx.spring_layout(G)
        edge_labels = nx.get_edge_attributes(G, 'label')

        plt.figure(figsize=(8, 6))
        nx.draw(G, pos, with_labels=True, node_size=1500, node_color='lightblue')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        start_node = f"q{self.start_state}"
        accept_nodes = [f"q{state}" for state in self.accept_states]
        nx.draw_networkx_nodes(G, pos, nodelist=[start_node], node_color='green')
        nx.draw_networkx_nodes(G, pos, nodelist=accept_nodes, node_color='orange')

        plt.title("DFA State Diagram")
        plt.show()

if __name__ == "__main__":
    print("DFA Substring Matcher\n")
    
    pattern = input("Enter the substring to search for (pattern): ").strip()
    text = input("Enter the string to search within: ").strip()

    if not pattern or not text:
        print("Both pattern and input string must be non-empty.")
    else:
        dfa = DFA(pattern)
        dfa.show_trace(text)
        dfa.draw()
