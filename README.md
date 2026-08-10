# Outrora

**Interactive** RPG where your choices shape the development of the story.

![Home Screen](assets/images/tela_inicial.png)
![Firmament](assets/images/firmamento.png)
![Credits](assets/images/creditos.png)

---

## Technologies / Frameworks

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Kivy](https://img.shields.io/badge/Kivy-333333?style=for-the-badge&logo=python&logoColor=white)
![KivyMD](https://img.shields.io/badge/KivyMD-13505B?style=for-the-badge&logo=materialdesign&logoColor=white)

---

## Requirements

- **Python 3.8 to 3.13**
  - Recommended on Windows: **Python 3.12** or **3.13**
- Dependencies installed via `requirements.txt`

> Tip: using a virtual environment (`venv`) helps avoid dependency conflicts.

---

## Project structure

```text
.
├── .gitattributes
├── .gitignore
├── LICENSE
├── README.md
├── main.py
├── requirements.txt
├── data/
│   ├── __init__.py
│   └── story.py
└── assets/
    ├── images/
    └── audio/
```

### Main folders and files

- `main.py`: application entry point.
- `data/story.py`: story data/structure (e.g., scenes, choices, and consequences).
- `assets/`: game resources (images and audio).

---

## How to run (Windows / Linux / macOS)

### 1) Clone the repository

```bash
git clone https://github.com/diegobrnrd/outrora.git
cd outrora
```

### 2) Create and activate a virtual environment (recommended)

Create:

```bash
python -m venv .venv
```

Activate:

- Windows (PowerShell):
  ```powershell
  .\.venv\Scripts\Activate.ps1
  ```
- Windows (cmd):
  ```bat
  .\.venv\Scripts\activate.bat
  ```
- Linux/macOS:
  ```bash
  source .venv/bin/activate
  ```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

### 4) Run the game

```bash
python main.py
```

---

## Troubleshooting (quick)

- **`python` not found**: check whether Python is installed and in the `PATH`.
- **Error installing dependencies**: update pip:
  ```bash
  python -m pip install --upgrade pip
  ```
- **Virtual environment won't activate in PowerShell**: you may need to allow scripts:
  ```powershell
  Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
  ```

---

## Roadmap (ideas)

- [ ] New branches and alternative endings
- [ ] UI/UX improvements
- [ ] Integrated soundtrack and sound effects
- [ ] Packaging for Windows (executable)

---

## Author

[**Diego Bernardo**](https://github.com/diegobrnrd)

---

## License

This project is licensed under the **Apache License 2.0**.
See the [LICENSE](LICENSE) file.
