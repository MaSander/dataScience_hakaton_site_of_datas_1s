import React, { useState } from "react";

import { getDespesas, getOrcamento } from "../../service/db";
import TabelaGenerica from "../../utils/generate_table";

function FinancialPage() {
  const [subPage, setSubPage] = useState("despesas");

  let table;

  switch (subPage) {
    case "despesas":
      table = TabelaGenerica(getDespesas());
      break;
    case "orcamento":
      table = TabelaGenerica(getOrcamento());
      break;
    default:
      table = <div>Error</div>;
      break;
  }

  return (
    <div>
      <h2>Financeiro</h2>

      <nav>
        <button onClick={() => setSubPage("despesas")}>Despesas</button>
        <button onClick={() => setSubPage("orcamento")}>Orçamentos</button>
      </nav>

      <div>{table}</div>
    </div>
  );
}

export default FinancialPage;
