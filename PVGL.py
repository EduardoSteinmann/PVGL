import matplotlib.pyplot as plt

data_file: str = input("Enter in the file to read the data from. The data must be ordered int the following format: 'P I D Error' : ")

time: list[int] = []
P_graph: list[float] = []
I_graph: list[float] = []
D_graph: list[float] = []
error_graph: list[float] = []

def read_data() -> None:
    global i
    file = open(data_file, 'r')

    count: int = 0

    while True:
        count += 1

        line: str = file.readline()

        data = line.split()

        if not line: 
            break

        P_graph.append(float(data[0]))
        I_graph.append(float(data[1]))
        D_graph.append(float(data[2]))
        error_graph.append(float(data[3]))

        time.append(count)


def plot_info() -> None:
    plt.plot(time, P_graph, label="P graph")
    plt.plot(time, I_graph, label="I graph")
    plt.plot(time, D_graph, label="D graph")
    plt.plot(time, error_graph, label="Error graph")
    plt.axhline(0, color="black", lw=2)
    plt.title("PID Graph")
    plt.xlabel("Time (Iteration of one PID loop)")
    plt.legend()
    plt.show()

read_data()
plot_info()