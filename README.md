# `tech_blog`

# DataBooth Technical Blog / Articles

Welcome to the **DataBooth Technical Blog** repository!  
This repo hosts technical articles, code samples, and reusable utilities related to data engineering, analytics, and Python programming. It is designed to be a resource for sharing insights, tutorials, and practical tools with the data community.


## Status

![Status](https://img.shields.io/badge/status-active-brightgreen.svg)

*The various code samples and articles in this repository are in various states of completion and some are evaluating
tools/libraries at different stages of development.*

---

## Table of Contents

- [`tech_blog`](#tech_blog)
- [DataBooth Technical Blog / Articles](#databooth-technical-blog--articles)
  - [Status](#status)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
  - [Repository Structure](#repository-structure)
    - [Decorators](#decorators)
    - [Perspective](#perspective)
    - [SQL](#sql)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Configuration](#configuration)
  - [Usage](#usage)
    - [Task Automation](#task-automation)
  - [Contributing](#contributing)
  - [License](#license)
  - [Contact](#contact)

---

## About

This repository contains:

- **Technical blog articles**: Jupyter notebooks and markdown files covering data engineering, analytics, and software development topics.
- **Reusable code**: Python modules, decorators, and SQL scripts for data workflows.
- **Examples & tutorials**: Hands-on guides and illustrative code samples.

Whether you're a data professional, student, or enthusiast, hopefully you'll find practical resources and inspiration here.

---

## Repository Structure

```text
tech_blog/
├── decorators/           # Python decorators for reusable logic
├── perspective/          # Perspective-related utilities and articles
├── sql/                  # SQL scripts and examples
├── src/tech_blog/        # Main Python package (core code) - *currently empty*
├── tests/                # Unit and integration tests
├── .gitignore
├── .python-version
├── justfile              # Justfile for task automation
├── pyproject.toml        # Project configuration (dependencies, metadata)
├── uv.lock               # Dependency lock file
├── LICENSE
└── README.md             # This file
```

### Decorators

See [`arg_from_file`](decorators/arg_file_file_linkedin.md) decorator - allows functions to accept either a string or a file path containing the string.

### Perspective

See an [Introduction to Perspective] (perspective/perspective_intro.md). 

*Note that this experiment is not yet complete - the initial evaluation of [Perpsective](https://perspective.finos.org) was performed in mid February 2025. I contacted the team to flag some issues in October 2024 and was directed to new documentation https://docs.rs/perspective-python/latest/perspective_python/ - I have not yet had time to review this.*

### SQL

See [`sql`](sql/) directory for SQL scripts and examples which are used in the other examples e.g. `decorators`.

---

## Getting Started

### Prerequisites

- **Python 3.10+** (see `.python-version`)
- [uv](https://github.com/astral-sh/uv) for dependency management (or your preferred tool)
- [Just](https://just.systems/) (optional) for task automation

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/DataBooth/tech_blog.git
   cd tech_blog
   ```

2. **Install dependencies:**

See `pyproject.toml` for dependencies

```bash
uv sync
```

---

## Configuration

Project configuration is managed in [`pyproject.toml`](./pyproject.toml).  
If you add custom settings, prefer TOML or YAML for clarity and structure.

---

## Usage

- **Explore articles**: Browse the `src/tech_blog/` and notebook files for tutorials and code samples.
- **Run code examples**: Open Jupyter notebooks locally or on [Hugging Face Spaces](https://huggingface.co/spaces) for interactive exploration.
- **Use decorators and utilities**: Import from the `decorators/` and `src/tech_blog/` directories in your own projects.

### Task Automation

If you have [Just](https://just.systems/) installed, you can run predefined tasks:

```bash
just 
```

Check the `justfile` for available commands.

---

## Contributing

Contributions are welcome!  
Feel free to open issues, submit pull requests, or suggest topics for future articles.

**To contribute:**

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Open a pull request

---

## License


This project is licensed under the [Apache-2.0 License](./LICENSE).  

![License](https://img.shields.io/badge/license-Apache--2.0-blue)

---

## Contact

For questions or collaboration, please open an issue or reach out via [github@databooth.com.au](mailto:github@databooth.com.au).

---

**Happy coding and I hope maybe some helpful learning!**