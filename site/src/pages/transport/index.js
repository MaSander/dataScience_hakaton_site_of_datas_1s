import React, { useState } from "react";

import { getEntregas, getRotas } from "../../service/db";

import TabelaGenerica from "../../utils/generate_table";

export default function TransportPage() {
  const [subPage, setSubPage] = useState("entregas");

  let table;

  switch (subPage) {
    case "entregas":
      table = TabelaGenerica(getEntregas());
      break;
    case "rotas":
      table = TabelaGenerica(getRotas());
      break;
    default:
      table = <div>Error</div>;
      break;
  }

  return (
    <div>
      <h2>Transporte</h2>

      <nav>
        <button onClick={() => setSubPage("entregas")}>Entregas</button>
        <button onClick={() => setSubPage("rotas")}>Rotas</button>
      </nav>

      <div>{table}</div>
    </div>
  );
}
