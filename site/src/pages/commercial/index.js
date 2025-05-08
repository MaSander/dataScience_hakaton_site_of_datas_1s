import React, { useState } from "react";

import { getClient, getVendas, getProdutos } from "../../service/db";
import TabelaGenerica from "../../utils/generate_table";

function CommercialPage() {
  const [subPage, setSubPage] = useState("produtos");
  let table;

  switch (subPage) {
    case "clientes":
      table = TabelaGenerica(getClient());
      break;
    case "produtos":
      table = TabelaGenerica(getProdutos());
      break;
    case "vendas":
      table = TabelaGenerica(getVendas());
      break;
    default:
      table = <div>Error</div>;
  }

  return (
    <div className="App">
      <h2>CommercialPage</h2>

      <div>
        <nav>
          <button onClick={() => setSubPage("clientes")}>Clientes</button>
          <button onClick={() => setSubPage("produtos")}>Produtos</button>
          <button onClick={() => setSubPage("vendas")}>Vendas</button>
        </nav>

        <div>{table}</div>
      </div>
    </div>
  );
}

export default CommercialPage;
