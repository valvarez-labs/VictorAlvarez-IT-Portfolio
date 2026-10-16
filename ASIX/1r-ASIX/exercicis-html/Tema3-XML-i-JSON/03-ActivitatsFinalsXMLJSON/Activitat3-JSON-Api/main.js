const panellPokemons = document.querySelector('#llista-pokemons');

const resposta = await fetch('./pokemons.json');
const dades = await resposta.json();

let llistaPokemons = dades.pokemons;
console.log(llistaPokemons);

function generarBadgesTipus(tipusArray) {
  return tipusArray.map(tipus => `<span class="badge badge--${tipus}">${tipus}</span>`).join('');
}

function crearTargeta(pokemon) {
  const article = document.createElement('article');
  article.classList.add('targeta');

  article.innerHTML = `
    <p class="targeta-numero">#${pokemon.id}</p>
    <img
      class="targeta-imatge"
      src="${pokemon.imatge}"
      alt="${pokemon.nom}"
      loading="lazy"
    >
    <h2 class="targeta-nom">${pokemon.nom}</h2>
    <div class="targeta-tipus">
      ${generarBadgesTipus(pokemon.tipus)}
    </div>
  `;

  return article;
}
function mostrarPokemons(pokemons) {
  panellPokemons.innerHTML = '';

  pokemons.forEach(pokemon => {
    const targeta = crearTargeta(pokemon);
    panellPokemons.appendChild(targeta);
  });
}

mostrarPokemons(llistaPokemons);
