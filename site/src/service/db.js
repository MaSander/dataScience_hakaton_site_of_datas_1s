import clientes from "../db/commercial/clientes.json";
import produtos from "../db/commercial/produtos.json";
import vendas from "../db/commercial/vendas.json";

import orcamento from "../db/financial/orcamento.json";
import despesas from "../db/financial/despesas.json";

import frequencia from "../db/human_resources/frequencia.json";
import funcionarios from "../db/human_resources/funcionarios.json";
import turnos from "../db/human_resources/turnos.json";

import equipamentos from "../db/operational/equipamentos.json";
import materiais from "../db/operational/materiais.json";
import uso_equipamento from "../db/operational/uso_equipamento.json";

import entregas from "../db/transport/entregas.json";
import rotas from "../db/transport/rotas.json";

function getClient() {
  return clientes;
}

function getProdutos() {
  return produtos;
}

function getVendas() {
  return vendas;
}

function getOrcamento() {
  return orcamento;
}

function getDespesas() {
  return despesas;
}

function getFrequencia() {
  return frequencia;
}

function getFuncionarios() {
  return funcionarios;
}

function getTurnos() {
  return turnos;
}

function getEquipamentos() {
  return equipamentos;
}

function getMateriais() {
  return materiais;
}

function getUso_Equipamento() {
  return uso_equipamento;
}

function getEntregas() {
  return entregas;
}

function getRotas() {
  return rotas;
}

export {
  getRotas,
  getEntregas,
  getUso_Equipamento,
  getMateriais,
  getEquipamentos,
  getTurnos,
  getFuncionarios,
  getFrequencia,
  getDespesas,
  getOrcamento,
  getVendas,
  getProdutos,
  getClient,
};
