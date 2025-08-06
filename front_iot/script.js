const distanceDisplay = document.getElementById("distance");
const updateForm = document.getElementById("updateForm");

async function fetchDistance() {
  try {
    const res = await fetch("/get-distance");
    const data = await res.json();
    if (data.distance !== undefined) {
      distanceDisplay.textContent = `${data.distance.toFixed(1)} cm`;
    } else {
      distanceDisplay.textContent = "Aucune donnée";
    }
  } catch (err) {
    distanceDisplay.textContent = "Erreur";
    console.error(err);
  }
}

// Auto-refresh toutes les 5 secondes
setInterval(fetchDistance, 5000);

// Démarrage
fetchDistance();
