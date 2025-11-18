const modal = document.getElementById("accessModal");
const openLoginModal = document.getElementById("openLoginModal");
const heroOpenModal = document.getElementById("heroOpenModal");
const closeModal = document.getElementById("closeModal");

function openModal() {
    if (modal) {
        modal.classList.remove("hidden");
    }
}

function hideModal() {
    if (modal) {
        modal.classList.add("hidden");
    }
}

[openLoginModal, heroOpenModal].forEach((btn) => {
    if (btn) {
        btn.addEventListener("click", openModal);
    }
});

if (closeModal) {
    closeModal.addEventListener("click", hideModal);
}

if (modal) {
    modal.addEventListener("click", (event) => {
        if (event.target === modal || event.target.classList.contains("modal-backdrop")) {
            hideModal();
        }
    });
}
