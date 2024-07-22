import csv
import json

class DataHandler:
    def get_data(self, chart_type):
        if chart_type in ['1', '4']:  # Bar Chart or Pie Chart
            return self._get_labeled_data()
        elif chart_type in ['2', '3']:  # Line Chart or Scatter Plot
            return self._get_xy_data()
        elif chart_type == '5':  # Histogram
            return self._get_histogram_data()

    def _get_labeled_data(self):
        data = {'labels': [], 'values': []}
        print("Enter data in the format 'label,value' (press Enter to finish):")
        while True:
            line = input().strip()
            if not line:
                break
            try:
                label, value = line.split(',')
                data['labels'].append(label.strip())
                data['values'].append(float(value.strip()))
            except ValueError:
                print("Invalid input. Please use the format 'label,value'.")
        return data if data['labels'] and data['values'] else None

    def _get_xy_data(self):
        data = {'x': [], 'y': []}
        print("Enter data in the format 'x,y' (press Enter to finish):")
        while True:
            line = input().strip()
            if not line:
                break
            try:
                x, y = line.split(',')
                data['x'].append(float(x.strip()))
                data['y'].append(float(y.strip()))
            except ValueError:
                print("Invalid input. Please use the format 'x,y'.")
        return data if data['x'] and data['y'] else None

    def _get_histogram_data(self):
        data = {'values': [], 'bins': 10}
        print("Enter numeric values (press Enter to finish):")
        while True:
            line = input().strip()
            if not line:
                break
            try:
                data['values'].append(float(line))
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        if data['values']:
            bins = input("Enter the number of bins (default is 10): ").strip()
            if bins and bins.isdigit():
                data['bins'] = int(bins)
            return data
        return None

    def load_from_csv(self, filename):
        data = {'labels': [], 'values': []}
        try:
            with open(filename, 'r') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if len(row) == 2:
                        data['labels'].append(row[0])
                        data['values'].append(float(row[1]))
            return data if data['labels'] and data['values'] else None
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except csv.Error:
            print(f"Error reading CSV file '{filename}'.")
        return None

    def load_from_json(self, filename):
        try:
            with open(filename, 'r') as jsonfile:
                data = json.load(jsonfile)
            return data if 'labels' in data and 'values' in data else None
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON file '{filename}'.")
        return None