
# coding: utf-8

# ## Lec54 Spatial Segregation : An Introduction
# 
# <img src = "lec54_1.png">
# <img src = "lec54_2.png">
# <img src = "lec54_3.png">
# <img src = "lec54_4.png">
# 
# * unhappy people tend to change their place to a happier destination
# 
# ### Schelling Model
# 
# -> Based on the threshold value
# -> Local changes affect the global behavior
# 
# <img src = "lec54_5.png">

# ## Lec55 Spatial Segregation : Simulation of Schelling Model
# 
# <a href = "http://nifty.stanford.edu/2014/mccown-schelling-model-segregation/"> Simulator </a>

# ## Lec56 Spatial Segregation : Conclusion
# 
# * OBSERVATION : Emerence of Homophily
# * Is homophily/ segregation is inevitable ? - NOT REALLY
# <img src = "lec56_1.png">

# ## Lec57 Schelling Model Implementation : An Introduction
# 
# <img src = "lec57_1.png">
# <img src = "lec57_2.png">
# <img src = "lec57_3.png">
# 

# ## Lec58 Schelling Model Implementation : Base Code

# In[2]:

#Programming Concepts
import networkx as nx
import matplotlib.pyplot as plt
N = 10
G = nx.grid_2d_graph(N, N)
nx.draw(G, with_labels = 1)
plt.show()
print G.nodes()


# In[3]:

pos = dict((n, n) for n in G.nodes())
print pos


# In[4]:

nx.draw(G, pos, with_labels = 1)
plt.show()


# In[5]:

labels = dict(((i, j), i*10 + j) for i,j in G.nodes())
nx.draw(G, pos, with_labels = 1, labels = labels)
plt.show()


# In[6]:

for (u, v) in G.nodes():
    if (u+1 <= N-1) and (v+1 <= N-1):
        G.add_edge((u, v), (u+1, v+1))

nx.draw(G, pos, with_labels = 1)
plt.show()


# In[7]:

for (u, v) in G.nodes():
    if (u+1 <= N-1) and (v-1 >= 0):
        G.add_edge((u, v), (u+1, v-1))

nx.draw(G, pos, with_labels = 1)
plt.show()


# In[8]:

nx.draw(G, pos, labels = labels, with_labels = 1)
plt.show()


# ## Lec59 Schelling Model Implementation : Visualization and getting a list of boundary and intenal nodes

# In[29]:

import networkx as nx
import matplotlib.pyplot as plt
import random as rd

N = 10
G = nx.grid_2d_graph(N, N)
pos = dict((n, n) for n in G.nodes())
labels = dict(((i, j), i*10 + j) for i,j in G.nodes())

def display_graph(G):
    nodes_g = nx.draw_networkx_nodes(G, pos, node_color = 'green', nodelist = type1_nodes)
    nodes_r = nx.draw_networkx_nodes(G, pos, node_color = 'red', nodelist = type2_nodes)
    nodes_w = nx.draw_networkx_nodes(G, pos, node_color = 'white', nodelist = empty_cells)
    
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos, labels = labels)
    plt.show()
    

#Add diagonal edges
for (u, v) in G.nodes():
    if (u+1 <= N-1) and (v+1 <= N-1):
        G.add_edge((u, v), (u+1, v+1))

for (u, v) in G.nodes():
    if (u+1 <= N-1) and (v-1 >= 0):
        G.add_edge((u, v), (u+1, v-1))

nx.draw(G, pos, labels = labels, with_labels = 1)
plt.show()

for n in G.nodes():
    G.node[n]['type'] = rd.randint(0, 2)
    
type1_nodes = [n for (n, d) in G.nodes(data = True) if d['type'] == 1]
type2_nodes = [n for (n, d) in G.nodes(data = True) if d['type'] == 2]
empty_cells = [n for (n, d) in G.nodes(data = True) if d['type'] == 0]

#print type1_nodes
#print type2_nodes
#print empty_cells

display_graph(G)


# In[15]:

def display_graph(G):
    nodes_g = nx.draw_networkx_nodes(G, pos, node_color = 'green', nodelist = type1_nodes)
    nodes_r = nx.draw_networkx_nodes(G, pos, node_color = 'red', nodelist = type2_nodes)
    nodes_w = nx.draw_networkx_nodes(G, pos, node_color = 'white', nodelist = empty_cells)
    
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos, labels = labels)
    plt.show()
    


# In[25]:

def get_boundary_nodes():
    boundary_nodes_list = []
    for u, v in G.nodes():
        if u == 0 or v == 0 or v == N-1 or u == N-1:
            boundary_nodes_list.append((u, v))
            #print  (u, v), " appended"
    return boundary_nodes_list

boundary_nodes = get_boundary_nodes()
internal_nodes = list(set(G.nodes()) - set(boundary_nodes))

print boundary_nodes
print internal_nodes

