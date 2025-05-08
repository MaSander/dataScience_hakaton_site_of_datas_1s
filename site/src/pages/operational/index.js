import React, { useState } from "react";

import {
  getEquipamentos,
  getMateriais,
  getUso_Equipamento,
} from "../../service/db";

import TabelaGenerica from "../../utils/generate_table";

export default function OperationalPage() {
  const [subPage, setSubPage] = useState("equipamentos");

  let table;

  switch (subPage) {
    case "equipamentos":
      table = TabelaGenerica(getEquipamentos());
      break;
    case "materiais":
      table = TabelaGenerica(getMateriais());
      break;
    case "uso_equipamentos":
      table = TabelaGenerica(getUso_Equipamento());
      break;
    default:
      table = <div>Error</div>;
      break;
  }

  return (
    <div>
      <h2>Operacional</h2>

      <nav>
        <button onClick={() => setSubPage("equipamentos")}>Equipamentos</button>
        <button onClick={() => setSubPage("materiais")}>Materiais</button>
        <button onClick={() => setSubPage("uso_equipamentos")}>
          Uso de equipamentos
        </button>
      </nav>

      <div>{table}</div>
    </div>
  );
}
