document.addEventListener('DOMContentLoaded', function() {
    const resultContainer = document.querySelector('.result-container');
    resultContainer.style.opacity = '0';
    resultContainer.style.transition = 'opacity 0.5s ease-in-out';
    
    const crop = document.getElementById('crop-name').textContent;
    
    // Fetch the growing tips
    fetch(`/get_growing_tips?crop=${encodeURIComponent(crop)}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('growing-tips').innerHTML = data.growing_tips;
            document.getElementById('crop-image').src = `/static/images/${crop.toLowerCase()}.jpg`;
            
            resultContainer.style.opacity = '1';
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('growing-tips').textContent = 'Error loading growing tips';
            resultContainer.style.opacity = '1';
        });
});