# Data Visualization Tool

A Python-based application for generating various types of charts and graphs from user-input data.

## Features

- Create multiple types of visualizations:
  - Bar Charts
  - Line Charts
  - Scatter Plots
  - Pie Charts
  - Histograms
- User-friendly command-line interface
- Supports manual data input
- Option to load data from CSV and JSON files
- Customizable chart appearance

## Requirements

- Python 3.x
- matplotlib
- numpy

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/JohnDev19/Data-Visualization-Tool.git
   ```
2. Navigate to the project directory:
   ```
   cd Data-Visualization-Tool
   ```
3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the main script:

```
python main.py
```

Follow the on-screen prompts to select the type of chart and input your data.

## File Structure

- `main.py`: Entry point of the application
- `visualizer.py`: Contains the Visualizer class for creating charts
- `data_handler.py`: Handles data input and processing
- `ui.py`: Manages the user interface
- `config.py`: Stores configuration settings

## Customization

You can customize the appearance of the charts by modifying the `config.py` file. Adjust the `FIGURE_SIZE` variable to change the size of the generated charts.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
