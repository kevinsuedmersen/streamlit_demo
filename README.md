# Streamlit Demo App
Streamlit demo app which mocks an API call to a mock backend. Note that this API call will obviously fail if your backend is not running on http://localhost:8081.

## Installation
```bash
conda create -y -n streamlit_demo python=3.12
conda activate streamlit_demo
pip install -r requirements.txt
```

## Usage
```bash
export PYTHONPATH="${PYTHONPATH}:${PWD}"
streamlit run 1_HELLO_WORLD.py
```
bla1