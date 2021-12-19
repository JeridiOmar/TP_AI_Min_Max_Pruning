from Game import Game
import time
import pandas as pd
import matplotlib.pyplot as plt

def plot_algorithms_execution_results(minmax_result, pruning_result):
    comp_list = [[minmax_result[i], pruning_result[i]] for i in range(len(minmax_result))]
    comp_df = pd.DataFrame(comp_list, columns=['minmax', 'pruning'])
    comp_df['number_of_essay'] = comp_df.index

    fig, ax = plt.subplots(figsize=[9, 7])
    ax.plot(comp_df['number_of_essay'], comp_df['minmax'], label="Min Max Execution Time",
            marker='o', linewidth=2
            )
    ax.plot(comp_df['number_of_essay'], comp_df['pruning'], label="Min Max alpha beta pruning Execution Time",
            marker='o', linewidth=2
            )
    ax.set_xlabel('Numbers of chips in stack')
    ax.set_ylabel('Execution Time ')
    plt.title('Comparison Between Min-Max and Alpha-Beta Algorithms Execution Time')
    plt.legend()
    plt.savefig('./algo_comp_time.png')
    plt.show()
def plot_algorithms_visited_nodes_results(minmax_result, pruning_result):
    comp_list = [[minmax_result[i], pruning_result[i]] for i in range(len(minmax_result))]
    comp_df = pd.DataFrame(comp_list, columns=['minmax', 'pruning'])
    comp_df['number_of_essay'] = comp_df.index

    fig, ax = plt.subplots(figsize=[9, 7])
    ax.plot(comp_df['number_of_essay'], comp_df['minmax'], label="Min Max visited nodes",
            marker='o', linewidth=2
            )
    ax.plot(comp_df['number_of_essay'], comp_df['pruning'], label="Min Max alpha beta pruning visited nodes",
            marker='o', linewidth=2
            )
    ax.set_xlabel('Numbers of chips in stack')
    ax.set_ylabel('Visited nodes')
    plt.title('Comparison Between Min-Max and Alpha-Beta Algorithms Visited Nodes')
    plt.legend()
    plt.savefig('./heuristics_comp_visited_nodes.png')
    plt.show()
def compare_algorithms(n):
    minmax_time = []
    pruning_time = []
    for i in range(1, n):
        g = Game(i)
        start = time.time()
        g.play_simulation(True)
        end = time.time()
        pruning_time.append(end - start)
        g = Game(i)
        start1 = time.time()
        g.play_simulation(False)
        end1 = time.time()
        minmax_time.append(end1 - start1)
        print('Simulation time: {}s'.format(round(end - start, 10)))
    plot_algorithms_execution_results(minmax_time, pruning_time)

def compare_algorithms_visited_nodes(n):
    minmax_exec = []
    pruning_exec = []
    for i in range(1, n):
        g = Game(i)
        visited=g.max_visited_nodes(True)
        minmax_exec.append(visited)
        g = Game(i)
        visited1=g.max_visited_nodes(False)
        pruning_exec.append(visited1)
    plot_algorithms_visited_nodes_results(minmax_exec, pruning_exec)
if __name__ == '__main__':
    chips = int(input('insert initial chips number'))
    g=Game(chips)
    g.play()
    ###########Pour une partie avec elagage#############
    # chips = int(input('insert initial chips number'))
    # g=Game(chips)
    # g.play_with_pruning()
    ####################################################
    ###########Pour une Simulation noeuds visite#############
    # compare_algorithms_visited_nodes(15)
    ####################################################
    ###########Pour une Simulation Temps execution#############
    # compare_algorithms(15)
    ####################################################
