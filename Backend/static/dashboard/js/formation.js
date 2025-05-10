// Function to hide the specified element
function hideYouTubeOverlay() {
    document.querySelectorAll('.ytp-chrome-top.ytp-show-cards-title').forEach(el => el.style.display = 'none');
}

// Create a MutationObserver instance
const observer = new MutationObserver((mutationsList, observer) => {
    // Call the hideYouTubeOverlay function whenever mutations occur
    hideYouTubeOverlay();
});

// Start observing the document body for changes
observer.observe(document.body, { childList: true, subtree: true });

// Initial call to ensure the element is hidden if it's already present
hideYouTubeOverlay();






