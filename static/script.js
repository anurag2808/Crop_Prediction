document.getElementById('crop-form').addEventListener('submit', async function(e) {
    e.preventDefault();

    const formData = new FormData(this);
    
    try {
        const response = await fetch('/predict', {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const result = await response.text();
        window.location.href = result;
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('result').innerHTML = `An error occurred: ${error.message}`;
    }
});