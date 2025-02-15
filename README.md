# JupyterStreet

A collection of financial analysis tools and notebooks for stock market analysis, with a focus on tech stocks and bubble detection.

## Features

- Stock price data retrieval using yfinance
- PE ratio analysis and bubble detection
- Comparison with historical bubbles (e.g., Dotcom bubble)
- Visualization tools for financial metrics

## Installation

1. Clone the repository:
```bash
git clone [your-repository-url]
cd JupyterStreet
```

2. Create and activate a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Notebooks
1. Start Jupyter Lab or Jupyter Notebook:
```bash
jupyter lab
# or
jupyter notebook
```

2. Open `NVDA_Bubble.ipynb` to see the NVIDIA stock analysis

### Using the Analysis Utils

```python
from src.analysis_utils import plot_pe_zscore

# Prepare your data with required columns: 'PE Ratio', 'PE Mean', 'PE Std'
# Then plot the PE Z-score
plot_pe_zscore(your_dataframe)
```

## Project Structure

```
JupyterStreet/
│
├── NVDA_Bubble.ipynb     # Main analysis notebook for NVIDIA stock
├── README.md            # Project documentation
├── requirements.txt     # Python dependencies
└── src/                # Source code directory
    ├── __init__.py
    └── analysis_utils.py  # Utility functions for financial analysis
```

## Contributing

Feel free to open issues or submit pull requests with improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Data provided by Yahoo Finance through yfinance
- Inspired by historical market analysis and bubble detection methods