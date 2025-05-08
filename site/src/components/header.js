import React from "react";
import "./header.css";

function Header() {
  return (
    <header>
      <a href="/">Home</a>
      <a href="/humanresources">RH</a>
      <a href="/financial">Financeiro</a>
      <a href="/commercial">Comercial</a>
      <a href="/operational">Operacional</a>
      <a href="/transport">Transporte</a>
    </header>
  );
}

export default Header;
