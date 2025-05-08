import React, { StrictMode } from "react";
import { createRoot } from "react-dom/client";

import Header from "./components/header";

import HomePage from "./pages/home";
import ComercialPage from "./pages/commercial";
import FinancialPage from "./pages/financial";
import OperationalPage from "./pages/operational";
import TransportPage from "./pages/transport";
import HumanResourcesPage from "./pages/human_resources";

import NotFoundPage from "./pages/notFound";

import "./assets/table.css";

import { createBrowserRouter, RouterProvider } from "react-router-dom";

const router = createBrowserRouter([
  { path: "/", element: <HomePage /> },
  { path: "/commercial", element: <ComercialPage /> },
  { path: "/humanresources", element: <HumanResourcesPage /> },
  { path: "/financial", element: <FinancialPage /> },
  { path: "/operational", element: <OperationalPage /> },
  { path: "/transport", element: <TransportPage /> },
  { path: "*", element: <NotFoundPage /> },
]);

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <Header />
    <RouterProvider router={router} />
  </StrictMode>,
);
