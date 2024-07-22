import matplotlib.pyplot as plt
import numpy as np
from config import FIGURE_SIZE

class Visualizer:
    def __init__(self):
        plt.style.use('seaborn-v0_8') 
        self.colors = plt.cm.viridis 

    def create_visualization(self, chart_type, data):
        plt.figure(figsize=FIGURE_SIZE)

        if chart_type == '1':
            self._bar_chart(data)
        elif chart_type == '2':
            self._line_chart(data)
        elif chart_type == '3':
            self._scatter_plot(data)
        elif chart_type == '4':
            self._pie_chart(data)
        elif chart_type == '5':
            self._histogram(data)

        plt.tight_layout()
        plt.show()

    def _bar_chart(self, data):
        bars = plt.bar(data['labels'], data['values'], color=self.colors(np.linspace(0, 1, len(data['labels']))))
        plt.title("Bar Chart", fontweight='bold')
        plt.xlabel("Categories", fontweight='bold')
        plt.ylabel("Values", fontweight='bold')
        plt.xticks(rotation=45, ha='right')

        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height,
                     f'{height:.2f}',
                     ha='center', va='bottom')

    def _line_chart(self, data):
        plt.plot(data['x'], data['y'], color=self.colors(0.6), marker='o')
        plt.title("Line Chart", fontweight='bold')
        plt.xlabel("X-axis", fontweight='bold')
        plt.ylabel("Y-axis", fontweight='bold')
        plt.grid(True, linestyle='--', alpha=0.7)

    def _scatter_plot(self, data):
        plt.scatter(data['x'], data['y'], color=self.colors(0.6), alpha=0.7)
        plt.title("Scatter Plot", fontweight='bold')
        plt.xlabel("X-axis", fontweight='bold')
        plt.ylabel("Y-axis", fontweight='bold')
        plt.grid(True, linestyle='--', alpha=0.7)

    def _pie_chart(self, data):
        plt.pie(data['values'], labels=data['labels'], autopct='%1.1f%%', startangle=90,
                colors=self.colors(np.linspace(0, 1, len(data['values']))))
        plt.title("Pie Chart", fontweight='bold')
        plt.axis('equal')

    def _histogram(self, data):
        n, bins, patches = plt.hist(data['values'], bins=data['bins'], 
                                    color=self.colors(0.6), alpha=0.7, edgecolor='black')
        plt.title("Histogram", fontweight='bold')
        plt.xlabel("Values", fontweight='bold')
        plt.ylabel("Frequency", fontweight='bold')

        for i in range(len(n)):
            plt.text((bins[i]+bins[i+1])/2, n[i], f'{int(n[i])}', 
                     ha='center', va='bottom')