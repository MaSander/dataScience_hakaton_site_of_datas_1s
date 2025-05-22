# Data Science Hakaton - Fictitious Food Company Website

## Project Overview

This repository contains the code for a fictitious food company website built during a Data Science Hakaton for first-semester SENAI students. The project demonstrates data generation and website display, leveraging web scraping techniques.

The repository is divided into two main projects:

1.  **Data Generation (`geradorDeDados`):** This project generates synthetic data for various aspects of the fictitious food company's operations (customers, expenses, deliveries, equipment, etc.).
2.  **Website Display (`site`):** This project builds a website that presents the generated data using React.

## Technologies Used

### Data Generation

*   **Python:** Used for scripting the data generation process.
*   **`subprocess` module:** Used to run the various Python scripts that create the datasets.

### Website Display

*   **React:** JavaScript library for building user interfaces.
*   **React Router:** Library for handling navigation within the React application.
*   **JavaScript (ES6+):** Programming language for front-end development.
*   **CSS:** For styling the website.
*   **Node.js:** JavaScript runtime environment used for running build tools and development server.

## Getting Started

### Prerequisites

*   **Python 3:** Required for running the data generation scripts.
*   **Node.js and npm (or yarn):** Required for setting up and running the React website.

### Running the Data Generation Project (`geradorDeDados`)

1.  Navigate to the `geradorDeDados` directory:
    ```bash
    cd geradorDeDados
    ```
2.  Ensure you have Python 3 installed.
3.  Run the `main.py` script:
    ```bash
    python main.py
    ```
    This will execute a series of Python scripts to generate the datasets.

### Running the Website (`site`)

1.  Navigate to the `site` directory:
    ```bash
    cd site
    ```
2.  Install the project dependencies:
    ```bash
    npm install
    ```
    Or if you prefer using yarn:
    ```bash
    yarn install
    ```
3.  Start the development server:
    ```bash
    npm start
    ```
    Or using yarn:
    ```bash
    yarn start
    ```
    This will open the website in your browser (usually at `http://localhost:3000`).

## Project Structure

*   **`dataScience_hakaton_site_of_datas_1s/`:** Root directory of the project.
    *   **`geradorDeDados/`:** Contains the data generation scripts.
        *   `main.py`: Main script to execute the data generation process.
        *   `gerarClientes.py`: Script to generate client data.
        *   `gerarDespesas.py`: Script to generate expense data.
        *   ... (other data generation scripts)
    *   **`site/`:** Contains the website code.
        *   `package.json`: Defines project dependencies and scripts.
        *   `src/`: Contains the React components and pages.
            *   `components/`: Contains reusable React components (e.g., `Header.js`).
            *   `pages/`: Contains the different pages of the website (e.g., `HomePage.js`, `ComercialPage.js`).
        *   `public/`: Contains static assets (e.g., images, CSS files).

## Deployment

This project uses GitHub Pages for deployment. The `site` project is deployed automatically when changes are pushed to the `main` branch of the repository.

## Contributing

Contributions are welcome! If you find any bugs or have any suggestions for improvements, please submit an issue or pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
