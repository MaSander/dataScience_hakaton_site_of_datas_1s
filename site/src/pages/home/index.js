import React from "react";
import "./home.css";

function HomePage() {
  return (
    <div className="App">
      <div>
        <h1>Alimenticia LDTA</h1>
        <nav>
          <ul>
            <li>
              <a href="#" className="active">
                Home
              </a>
            </li>
            <li>
              <a href="/clients">Clients</a>
            </li>
          </ul>
        </nav>
      </div>
      <main>
        <h2>Welcome to AlimenticiaLDTA</h2>
        <p>This is a simple home page.</p>
      </main>
    </div>
  );
}

export default HomePage;
