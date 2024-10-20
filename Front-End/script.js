let allProducts = [];
let favoriteProducts = [];

async function fetchProducts() {
  try {
    const response = await fetch("http://127.0.0.1:8000/api/corona/products");
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error("Error al cargar los productos:", error);
    return [];
  }
}

async function fetchFavorites() {
  try {
    const response = await fetch("http://127.0.0.1:8000/api/corona/");
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error("Error al cargar los favoritos:", error);
    return [];
  }
}

async function addToFavorites(product) {
  try {
    const response = await fetch("http://127.0.0.1:8000/api/corona/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(product),
    });
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error("Error to add favorite:", error);
    return null;
  }
}

async function removeFromFavorites(productId) {
  try {
    const response = await fetch(
      `http://127.0.0.1:8000/api/corona/${productId}/`,
      {
        method: "DELETE",
      }
    );
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return true;
  } catch (error) {
    console.error("Error to delete favorite:", error);
    return false;
  }
}

function renderProducts(products, container, isFavorite = false) {
  container.innerHTML = "";
  products.forEach((product) => {
    const productElement = document.createElement("div");
    productElement.className = "producto";
    productElement.innerHTML = `
      <img src="${product.image}" alt="${product.title}">
      <h3>${product.title}</h3>
      <p>Precio: $${product.precio}</p>
      <button onclick="toggleFavorite(${product.id})">${
      isFavorite ? "Quitar de favoritos" : "Añadir a favoritos"
    }</button>
    `;
    container.appendChild(productElement);
  });
}

async function toggleFavorite(productId) {
  const product = allProducts.find((item) => item.id === productId);
  const isFavorite = favoriteProducts.some((fav) => fav.id === productId);
  try {
    if (isFavorite) {
      await removeFromFavorites(productId);
      favoriteProducts = favoriteProducts.filter((fav) => fav.id !== productId);
      updateView();
      return;
    }
    const addedFavorite = await addToFavorites(product);
    favoriteProducts.push(addedFavorite);
    updateView();
  } catch (error) {
    console.error("Error al modificar favoritos:", error);
  }
}

function updateView() {
  renderProducts(favoriteProducts, document.getElementById("favoritos"), true);
  renderProducts(allProducts, document.getElementById("productos"));
}

async function initialize() {
  allProducts = await fetchProducts();
  favoriteProducts = await fetchFavorites();
  updateView();
}

initialize();
