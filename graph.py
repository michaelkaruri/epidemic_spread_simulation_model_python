
# importing the required module
import matplotlib.pyplot as plt



class Graph:
    def __init__(self, contegoius_people_list):
        self.contegoius_people_list=contegoius_people_list
        number_of_days=0
        self.days_list=[]
        for i in range(0,len(self.contegoius_people_list)):
            self.days_list.append(i)


    def draw(self):
        # x axis values
        
        x = self.days_list
        # corresponding y axis values
        y = self.contegoius_people_list

        # plotting the points
        plt.plot(x, y)

        # naming the x axis
        plt.xlabel('Days')
        # naming the y axis
        plt.ylabel('Number of contagious people')

        # giving a title to my graph
        plt.title('Simulation of a pandemic')

        # function to show the plot
        plt.show()