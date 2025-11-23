document.addEventListener("DOMContentLoaded", () => {
  const wargaListContainer = document.getElementById("warga-list-container");
  const form = document.getElementById("formWarga");

  const apiUrl = "http://127.0.0.1:8000/api/warga/";

  // ================================
  // 1. Render elemen warga
  // ================================
  function renderWarga(warga) {
    const wargaDiv = document.createElement("div");
    wargaDiv.className = "warga-card";
    wargaDiv.style.border = "1px solid #ccc";
    wargaDiv.style.padding = "10px";
    wargaDiv.style.marginBottom = "10px";

    wargaDiv.innerHTML = `
            <h3>${warga.nama_lengkap}</h3>
            <p><strong>NIK:</strong> ${warga.nik}</p>
            <p><strong>Alamat:</strong> ${warga.alamat}</p>
            <p><strong>No. Telepon:</strong> ${warga.no_telepon}</p>
        `;

    return wargaDiv;
  }

  // ================================
  // 2. Ambil & tampilkan data warga
  // ================================
  function loadWarga() {
    fetch(apiUrl)
      .then((response) => {
        if (!response.ok) {
          throw new Error("Gagal memuat data.");
        }
        return response.json();
      })
      .then((data) => {
        wargaListContainer.innerHTML = ""; // kosongkan list

        // Jika API menggunakan pagination DRF, gunakan data.results
        const list = data.results ?? data;

        list.forEach((w) => {
          wargaListContainer.appendChild(renderWarga(w));
        });
      })
      .catch((error) => {
        wargaListContainer.innerHTML =
          "<p>Gagal memuat data. Pastikan server backend berjalan.</p>";
        console.error("Fetch error:", error);
      });
  }

  // Panggil pertama kali
  loadWarga();

  // ================================
  // 3. Form SUBMIT → POST data warga
  // ================================
  form.addEventListener("submit", (event) => {
    event.preventDefault();

    const newWarga = {
      nik: document.getElementById("nik").value,
      nama_lengkap: document.getElementById("nama_lengkap").value,
      alamat: document.getElementById("alamat").value,
      no_telepon: document.getElementById("no_telepon").value,
    };

    fetch(apiUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        // "Authorization": "Token ...."  <- jika backend pakai token
      },
      body: JSON.stringify(newWarga),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error("Gagal mengirim data");
        }
        return response.json();
      })
      .then(() => {
        form.reset();
        loadWarga(); // refresh list setelah data baru masuk
      })
      .catch((error) => {
        alert("Gagal mengirim data");
        console.error("POST error:", error);
      });
  });
});
