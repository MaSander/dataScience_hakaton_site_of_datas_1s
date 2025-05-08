import React from "react";

/**
 * Componente genérico para renderizar uma tabela a partir de um array de objetos JSON.
 *
 * @param {Object[]} data - Array de objetos JSON com os dados.
 * @param {string[]} [columns] - Opcional. Array com as chaves dos objetos que serão exibidas como colunas.
 *                               Se não informado, usa todas as chaves do primeiro objeto.
 * @param {string} [keyField] - Opcional. Nome da propriedade para usar como key no <tr>. Se não informado, usa índice.
 */
export default function TabelaGenerica(data, columns, keyField) {
  console.log("data.length");
  console.log(data);

  if (!data || data.length === 0) {
    return <p>Nenhum dado disponível.</p>;
  }

  // Se não recebeu colunas, pega as chaves do primeiro objeto
  const cols = columns && columns.length > 0 ? columns : Object.keys(data[0]);

  return (
    <table style={{ width: "100%", borderCollapse: "collapse" }}>
      <thead>
        <tr>
          {cols.map((col) => (
            <th key={col}>{col.charAt(0).toUpperCase() + col.slice(1)}</th>
          ))}
        </tr>
      </thead>
      <tbody>
        {data.map((item, index) => (
          <tr
            key={keyField && item[keyField] ? item[keyField] : index}
            style={{ borderBottom: "1px solid #ddd" }}
          >
            {cols.map((col) => (
              <td key={col} style={{ padding: "8px" }}>
                {item[col]}
              </td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );
}
