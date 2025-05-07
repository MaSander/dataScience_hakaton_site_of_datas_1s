import React, { StrictMode } from "react";
import { createRoot } from "react-dom/client";

import Header from "./components/header";

import HomePage from "./pages/home";
import ClientPage from "./pages/client";

import { createBrowserRouter, RouterProvider } from "react-router-dom";

const router = createBrowserRouter([
  { path: "/", element: <HomePage /> },
  { path: "/clients", element: <ClientPage /> },
  // { path: "*", element: HomePage },
]);

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <Header />
    <RouterProvider router={router} />
  </StrictMode>,
);
