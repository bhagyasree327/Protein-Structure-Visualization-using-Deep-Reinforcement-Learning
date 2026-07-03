import matplotlib.pyplot as plt

def visualize(coords):

    x=coords[:,0]
    y=coords[:,1]
    z=coords[:,2]

    fig=plt.figure()

    ax=fig.add_subplot(111,projection="3d")

    ax.scatter(x,y,z)

    ax.set_title("Predicted Protein Structure")

    plt.show()