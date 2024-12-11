# Quickstart: Federated Averaging (FedAvg)

## Setup

### 1. Clone the repository

Begin by cloning the BlazeFL repository and navigating to the `quickstart-fedavg` directory:

```bash
git clone https://github.com/kitsuya0828/blazefl.git
cd blazefl/examples/quickstart-fedavg
```

### 2. Install the dependencies

Install the required dependencies using [uv](https://github.com/astral-sh/uv) or other package managers:

```bash
uv sync

# or

python -m venv .venv
source .venv/bin/activate
pip install .
```

## Running the example

To execute the FedAvg example, run the following command:

```bash
uv run python main.py --num_parallels 3
```

Adjust the `--num_parallels` parameter based on your system’s specifications to optimize performance.

For additional options and configurations, please refer to the [`main.py`](https://github.com/kitsuya0828/BlazeFL/blob/main/examples/quickstart-fedavg/main.py) file.