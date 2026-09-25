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

This project is developed using a collaborative human-AI workflow. The code, architecture, and documentation were written and refined with the assistance of advanced AI models. 

I approach AI not as a tool for blind self-automation, but as a collaborative interaction. I aspire to be a [centaur](https://mitsloan.mit.edu/ideas-made-to-matter/3-ways-to-use-ai-are-you-a-cyborg-a-centaur-or-a-self-automator), "... maintain[ing] structured and controlled interactions with AI, harnessing it as a tool for targeted efficiency". I acknowledge that when learning a new domain I might be a cyborg "... collaborat[ing] closely with the AI tool -- probing its suggestions, allowing it to lead the way, and taking its advice on some occasions while pushing back against it on others." Both are OK. In this model, the AI acts as a high-powered pair-programming partner. It helps me rapidly explore and develop my own understanding of complex topics. Meanwhile, I hold the strategic vision, conduct the physical testing/validation, and apply and build domain knowledge as I go.

For rules regarding AI-assisted contributions from the community, please see the [Code of Conduct](CODE_OF_CONDUCT.md).


## License

This project utilizes a **Dual License** structure to comply with both software and open-source hardware best practices. These specific open-source licenses were chosen to support the transition to an anarchist economy—promoting mutual aid, free distribution of information, and breaking down artificial scarcity.

*   **Software (Python Code):** All source code in this repository is licensed under the [GNU General Public License v3.0 (GPLv3)](COPYING). This ensures that any modifications to the code remain open-source and provides explicit patent protections.
*   **Hardware (3D Models):** The generated output files (STL and STEP files) are licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0)](LICENSE). This is the standard license for the 3D printing community.

