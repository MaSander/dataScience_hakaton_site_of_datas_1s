import React, { useState } from "react";

import { getFrequencia, getFuncionarios, getTurnos } from "../../service/db";

import TabelaGenerica from "../../utils/generate_table";

export default function HumanResourcesPage() {
  const [subPage, setSubPage] = useState("frequencia");

  let table;

  switch (subPage) {
    case "frequencia":
      table = TabelaGenerica(getFrequencia());
      break;
    case "funcionarios":
      table = TabelaGenerica(getFuncionarios());
      break;
    case "turnos":
      table = TabelaGenerica(getTurnos());
      break;
    default:
      table = <div>Error</div>;
      break;
  }

  return (
    <div>
      <h2>RH - Recursos Humanos</h2>

      <nav>
        <button onClick={() => setSubPage("frequencia")}>Frequencia</button>
        <button onClick={() => setSubPage("funcionarios")}>Funcionários</button>
        <button onClick={() => setSubPage("turnos")}>Turnos</button>
      </nav>

      <div>{table}</div>
    </div>
  );
}
