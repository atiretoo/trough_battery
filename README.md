# Trough Battery

Drew's adult daughter made the mistake of suggesting they build a fuel cell. One thing led to another and Drew discovered that chemistry is actually interesting and energy storage is cool. There are various projects underway in this area, but this one grew out of a desire to replicate early battery experiments in historically accurate ways. And then also to hook up a Cruickshank cell to a modern battery cycler. Because. 

## How to Install & Use

This project uses Python and [CadQuery](https://cadquery.readthedocs.io/) to generate 3D models (STL files) from code. You don't need to be a Python expert to generate your own models, just follow these steps:

### 1. Install Prerequisites
You will need Python installed on your computer. 
*   **Install uv:** We highly recommend using `uv` (a very fast Python package manager). You can install it following [their official guide](https://docs.astral.sh/uv/getting-started/installation/).

### 2. Setup the Project
Clone the repository and install `cadquery`:
```bash
git clone https://github.com/atiretoo/trough_battery.git
cd trough_battery

# Create a virtual environment and install dependencies
uv venv
uv pip install -r requirements.txt
```

### 3. Generate the Models
You can run the generator scripts individually (e.g., `python src/trough_battery.py`) to generate the parts.

**On Windows:**
Activate the environment and run the script:
```cmd
.venv\Scripts\activate
python src\trough_battery.py
```

**On Mac / Linux:**
Activate the environment and run the script:
```bash
source .venv/bin/activate
python src/trough_battery.py
```

## Rationale & Inspiration

This project grew out of a desire to replicate early battery experiments in historically accurate ways. By utilizing parametric CAD tools like CadQuery, we can bridge the gap between historical chemistry and modern manufacturing. This allows us to rapidly prototype, iterate, and generate the necessary components for a Cruickshank cell that can interface with modern battery cycling equipment.

## Development & AI Policy: The "Centaur" Approach

This project is developed using a collaborative human-AI workflow. The CadQuery scripts, Python generators, and overall system architecture were written and refined with the assistance of AI, such as **Google Gemini**. 

We approach AI not as a tool for blind automation, but as a [collaborative "Centaur"](https://mitsloan.mit.edu/ideas-made-to-matter/3-ways-to-use-ai-are-you-a-cyborg-a-centaur-or-a-self-automator). In this model, the AI acts as a high-powered pair-programming partner. It helps us rapidly explore and develop our own understanding of complex topics—whether that is navigating the quirks of 3D modeling coordinate systems, optimizing Python code, or learning battery chemistry. Meanwhile, we maintain the strategic vision, conduct the physical testing, and apply and build domain knowledge as we go.

For rules regarding AI-assisted contributions from the community, please see our [Code of Conduct](CODE_OF_CONDUCT.md).

## License

The files are released under the **CC BY-SA 4.0 (Copyleft)** license. This specific open-source license was chosen to support the transition to an anarchist economy—promoting mutual aid, free distribution of information, and breaking down artificial scarcity. Anyone is free to download, print, modify, and even commercialize these files, provided they attribute the original creators and share any modifications under the exact same open license.

This project is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0)](LICENSE).
