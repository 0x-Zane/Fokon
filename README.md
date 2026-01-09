![image alt](https://github.com/0x-Zane/Fokon/blob/7eaa9e36eeabff5597c3f842cb1eb0a59a60eea8/assets/banner_fokon.png)

# FOKON

[![Python](https://img.shields.io/badge/Python-3.14.2-blue.svg)](https://www.python.org/)
[![discord.py](https://img.shields.io/badge/discord.py-latest-blue.svg)](https://discordpy.readthedocs.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Discord Buildathon 2025](https://img.shields.io/badge/Discord-Buildathon%202025-5865F2.svg)](https://discord.com/)

Fokon is an open source Discord bot created in Python for the Discord Buildathon 2025. The project aims to provide useful tools for developers, science enthusiasts, and people interested in computer science and general sciences, whether for their daily tasks or for learning purposes.

## Table of Contents

- [FOKON](#fokon)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
  - [Features](#features)
  - [Commands](#commands)
    - [Quiz](#quiz)
    - [Science](#science)
    - [Electronics](#electronics)
    - [Utilities](#utilities)
  - [Project Structure](#project-structure)
  - [Tech Stack](#tech-stack)
  - [Contributing](#contributing)
    - [How to Contribute](#how-to-contribute)
    - [Contribution Areas](#contribution-areas)
    - [Code Guidelines](#code-guidelines)
  - [Roadmap](#roadmap)
    - [General Improvements](#general-improvements)
    - [Commands to Implement](#commands-to-implement)
    - [Implemented Commands](#implemented-commands)
  - [License](#license)
  - [Acknowledgments](#acknowledgments)

## About

Fokon is a modular Discord bot that offers a collection of slash commands organized by categories. The project is actively developed and open to community contributions. The goal is to create a versatile tool that combines practical utilities and educational content.

The bot uses the modern Discord API with slash commands and supports different categories of features ranging from educational quizzes to electronic calculation tools.

## Features

**Educational Quizzes**

Quiz system covering eight different domains: software, hardware, electronics, cybersecurity, blockchain, 3dmodeling, webdevelopment, networking. Each category contains questions with answers for learning and practice.

**Periodic Table**

Complete access to information on all 118 elements of the periodic table. Search by symbol, name, or atomic number with display of physical and chemical properties.

**Electronic Tools**

Electrical resistance calculations and resistor color code decoding (4 and 5 bands). Useful for electronics projects and learning.

**Utilities**

Random number generator, GitHub repository information retrieval, and links to online communication resources.

## Commands

### Quiz

`/quizz {category}` - Generates a random question in the specified category.

Available categories: `cybersecurity`, `hardware`, `software`, `networking`, `3dmodeling`, `webdevelopment`, `electronics`, `blockchain`.

### Science

`/periodic {element}` - Displays detailed information about a periodic table element.

The argument can be the symbol (e.g., "H"), the name (e.g., "Hydrogen"), or the atomic number (e.g., "1").

### Electronics

`/resistance {voltage} {current}` - Calculates the required resistance for a given voltage and current according to Ohm's law.

`/resistance_color {number_of_lines} {color1} {color2} {color3} {color4} {color5}` - Decodes a resistor color code and displays its value in ohms as well as its tolerance.

### Utilities

`/random {minimum} {maximum}` - Generates a random number between two values.

`/github {repo}` - Retrieves and displays information about a GitHub repository. Expected format: `username/repositoryname`.

`/nohello` - Displays a link to nohello.net.

`/dontasktoask` - Displays a link to dontasktoask.com.

`/info` - Displays a link to this README.

## Project Structure

```
Fokon/
├── source/
│   └── main.py              # Main bot code
├── assets/
│   ├── images/              # Images and banners
│   └── text_sources/        # JSON data
│       ├── periodic.json    # Periodic table data
│       └── quizz.json       # Quiz questions by category
├── requirements.txt         # Python dependencies
├── LICENSE                  # MIT License
└── README.md               # Documentation
```

## Tech Stack

- **Python 3.14.2** - Programming language
- **discord.py** - Library for Discord API
- **requests** - HTTP requests for external APIs
- **python-dotenv** - Environment variable management

discord.py documentation: [discordpy.readthedocs.io](https://discordpy.readthedocs.io/en/stable/ext/commands/api.html#discord.ext.commands.Context)

## Contributing

Contributions are essential to the project's development. Several areas for improvement are available.

### How to Contribute

1. Fork the repository
2. Create a branch for your modification (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -m 'Add a new feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Open a Pull Request

### Contribution Areas

**Code Improvement**

The code can be optimized and improved. If you identify bugs, duplicated code, optimization opportunities, or performance issues, feel free to propose your modifications.

**Data Verification**

The JSON files in `assets/text_sources/` contain periodic table data and quiz questions. This data was largely generated by AI and may contain errors. Any correction is appreciated.

**New Features**

Several commands are planned but not yet implemented (see Roadmap section). Proposals for new features are also welcome. Discuss them first in an issue to validate the approach.

**Issue Resolution**

If issues are open on the repository and you have a solution, feel free to contribute. Make sure to read existing comments before starting.

**Documentation**

Improving documentation, whether in the README or in code comments, is always appreciated.

### Code Guidelines

- Respect the existing code style
- Add comments for complex parts
- Test your modifications before submitting a PR
- Ensure the code works without errors

## Roadmap

### General Improvements

- [ ] Add cooldowns to all commands (currently only on `/github`)
- [ ] Improve error handling
- [ ] Optimize searches in JSON data
- [ ] Refactor duplicated code

### Commands to Implement

- [ ] `/ocr {image}` - Extract text from an image

- [ ] `/whois {website}` - Retrieve information about a domain

### Implemented Commands

- [x] `/random` - Random number generator
- [x] `/github` - GitHub repository information
- [x] `/quizz` - Quiz system with category selection
- [x] `/nohello` - Link to nohello.net
- [x] `/dontasktoask` - Link to dontasktoask.com
- [x] `/resistance` - Electrical resistance calculation
- [x] `/resistance_color` - Resistor color code decoding
- [x] `/periodic` - Periodic table lookup
- [x] `/base_convert {number} {from} {to}` - Convert a number from one base to another
## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

Thanks to the [Discord Developers](https://discord.gg/discord-developers) community for the support and ideas brought to the project.

The code for displaying GitHub repository information is inspired by an article by Rachelle Palmer on [dev.to](https://dev.to/techbelle/how-to-retrieve-github-repository-data-using-python-59g3).
