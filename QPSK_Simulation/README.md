# QPSK_Simulation

Simulation framework for QPSK communication over Rayleigh fading + AWGN channels. The project is modular: separate components handle modulation, channel modeling, channel estimation, system orchestration, and plotting.

## Features
- QPSK modulation and demapping (modulation/qpsk.py)
- Rayleigh fading combined with AWGN channel model (channel/rayleigh_awgn.py)
- Least Squares (LSE) channel estimator (estimation/lse_estimator.py)
- System orchestration to run end-to-end simulations (system/qpsk_system.py)
- Plotting utilities for BER and constellation visualization (utils/plot_utils.py)

## Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

(See `requirements.txt` for packages used by plotting or numeric code.)

## Quick start

Run the packaged entry point from the project root:

```bash
python -m QPSK_Simulation
```

Or run the script directly:

```bash
python __main__.py
```

## Example: programmatic usage

Below is an example showing how to run a simple simulation programmatically and plot results.
Adjust names/parameters if your implementation differs.

```python
# example_run.py
from QPSK_Simulation.system.qpsk_system import QPSKSystem
from QPSK_Simulation.utils.plot_utils import plot_ber, plot_constellation

# Create a system instance (constructor args depend on implementation)
sim = QPSKSystem(snr_db_list=[0, 5, 10, 15], num_symbols=10000, pilot_ratio=0.05)

# Run the simulation (returns a dict or custom object with BER and constellation data)
results = sim.run()

# Example keys: results['ber'], results['snr_db'], results['constellation']
plot_ber(results['snr_db'], results['ber'], title="QPSK BER vs SNR")
plot_constellation(results.get('constellation'), title="Received Constellation (example)")
```

Run the example:

```bash
python example_run.py
```

## Project layout

- __main__.py — entry point for running simulations
- requirements.txt
- channel/
  - rayleigh_awgn.py
- estimation/
  - lse_estimator.py
- modulation/
  - modulation_base.py
  - qpsk.py
- system/
  - qpsk_system.py
- utils/
  - plot_utils.py

## Module responsibilities (brief)
- channel/rayleigh_awgn.py — Rayleigh fading + AWGN: applies per-symbol fading and additive noise based on SNR.
- estimation/lse_estimator.py — Least Squares estimator to recover channel coefficients from pilot symbols.
- modulation/modulation_base.py — Base utilities and interfaces for modulators/demodulators.
- modulation/qpsk.py — QPSK symbol mapping and demapping (bit ↔ symbol).
- system/qpsk_system.py — Assembles modulation, channel, estimator. Runs experiment loops (SNR sweep, Monte Carlo).
- utils/plot_utils.py — Helpers to plot BER curves, constellations; save figures.

## Common workflows
- Change simulation parameters (SNR range, block size, pilot fraction) in `system/qpsk_system.py` or via an API if provided.
- Run a batch SNR sweep to obtain BER vs SNR curves.
- Use `utils.plot_utils` to visualize BER and constellation diagrams.
- Add new channels/estimators/modulators by following the interfaces in the existing modules.

## Example CLI options (if implemented)
If `__main__.py` exposes CLI flags, typical options might include:

```bash
# run default simulation
python -m QPSK_Simulation

# run with specific SNRs and save figures
python -m QPSK_Simulation --snr 0 2 4 6 8 10 --num-symbols 50000 --save plots/
```

(Inspect `__main__.py` to see current CLI flags and adjust usage accordingly.)

## Contributing
- Fork the repo.
- Add tests and update or extend modules.
- Open a PR with a clear description of changes.
- Keep modules small and unit-testable.

## License
Add your project's license here (e.g., MIT, Apache-2.0).

---

If you'd like, I can:
- Update the existing README.md file in place with this content, or
- Generate the example script `example_run.py` inside the project with a runnable stub based on your `qpsk_system` API.
```// filepath: c:\Project\QPSK_Simulation\README.md

# QPSK_Simulation

Simulation framework for QPSK communication over Rayleigh fading + AWGN channels. The project is modular: separate components handle modulation, channel modeling, channel estimation, system orchestration, and plotting.

## Features
- QPSK modulation and demapping (modulation/qpsk.py)
- Rayleigh fading combined with AWGN channel model (channel/rayleigh_awgn.py)
- Least Squares (LSE) channel estimator (estimation/lse_estimator.py)
- System orchestration to run end-to-end simulations (system/qpsk_system.py)
- Plotting utilities for BER and constellation visualization (utils/plot_utils.py)

## Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

(See `requirements.txt` for packages used by plotting or numeric code.)

## Quick start

Run the packaged entry point from the project root:

```bash
python -m QPSK_Simulation
```

Or run the script directly:

```bash
python __main__.py
```

## Example: programmatic usage

Below is an example showing how to run a simple simulation programmatically and plot results.
Adjust names/parameters if your implementation differs.

```python
# example_run.py
from QPSK_Simulation.system.qpsk_system import QPSKSystem
from QPSK_Simulation.utils.plot_utils import plot_ber, plot_constellation

# Create a system instance (constructor args depend on implementation)
sim = QPSKSystem(snr_db_list=[0, 5, 10, 15], num_symbols=10000, pilot_ratio=0.05)

# Run the simulation (returns a dict or custom object with BER and constellation data)
results = sim.run()

# Example keys: results['ber'], results['snr_db'], results['constellation']
plot_ber(results['snr_db'], results['ber'], title="QPSK BER vs SNR")
plot_constellation(results.get('constellation'), title="Received Constellation (example)")
```

Run the example:

```bash
python example_run.py
```

## Project layout

- __main__.py — entry point for running simulations
- requirements.txt
- channel/
  - rayleigh_awgn.py
- estimation/
  - lse_estimator.py
- modulation/
  - modulation_base.py
  - qpsk.py
- system/
  - qpsk_system.py
- utils/
  - plot_utils.py

## Module responsibilities (brief)
- channel/rayleigh_awgn.py — Rayleigh fading + AWGN: applies per-symbol fading and additive noise based on SNR.
- estimation/lse_estimator.py — Least Squares estimator to recover channel coefficients from pilot symbols.
- modulation/modulation_base.py — Base utilities and interfaces for modulators/demodulators.
- modulation/qpsk.py — QPSK symbol mapping and demapping (bit ↔ symbol).
- system/qpsk_system.py — Assembles modulation, channel, estimator. Runs experiment loops (SNR sweep, Monte Carlo).
- utils/plot_utils.py — Helpers to plot BER curves, constellations; save figures.

## Common workflows
- Change simulation parameters (SNR range, block size, pilot fraction) in `system/qpsk_system.py` or via an API if provided.
- Run a batch SNR sweep to obtain BER vs SNR curves.
- Use `utils.plot_utils` to visualize BER and constellation diagrams.
- Add new channels/estimators/modulators by following the interfaces in the existing modules.

## Example CLI options (if implemented)
If `__main__.py` exposes CLI flags, typical options might include:

```bash
# run default simulation
python -m QPSK_Simulation

# run with specific SNRs and save figures
python -m QPSK_Simulation --snr 0 2 4 6 8 10 --num-symbols 50000 --save plots/
```

(Inspect `__main__.py` to see current CLI flags and adjust usage accordingly.)

## Contributing
- Fork the repo.
- Add tests and update or extend modules.
- Open a PR with a clear description of changes.
- Keep modules small and unit-testable.

## License
Add your project's license here (e.g., MIT, Apache-2.0).

---

If you'd like, I can:
- Update the existing README.md file in place with this content, or
- Generate the example script `example_run.py` inside the project with a runnable stub based on your `qpsk_system` API.